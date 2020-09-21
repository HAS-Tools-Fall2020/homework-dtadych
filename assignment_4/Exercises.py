# %%
import numpy as np

# %%
avg_monthly_precip = np.array([0.70, 0.75, 1.85])

print(avg_monthly_precip)
# %%
p02_03 = np.array([
    [1, 0.4, 1.5],
    [0.27, 1.13, 1.72]
])
print(p02_03)

# %%
#automatically retrieving data from usgs

conda install -c conda-forge  dataretrieval

#%%
import dataretrieval.nwis as nwis

site = '09506000'

# %%
daily

##--^ try this again later

# %%
# writing this so I don't forget it - shift+enter makes a new cell
# I know there are cheat sheets but this will help me remember

# Import necessary packages
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)
# %%

streamflow = np.loadtxt(filename)