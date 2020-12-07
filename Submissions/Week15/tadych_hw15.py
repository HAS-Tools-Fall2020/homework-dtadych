# HAS TOOLS - Forecast 15
# Danielle Tadych

import numpy as np
import pandas as pd

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

url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=' \
      'rdb&site_no=09506000&referred_module=sw&period=&begin_date' \
      '=1989-01-01&end_date=2020-12-5'

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

# Actual Forecast

# Only going to use 2020 October daily flows to predict
# Since it's been increasing slightly, I'm using the october mean
# for week 1 forecast and mean plus the standard deviation for week 2
november = getflowyrmo(data, 2020, 11)
december = getflowyrmo(data, 2020, 12)
november = november.append(december)
print(november)

week1_forecast = np.mean(november['flow'].tail(2))
week2_forecast = week1_forecast + np.std(november['flow'])

# Seasonal Forecast

# Just going to use the last months of 2019 since it also
# is a record dry year
semestermonths = [8, 9, 10, 11, 12]
semester2009 = pd.DataFrame()

for i in semestermonths:
    semesterflow = getflowyrmo(observedweeklyflow, 2009, i)
    semester2009 = semester2009.append(semesterflow)

# Printing all the results

print()
print("Actual Forecast:")
print("Week 1: ", np.round(week1_forecast, decimals=2), "cfs")
print("Week 2: ", np.round(week2_forecast, decimals=2), "cfs")
print()
print("Seasonal Forecast:")
print(semester2009)
# %%
