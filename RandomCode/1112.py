
#%%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1) Load in your streamflow timeseries from your data folder like this:
filename = 'streamflow_week1.txt'
filepath = os.path.join('../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                      names=['agency_cd', 'site_no',
                             'datetime', 'flow', 'code'],
                      parse_dates=['datetime'], index_col='datetime'
                      )

# %%
# Return the streamflow January 10-12 as many ways as you can
data.head()
# %%
data['flow'].iloc[9:12]
#%%
data['flow'].loc['1989-01-10':'1989-01-12']
# %%
    q = pd.DataFrame(data_set[data_set['year'] == year])

data[['year']]