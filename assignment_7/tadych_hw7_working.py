# HAS TOOLS - Forecast 7
# Danielle Tadych

# AR Forecast strategy:
#  From previous homeworks, I picked out years where Semptember
#   had flows below 60 cfs.  These I dubbed "drought years".
#   droughtyrs = [2002, 2004, 2011, 2019, 2020]
#  I then filtered the data for just these years and used this
#   as training data

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
# Note you may need to do pip install for sklearn

# Defining some functions to filter the data


def getflowyr(datum, year):
    q = pd.DataFrame(datum[datum['year'] == year])
    print(q)
    return q


def getflowyrmo(datum, year, month):
    q = pd.DataFrame(datum[(datum['year'] == year)
                           & (datum['month'] == month)])
    print(q)
    return q


def getflowymw(datum, year, month, week):
    q = pd.DataFrame(datum[(datum['year'] == year)
                           & (datum['month'] == month)
                           & (datum['weeknumber'] == week)])
    print(q)
    return q

# %%


# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week7.txt'
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
#    print(flow_weeklytest)

# %%
# Add a column for new week number for easier indexing
#  without messing with datetime

flow_weeklytest['randonum'] = 1
flow_weeklytest['weeknumber'] = flow_weeklytest['randonum'].cumsum(axis=0)
flow_weeklytest.pop('randonum')
# print(flow_weeklytest)

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
# %%
lastweekflowtest = observedweeklyflow.iloc[1657]['flow']

week1_AR = model.intercept_ + model.coef_ * lastweekflowtest
week2_AR = model.intercept_ + model.coef_ * week1_AR

# %%
# Actual Forecast

# Only going to use 2020 October daily flows to predict
# Since it's been increasing slightly, I'm using the october mean
# for week 1 forecast and mean plus the standard deviation for week 2
# %%
october = getflowyrmo(data, 2020, 10)

week1_forecast = np.mean(october['flow'])
week2_forecast = week1_forecast + np.std(october['flow'])

# %%
# Printing stuff

print("Autoregression Model Results:")
print("Week 1: ", np.round(week1_AR, decimals=2), "cfs")
print("Week 2: ", np.round(week2_AR, decimals=2), "cfs")
print()
print("Actual Forecast:")
print("Week 1: ", np.round(week1_forecast, decimals=2))
print("Week 2: ", np.round(week2_forecast, decimals=2))

# %%
