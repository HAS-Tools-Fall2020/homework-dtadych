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
flowsep2019=flow2019[(flow2019["month"]==9)&(flow2019["month"])]
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

#All september flows by day
flowsep=data[data["month"]==9]
f, ax = plt.subplots()
ax.plot(flowsep.day,
        flowsep.flow)

ax.set(title="Plot of Sep flow (cms)")
#%%
flowsep2020=flowsep[flowsep["year"]==2020]
f, ax = plt.subplots()
ax.plot(flowsep2020.day,
        flowsep2020.flow,
        flowsep2019.day,
        flowsep2019.flow)

ax.set(title="Plot of Sep flow (cms)")
ax.legend()
#%%
#semester months 2019
flowoct=data[data["month"]==10]
flownov=data[data["month"]==11]
flowdec=data[data["month"]==12]
flowoct2019=flowoct[flowoct["year"]==2019]
flownov2019=flownov[flownov["year"]==2019]
flowdec2019=flowdec[flowdec["year"]==2019]

#%%
f, ax = plt.subplots()
ax.plot(flowsep2019.day,
        flowsep2019.flow,
        flowoct2019.day,
        flowoct2019.flow,
#        flowsep2020.day,
#        flowsep2020.flow,
        flownov2019.day,
        flownov2019.flow,
        flowdec2019.day,
        flowdec2019.flow)
ax.legend("SOND")
ax.set(title="Plot of Semester flow (cms)")

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
data.flow.nlargest(5)
#%%
data.flow.nsmallest(5)
#%%
data.iloc[8582]
#%%
data.iloc[8583]
#%%
data.iloc[8581]
#%%
data.iloc[8580]
#%%
data.iloc[8584]

#%%
#Number 4
for i in range(1, 13):
        print(i)
        print(data.flow[data.month == (i)].nlargest(1))
        print(data.year[data.flow[data.month == (i)].nlargest(1).index])

print('\n')

for i in range(1, 13):
        print(i)
        print(data.flow[data.month == (i)].nsmallest(1))
        print(data.year[data.flow[data.month == (i)].nsmallest(1).index])


# Five Lowest
# %%
#Number 6
prediction = 60
tenperc = prediction*0.1
print(tenperc)
# %%
flowrng = (prediction - tenperc, prediction + tenperc)
print(flowrng)

#%%
historical = data.datetime[(data['flow']>flowrng[0])&(data['flow']<flowrng[1])]
print(historical)
