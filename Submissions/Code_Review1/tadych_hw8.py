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


def getflowyr(data_set, year):
    'This function can create a pandas data frame filtered by year.'
    q = pd.DataFrame(data_set[data_set['year'] == year])
    print(q)
    return q


def getflowyrmo(data_set, year, month):
    'Can create a pandas dataframe filtered by year and month.'
    q = pd.DataFrame(data_set[(data_set['year'] == year)
                              & (data_set['month'] == month)])
    print(q)
    return q


def getflowymw(data_set, year, month, week):
    'Can create a pandas data frame filtered by year, month, and week'
    q = pd.DataFrame(data_set[(data_set['year'] == year)
                              & (data_set['month'] == month)
                              & (data_set['weeknumber'] == week)])
    print(q)
    return q


# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week8.txt'
filepath = os.path.join('../../data', filename)
# filepath = os.path.join('../../data', filename)
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

# Using a for loop and the functions to create new weekly dataframe
droughtyrs = [2002, 2004, 2011, 2019, 2020]
flow_weeklytest = pd.DataFrame()

for k in droughtyrs:
    f = getflowyr(flow_weekly, k)
    flow_weeklytest = flow_weeklytest.append(f)
#    print(flow_weeklytest)

# %%
# Add a column for new week number for easier indexing later
#  and without messing with datetime.
#  I think there is an easier way to do this but I didn't
#  get a chance to flesh it out.

flow_weeklytest['randonum'] = 1
flow_weeklytest['weeknumber'] = flow_weeklytest['randonum'].cumsum(axis=0)
flow_weeklytest.pop('randonum')
# print(flow_weeklytest)

# %%
# Replacing the old flow weekly with the test one now that everything
# looks okay
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
lastweekflow = observedweeklyflow.tail(2)

lastweekflowtest = lastweekflow.iloc[0]['flow']

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
# Seasonal Forecast

# Just going to use the last months of 2019 since it also
# is a record dry year
semestermonths = [8, 9, 10, 11, 12]
semester2019 = pd.DataFrame()

for i in semestermonths:
    semesterflow = getflowyrmo(flow_weekly, 2019, i)
    semester2019 = semester2019.append(semesterflow)

# Cleaning up the new dataframe for prettier viewing
del(semester2019["flow_tm1"], semester2019["flow_tm2"],
    semester2019["site_no"])

# %%
# Printing all the results

print("Autoregression Model Results:")
print("Week 1: ", np.round(week1_AR, decimals=2), "cfs")
print("Week 2: ", np.round(week2_AR, decimals=2), "cfs")
print()
print("Actual Forecast:")
print("Week 1: ", np.round(week1_forecast, decimals=2), "cfs")
print("Week 2: ", np.round(week2_forecast, decimals=2), "cfs")
print()
print("Seasonal Forecast:")
semester2019
# %%
