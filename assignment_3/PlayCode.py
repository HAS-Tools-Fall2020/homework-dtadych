# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
filepath = os.path.join('/Users/danielletadych/Documents/FALL2020/Coding/homework-dtadych/data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework. 
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
print("This is minimum flow:",min(flow))
print("This is maximum flow:",max(flow))
print("This is average flow:",np.mean(flow))
print("This is standard deviation of flow:",np.std(flow))

# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] > 600 and month[i] == 7:
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print("number of flow values greater than 600:",len(ilist))

# Alternatively I could have  written the for loop I used 
# above to  create ilist like this
ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==7]
print("List Comprehension Example:",len(ilist2))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
subset = [flow[j] for j in ilist]
print("Pulling out the data:",subset)

#%%
# New Code
#week1 forecast
#making a week 1 list
Week1historical = []
w1days = [13, 14, 15, 16, 17, 18, 19]

#---vv- didn't work-vv-----
#creating a list of all values for september 13-19
w1days = [13, 14, 15, 16, 17, 18, 19]
Week1 = [k for k in range(len(flow)) if month[k]==9 and day[k]==w1days]
print("chacking datapoints",len(Week1))
w1f = [flow[k] for k in Week1]
print("Pulling out the data:",w1f)

#getting values
print("Week 1 Statistics")
print("Min:",min(w1f))
print("Max:",max(w1f))
print("Avg:",np.mean(w1f))
print("Stdev:",np.std(w1f))
# %%
#Gonna try some else if and for loops

for i in range(flow):
        if  month[i]==9 and day[i]==w1days:
                ilist.append(i)
                print(i)

# %%
#if else
if month==9:
        print("Week 1 Statistics")
        print("Min:",min(flow))
        print("Max:",max(flow))
        print("Avg:",np.mean(flow))
        print("Stdev:",np.std(flow))
#------------------------
# %%

#CODE THAT ACTUALLY WORKS
for i in range(len(flow)):
        if month[i] == 9 and day[i]==w1days:
                Week1historical.append(i)
# %%
Week1 = [flow[j] for j in Week1historical]
print(Week1historical)
# %%
print("Week 1 Statistics")
print("Min:",min(Week1historical))
print("Max:",max(Week1historical))
print("Avg:",np.mean(Week1historical))
print("Stdev:",np.std(Week1historical))
# %%
# WEEK 2 FORECAST

W2historical = []
w2days = [20, 21, 22, 23, 24, 25, 26]

for i in range(len(flow)):
        if month[i] == 9 and day[i] == w2days:
                W2historical.append(i)
# %%
Week2 = [flow[j] for j in W2historical]
print(W2historical)
# %%
print("Week 1 Statistics")
print("Min:",min(W2historical))
print("Max:",max(W2historical))
print("Avg:",np.mean(W2historical))
print("Stdev:",np.std(W2historical))

#%%
#--- starting over


# Making and empty list that I will use to store
# index values I'm interested in
w1h = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if  month[i] == 9 and day[i] >=13 and day[i]<=19:
                w1h.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(len(w1h))

#%%
# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
week1 = [flow[j] for j in w1h]
#%%
print("Pulling out the data:", week1)
# %%
print("Week 1 Statistics:")
print("Min:",min(week1))
print("Max:",max(week1))
print("Avg:",np.mean(week1))
print("Stdev:",np.std(week1))
# %%

#%%
#week 2 again
w2h = []
for i in range(len(flow)):
        if  month[i] == 9 and day[i] >=20 and day[i]<=26:
                w2h.append(i)

week2 = [flow[j] for j in w2h]
print("Week 2 Statistics:")
print("Min:",min(week2))
print("Max:",max(week2))
print("Avg:",np.mean(week2))
print("Stdev:",np.std(week2))
# %%
#Forecast for the rest of the semester
ltw = []
for i in range(len(flow)):
        if  month[i] == 9 and day[i] >=6 and day[i]<=12 and year[i]<2020:
                ltw.append(i)

#for i in range(len(flow)):
#        if  month[i] == 11 and day[i] >=29 and day[i]<=30 and year[i]<2020:
#                ltw.append(i)

ltweek = [flow[j] for j in ltw]
print("ltw Statistics:")
print("Min:",min(ltweek))
print("Max:",max(ltweek))
print("Avg:",np.mean(ltweek))
print("Stdev:",np.std(ltweek))
# %%
#Answering Questions
Q = []
for i in range(len(flow)):
        if  month[i] == 9 and day[i] >=16 and day[i]<=30 and year[i]<2020:
                Q.append(i)


#for i in range(len(flow)):
#        if  month[i] == 11 and day[i] >=29 and day[i]<=30 and year[i]<2020:
#                ltw.append(i)

Qval = [flow[j] for j in Q]
print("ltw Statistics:")
print("length:",len(Qval))
print("Min:",min(Qval))
print("Max:",max(Qval))
print("Avg:",np.mean(Qval))
print("Stdev:",np.std(Qval))

# %%
