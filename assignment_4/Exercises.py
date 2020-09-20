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