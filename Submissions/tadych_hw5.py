#Homework 5 Code

# stream gauge is Station 09506000 Verde River Near Camp Verde

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :) 
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.

#%%
## Experimenting Filtering Data

flow2019=data[data["year"]==2019]
# %%
flowsep2019=flow2019[flow2019["month"]==9]
# %%
#From the lessons - a quick plot
f, ax = plt.subplots()
avg_monthly_precip.plot(x="month",
                        y="precip_in",
                        title="Plot of Pandas Data Frame using Pandas .plot",
                        ax=ax)
plt.show()

#%%
#Trying it with flow
f, ax = plt.subplots()
ax.plot(flowsep2019.day,
        flowsep2019.flow)

ax.set(title="Plot of Sep 2019 flow (cms)")
plt.show()

#%%
# Group by functions
# dataframe.groupby(['label_column'])[["value_column"]].method()

monthstats = data.groupby(['month'])[["flow"]].describe()
monthstats

#%%
# Histogram from lesson
f, ax = plt.subplots()

ax.bar(x=avg_monthly_precip.months,
       height=avg_monthly_precip.precip,
       color="purple")

ax.set(title="Plot of Average Monthly Precipitation in mm")
plt.show()
# %%
#Forecasting stuff


#%%
### Questions
#Number 1
data.info
# %%
data.columns
# %%
#
data[["flow"]].describe()
# %%
# Number 2
monthstats = data.groupby(['month'])[["flow"]].describe()
monthstats

#%%
# Number 3
#  Five Highest
print(data.flow.nlargest(5))

        
#%%
print(data.month[data.flow.nlargest(5).index])
print(data.flow[data.flow.nlargest(5).index])

print(data.datetime[data.flow.nsmallest(5).index])
print(data.month[data.flow.nsmallest(5).index])
print(data.flow[data.flow.nsmallest(5).index])
# Five Lowest