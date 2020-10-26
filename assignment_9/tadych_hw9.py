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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json
import urllib.request as req
import urllib
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
# Read the data into a pandas dataframe

url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=' \
      'rdb&site_no=09506000&referred_module=sw&period=&begin_date' \
      '=1989-01-01&end_date=2020-10-24'

# Read the data into a pandas dataframe

data = pd.read_table(url, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow',
                            'code'], parse_dates=['datetime'], 
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to week and subset full dataset
flow_weekly = data.resample("W", on='datetime').mean()
observedweeklyflow = flow_weekly

# %%
# ~ Working with API's ~
# copy past from the starter code

mytoken = 'KygI8ZkKTIl5y03KGWd56C15e14MH5UAmID3cqCRnJ'

# Daymet Example:
# You can get Daymet data for a single pixle form this site:
#https: // daymet.ornl.gov/single-pixel/ 
# You can also experiment with their API Here: 
# https: // daymet.ornl.gov/single-pixel/api  

# Example reading it as a json file
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.9455&lon=-113.2549"  \
       "&vars=prcp&format=json"
response = req.urlopen(url)
# Look at the kesy and use this to grab out the data
responseDict = json.loads(response.read())
responseDict['data'].keys()
year = responseDict['data']['year']
yearday = responseDict['data']['yday']
precip = responseDict['data']['prcp (mm/day)']

# make a dataframe from the data
daymetdata = pd.DataFrame({'year': year,
                     'yearday': yearday, "precip": precip})

# %%
# Fix from Diana to get date time to work
# Changing the data into strings, then slicing part of the data so that after
# added them together the to_datetime function would work

daymetdata["year"] = daymetdata["year"].astype(str)
daymetdata["yearday"] = daymetdata["yearday"].astype(str)
daymetdata["year"] = daymetdata["year"].str.slice(0, -2)
daymetdata["yearday"] = daymetdata["yearday"].str.slice(0, -2)
daymetdata["newyearday"] = daymetdata["year"].str.cat(daymetdata["yearday"], sep = ' ')
daymetdata["datetime"] = pd.to_datetime(daymetdata.newyearday, format='%Y %j')
# %%
# Expand the dates to year month day
daymetdata['year'] = pd.DatetimeIndex(daymetdata['datetime']).year
daymetdata['month'] = pd.DatetimeIndex(daymetdata['datetime']).month
daymetdata['day'] = pd.DatetimeIndex(daymetdata['datetime']).dayofweek
daymetdata['dayofweek'] = pd.DatetimeIndex(daymetdata['datetime']).dayofweek

# %%
# Aggregate weekly
precip_weekly = daymetdata.resample("W", on='datetime').mean()
print(precip_weekly)
# %%

# Using a for loop and the functions to create new weekly dataframe
droughtyrs = [2002, 2004, 2011, 2019]
flow_weeklytest = pd.DataFrame()
precip_test = pd.DataFrame()

for k in droughtyrs:
    f = getflowyr(flow_weekly, k)
    flow_weeklytest = flow_weeklytest.append(f)
    potato = getflowyr(precip_weekly, k)
    precip_test = precip_test.append(potato)
    print(flow_weeklytest)
    print(precip_test)

# %%
# Replacing the old flow weekly with the test one now that everything
# looks okay
flow_weekly = flow_weeklytest

# %%
# Fixing issue with precip_test
precip_test.drop(precip_test.tail(1).index,inplace=True)

# %%
# Building an linear model
model = LinearRegression()
x = flow_weekly['flow'].values.reshape(-1, 1)
y = precip_test['precip'].values
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

# %%
# Printing all the results

print("Model Results:")
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
