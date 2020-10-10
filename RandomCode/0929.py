#%%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
data = np.ones((7,3))
data_frame = pd.DataFrame(data,
            columns = ['data1','data2','data3'],
            index=['a','b','c','d','e','f','g'])

#%%
data_frame.loc[['a', 'e']] = 3
# %%
#A) Change the values for all of the vowel rows to 3 


# %%
#B) multiply the first 4 rows by 7 
data_frame1 = data_frame.iloc[:4,] * 7
    #:4 means everything up to 4
data_frame1

# %%
#C) Make the dataframe into a checkerboard  of 0's and 1's using loc 
data_frame2 = data_frame.loc[['a','b','c','d','e','f','g'],['data1', 'data3']]=0
data_frame2.loc[['a','b','c','d','e','f','g'],['data1', 'data3']]=0
#remeber when doing loc stuff,, remember to put things in brackets because you're giving it lists of things

# %%
#D) Do the same thing without using loc 

dataframe3 = data_frame.iloc[]

### Homework
#from Alcely
dataframe.to_markdown()

# get plugin for atom
# go and look at the answer sheet

### Notes
# Cheat sheets are beautiful, go look at them
# rules - don't make anything more than linear regression model
# Don't have to be bound by model to make forecast
# Will make our codes pretty next week
# 2 weeks from now someone else is going to take our code and forecast for us

#%%
data_frame = pd.DataFrame([[1, np.nan, 2],[2, 3, 5],[np.nan, 4, 6]])
print(data_frame)
#%%
#1) Use the function fill.na to fill the na values with 999
dataf2 = data_frame.fillna(999)
dataf2
#%%
#2) Turn the 999 values back to nas. See how many different ways you can do this
dataf2[dataf2.isnull()] = np.nan
dataf2
# %%
dataf3
# %%
#NaN is special, not a number, so we can't do computations with it

#Random plotting notes
# adding fig creates an object
# ax are the graphs inside the object (figure)


# %%
# Class work for 10/5/2020
# Given the following series of flow values and days Assume that the flow has uncertainty of +/- 25%
# Come up with a way to visualize this information

flow = np.random.randn(100)
day = range(len(flow))
stdev = 0.25
upperrange = flow + flow*0.25
lowerrange = flow - flow*0.25

# %%
fig, ax = plt.subplots()
ax.plot(flow, color='blue', linewidth=1, label='flow')
ax.plot(upperrange, color='orange', linewidth=0, label='stdev')
ax.plot(lowerrange, color='orange', linewidth=0, label='flow')
ax.fill_between(day, upperrange, lowerrange, color='orange')
ax.set(title="Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]")

# %%
# Functions
x = np.arange(2, 11).reshape(3,3)
y = 3
answer = np.floor(np.divide(x,y))
print(x)
print(answer)
# %%
def get_floor(numerator, denominator):
    fl = np.floor(np.divide(numerator, denominator))
    print(fl)
    return fl

floor = get_floor(x, y)
# %%
def potatofamine():
    
# %%
# Doc Strings


def get_floor(numerator, denominator):
    """ Function to do floor divide

    Look at this sexy function!  It divides two
    things that are np arrays
    numerator = np.array...
    denominator = np.array...
    """
    fl = np.floor(np.divid(numerator, denominator))
    print("You did the thing")
    print (fl)
    return fl

randomstuff = get_floor(x, y)
# %%
