# HAS TOOLS - Forecast 7
# Danielle Tadych

# AR Forecast strategy:
#  From previous homeworks, I picked out years where Semptember
#   had flows below 60 cfs.  These I dubbed "drought years".
#   droughtyrs = [2002, 2004, 2011, 2019, 2020]
#  I then filtered the data for just these years and used this
#  as training data  

# %%
# Defining some functions to filter the data
def getflowyr(datum, year):
        q = pd.DataFrame(datum[datum['year'] == year])
        print(q)
        return q
def getflowyrmo(datum, year, month):
        q = pd.DataFrame(datum[(datum['year'] == year) & (datum['month'] == month)])
        print(q)
        return q
def getflowymd(datum, year, month, day):
        q = pd.DataFrame(datum[(datum['year'] == year) & (datum['month'] == month) & (datum['day'] == day)])
        print(q)
        return q

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
# Note you may need to do pip install for sklearn

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'])

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to week and subset full dataset
flow_weekly = data.resample("W", on='datetime').mean()
observedweeklyflow = flow_weekly

# %%

droughtyrs = [2002, 2004, 2011, 2019, 2020]
# droughtmos = range(1, 12)
flow_weeklytest = pd.DataFrame()

for k in droughtyrs:
    f = getflowyr(flow_weekly, k)
    flow_weeklytest = flow_weeklytest.append(f)
    print(flow_weeklytest)

#%%
# Add a column for new week number for easier indexing without messing with datetime
flow_weeklytest['randonum'] = 1
flow_weeklytest['weeknumber'] = flow_weeklytest['randonum'].cumsum(axis=0)
flow_weeklytest.pop('randonum')
print(flow_weeklytest)

# %%
# Now that the dataframe looks okay
flow_weekly = flow_weeklytest

# %%
# Building an autoregressive model
# You can learn more about the approach I'm following by walking
# Through this tutorial
# https://realpython.com/linear-regression-in-python/

# Step 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)


# %%
# Step 2 - pick what portion of the time series
#          you want to use as training data

# training with data years prior to 2020 and testing with 2020
train = flow_weekly[2:204][['flow', 'flow_tm1', 'flow_tm2']]
test = flow_weekly[205:][['flow', 'flow_tm1', 'flow_tm2']]

# Step 3: Fit a linear regression model using sklearn
model = LinearRegression()
x = train['flow_tm1'].values.reshape(-1, 1)
#  See the tutorial to understand the reshape step here
y = train['flow'].values
model.fit(x, y)

# Look at the results
# r^2 values
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

# print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Step 4 Make a prediction with your model
# Predict the model response for a  given flow value
q_pred_train = model.predict(train['flow_tm1'].values.reshape(-1, 1))
q_pred_test = model.predict(test['flow_tm1'].values.reshape(-1, 1))

#altrenatievely you can calcualte this yourself like this: 
q_pred = model.intercept_ + model.coef_ * train['flow_tm1']

# you could also predict the q for just a single value like this
last_week_flow = 500
prediction = model.intercept_ + model.coef_ * last_week_flow

# %%
lastweekflowtest = observedweeklyflow[(observedweeklyflow['year'] == 2020) 
                                       & (observedweeklyflow['month'] == 9)
                                       & (observedweeklyflow['year'] == 27)]
print(lastweekflowtest)


# %%
# Another example but this time using two time lags as inputs to the model
model2 = LinearRegression()
x2 = train[['flow_tm1', 'flow_tm2']]
model2.fit(x2, y)
r_sq = model2.score(x2, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 2))

# generate preditions with the funciton
q_pred2_train = model2.predict(train[['flow_tm1', 'flow_tm2']])

# or by hand
q_pred2 = model2.intercept_   \
         + model2.coef_[0] * train['flow_tm1'] \
         + model2.coef_[1] * train['flow_tm2']

# %%
# Here are some examples of things you might want to plot to get you started:

# 1. Timeseries of observed flow values
# Note that date is the index for the dataframe so it will
# automatically treat this as our x axis unless we tell it otherwise
fig, ax = plt.subplots()
ax.plot(observedweeklyflow['flow'], label='full')
ax.plot(train['flow'], 'r:', label='training')
ax.plot(test['flow'], '--', label='test')
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
ax.legend()
# an example of saving your figure to a file
fig.set_size_inches(5, 3)
# fig.savefig("Observed_Flow.png")

# %%
# 2. Time series of flow values with the x axis range limited
fig, ax = plt.subplots()
ax.plot(observedweeklyflow['flow'], color='green', label='Observed Flow')
ax.plot(train['flow'], 'r:', label='Training Period')
ax.set(title="Timeseries of Observed and Training periods", xlabel="Date",
        ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2000, 1, 26), datetime.date(2020, 12, 1)])
fig.savefig("Timeseries of Observed and Training periods")

ax.legend()

#%%
# 3. Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots()
ax.plot(train['flow'], color='grey', linewidth=2, label='observed')
ax.plot(train.index, q_pred2_train, color='green', linestyle='--', 
        label='simulated')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.legend()

#%%
# 4. Scatter plot of t vs t-1 flow with log log axes
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='p',
              color='blueviolet', label='obs')
ax.set(xlabel='flow t-1', ylabel='flow t', yscale='log', xscale='log')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), color='orange', label='AR model')
ax.legend()
fig.savefig("AR Model")

#%%
# 5. Scatter plot of t vs t-1 flow with normal axes
fig, ax = plt.subplots()
ax.scatter(train['flow_tm1'], train['flow'], marker='p',
              color='blueviolet', label='observations')
ax.set(xlabel='flow t-1', ylabel='flow t')
ax.plot(np.sort(train['flow_tm1']), np.sort(q_pred_train), label='AR model')
ax.legend()

plt.show()

# %%
## Actual Forecast

import matplotlib.ticker as ticker

#%%
#Make a plot of Observed flows in 2019 for semester
fig, ax = plt.subplots()
ax.plot(flow2019['flow'], color='green', linewidth=2, label='2019 observed')
ax.set(title="2019 Semester flows", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2019, 8, 1), datetime.date(2019, 12, 31)])
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
fig.savefig("2019 Fall Semester Flows")
# %%
flow2019[flow2019['month']==10].describe()
# %%
#Make a plot of Observed flows in 2020 for semester
fig, ax = plt.subplots()
ax.plot(flow2020['flow'], color='blue', linewidth=2, label='2020 observed')
ax.set(title="2020 Semester Flows", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
         ylim=[0,200], xlim=[datetime.date(2020, 8, 1), datetime.date(2020, 10, 3)])
ax.xaxis.set_major_locator(ticker.MultipleLocator(12))
fig.savefig("2020 Fall Semester Flows")
plt.show()

#%%
flow2020[flow2020['month']==9].describe()
# %%
flow2019[flow2019['month']==10].describe()

# %%
flow2019[flow2019['month']==11].describe()
#%%
flow2019[flow2019['month']==12].describe()

# %%
