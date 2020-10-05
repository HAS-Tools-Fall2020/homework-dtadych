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

#%%
#1) Use the function fill.na to fill the na values with 999
data_frame.fillna(999)
print(data_frame)
#%%
#2) Turn the 999 values back to nas. See how many different ways you can do this 