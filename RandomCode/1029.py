# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json
import urllib.request as req
import urllib
from sklearn.linear_model import LinearRegression

import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx

# %%
# Grab daymet precip data
# (daymet.ornl.gov/single-pixel/)
# Grab data using base URL and API strings
base_url1 = "https://daymet.ornl.gov/single-pixel/api/data"

args1 = {
    'lat': '34.448',
    'lon': '-111.789',
    'vars': 'prcp',
    'start': '1989-01-01',
    'end': '2020-10-24',
    }
apiString1 = urllib.parse.urlencode(args1)

fullUrl1 = base_url1 + '?' + apiString1 + "&format=json"
print(fullUrl1)
daymet_precip = req.urlopen(fullUrl1)

# Load json file and look at the keys for json download
daymet_precipDict = json.loads(daymet_precip.read())
daymet_precipDict.keys()

# Make a dataframe from the data
 
year = daymet_precipDict['data']['year']
yearday = daymet_precipDict['data']['yday']
precip = daymet_precipDict['data']['prcp (mm/day)']
 
precipdata = pd.DataFrame({'year': year,
                           'yearday': yearday, "precip": precip})
precipdata.set_index('year')
precipdata.head()

# Convert to datetime and add column
date_time = pd.to_datetime(precipdata['year'] * 1000 +
                           precipdata['yearday'], format='%Y%j')
precipdata['datetime'] = date_time
precipdata.set_index('datetime')
 
# Get year month day for precipdata
precipdata['year'] = pd.DatetimeIndex(precipdata['datetime']).year
precipdata['month'] = pd.DatetimeIndex(precipdata['datetime']).month
precipdata['day'] = pd.DatetimeIndex(precipdata['datetime']).day
precipdata
 
# Aggregate to weekly mean precip (precip_weekly)- with a start day of Saturday
precip_weekly = precipdata.resample("W-SAT", on='datetime').mean()
precip_weekly[["precip"]]	
# %%
# Reading it using geopandas
file = os.path.join('/Users/danielletadych/Documents/PhD_Materials/Data/Groundwater/GWSI_ZIP_04142020/GWSI_Shape/', 'GWSI_SITES.shp')
gages = gpd.read_file(file)

# %%
type(gages)
#%% 
gages.head()
# %%
gages.columns
gages.shape
# %%
gages.geom_type
# %%
gages.crs
#%%
fig, ax = plt.subplots(figsize=(5,5))
gages.plot(ax=ax)
plt.show
# %%
file = os.path.join('/Users/danielletadych/Documents/PhD_Materials/Data/Maps/GovUnits/government_units_NRCSCNTY_mbr_3824988_02
', 'county_nrcs_a_mbr.gdb')
counties = gpd.read_file(file)
# %%
