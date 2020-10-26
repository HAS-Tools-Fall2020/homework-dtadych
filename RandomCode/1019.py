# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

filename = 'streamflow_week1.txt'
filepath = os.path.join('../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no','datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime')

# %%
# Return the streamflow January 3-5 as many ways as you can 1989
data.iloc[2:5]
data.loc["198"]

# %%
# Content Notes

# ~ Data stuff ~
# This is how we've been reading data

# Option 1 - you have a file locally that you want to read:
#   1) you need file location (os.path.join)
#   2) you need to know how the file is formatted so you can read it correctly
filename = 'streamflow_week1.txt'
filepath = os.path.join('../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no','datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime')

# so first download the data, then look at it
# then go to pandas.read_table description page
# fix it accordingly

# %%
# Option 2 - Read the data from a url rather than a local file
# You need:
#   1) the location of the data - this time on the internet
#   2) how it is formatted

url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000&referred_module=sw&period=&begin_date=1989-01-01&end_date=2020-10-17"

data2 = pd.read_table(url, skiprows=30,
                     names=['agency_cd', 'site_no','datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime')

# This URL is suprisingly predictabile

# %%
site = "09506000"
start = "1989-01-01"
end = "2020-10-19"
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
      "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end

data3 = pd.read_table(url, skiprows=30,
                     names=['agency_cd', 'site_no','datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime')

# %%
# Option 3 - we can generate this url and get the data using an API
# Technically we were already doing this, you just didn't know :O
# API = Application programming interface (translation - a standard set of approaches/protocols
#   for working with a given dataset in a predictable way.  E.g. rules for accessing data)

# Different datasets have their own APIs
# 1) step 1, see if there is an API and get the rules for working with it

