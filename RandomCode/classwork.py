#%%
# EXERCISE 1: 
#1a.  Create a 3X3 matrix with values ranging from 2-10  

xb=np.reshape(np.arange*2,33,2),(4,4))

#1.b  Make a matrix with all of the even values from 2-32


# 1.c Make a matrix with all of the even values from 2-32
# But this time have the values arrange along columns rather than rows


#%%
import numpy as np
#%%
arr_zero = np.ones(10)
# %%

#9.24.20

# BONUS:
# Create the same 3x3 matrix with value ranging from 2-10 as you did 
# in part a but this time do so by combining one 3X1 matrix and one 1X3 matrix

#we can do this by broadcasting


x=np.arange(2,5,1)
y=np.arange(0,7,3).reshape(3,1)
print(x)
print(y)
# %%
z=x*y
# %%
#what happens when we add x to the array
z2=z+x
print(z2)
#added across

# %%
#new Exercise
#1. Get the largest integer that is less than or equal to the division of the 
# inputs x1 and x2 where x1 is all the integers from 1-10 and x2=1.3# 

#%%
# 2. given an array x1=[0, 4, 37,17] and a second array with the values# 
# x2=[1.2, 3, 4.6, 7] return x1/x2 rounded to two decimal places# 
x1=np.array([0, 4, 37,17])
x2=np.array([1.2, 3, 4.6, 7])
x1/x2

np.round(np.divide(x1,x2), decimals=2)

#%%
#do this next week

# 3. Create a 10 by 100 matrix with 1000 random numbers and 
# report the # average and standard deviation across the entire matrix and 
# for each of the 10 rows. Round your answer to  two decimal places

#hint:
#np.random, np.round, np.mean, np.std

#%%
# PANDAS
# With pandas - we can name our rows and columns and refer to them by names
# We dont' have to have just one data type like with numpy
# Laura has been using Pandas and then turning them into simpler things to play with
# Can also sometimes make it confusing tho
# Builds off of numpy, so most of the things we do in numpy can work pandas
import pandas as pd

# %%
# three things we can make - series, dataframes, and indices
## Series - 1D array (case sensitive)
data = pd.Series([0.1, 50, 47, 1.376])
print(data)
#could also make a list and only have thesenumbers
data0=[0.1, 50, 47, 1.376]
data0
# %%
# note, it has an extra columan which is the index
# can grab elements from a series by referencing the index
data[1:3]
# %%
# Or we can name our index differently
data = pd.Series([0.1, 50, 47, 1.376], index=['a', 'b', 'c', 'd'])
data

# %%
#So, our series has 2 things = values and indices
data.values #gives us just values

data.index #gives us just index
# %%
# Dataframes
#  These are like eries but in 2D so we have rows and columns
#  but also index is always referring to the row numbers/names
rng = np.random.RandomState(42)
#   running random integers in a 2x2 array
dataframe=pd.DataFrame(rng.randint(0,10,(3,3)), columns=['b', 'a', 'c'],
            index=['row1', 'row2', 'row3'])
# %%
#now i can grab out a column of data by "dataframe.<column>"
dataframe.b
# %%
#can do stats with columns
np.mean(dataframe.b)
# %%
dataframe['b']
np.mean(dataframe['b'])
# %%
dataframe.values
dataframe.index
dataframe.columns

# %%
dataframe['b']
# %%
# loc lets you find rows by their names
dataframe.loc['row1']
dataframe.loc['row1','a']
#%%
# iloc lets you find rows by their numbers starting at zero and counting out integers
# 
dataframe.iloc[0]
#%%
dataframe.iloc[0, 1]
# %%
# If we hypothetically added dataframes, it'll add up the row names properly no matter the row names

dataframe2=pd.DataFrame(rng.randint(0,10,(3,3)), columns=['b', 'a', 'c'],
            index=['row3', 'row1', 'row2'])

dataframe + dataframe2
#%%
# Makes row 2 and row 4 as NaN
dataframe3=pd.DataFrame(rng.randint(0,10,(3,3)), columns=['b', 'a', 'c'],
            index=['row3', 'row1', 'row4'])

dataframe + dataframe3
#%%
# Masking values
dataframe.b(dataframe['c']>5)
# %%
# Look over the 1. training activities before trying homework
# 2. has good stuff but don't have type everything if you don't want to

# Questions - 1&2 should be one line of code answers
#              Key is to understand the index
# we're going to have to use loc and iloc, know differences
# keep in mind fundamentally what you're working with and why it's different
# %%
