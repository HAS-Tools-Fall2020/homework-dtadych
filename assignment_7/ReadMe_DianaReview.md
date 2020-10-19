## Code Review Readme
Danielle Tadych, 10/9/2020

*note*:
The instructions sound super sassy but I swear to God it should hopefully run well and be that simple.  If not, then I give up

___

**Instructions to run forecast:**
1. Click "Run Below" above the # %% on line 11
2. Scroll down to the bottom to view the output
3. Enter the labelled forecast numbers in the table below
4. Enter the Actual Numbers in the forecast excel sheet "tadych.csv"


|Forecast Type|Week 1| Week 2|
|---|---|---|
|Auto-regression| 161.24 | 218.9 |
|Actual Submission| 59.54| 61.64|

___

**Code Review**

Overall, I thought the code was very good. Easy to understand what you were trying to do and it was written well. Here are some ideas/suggestions to improve the code.

1) Doc-strings! Add them to your functions to tell people what it is the function is trying to do.

2) I suggest renaming "datum" in your functions to "data_set" to make it clear it is a set of data rather than a specific value.

3) I had to add a "../" to find the streamflow file. When Laura reviews this make sure there is a data folder in where your code is, or else give her instructions on how to find the streamflow file.

4) I think there is probably an easier way to index your flow_weeklytest data (lines 85-87). That said... I am not sure how to do this. I tried to google but it failed me. Pandas normally indexes for us but I think because we did a For Loop it just left them out? I did however learn the new functions .pop and .cumsum, which was cool.

5) Line 132, I think an improvement would be to use the "tail" function, rather than specifying the row with which you are trying to use as "lastweekflowtest". This could be accomplished by making a new variable = observedweeklyflow.tail(2). Then you could use iloc[0] to pick out last weeks flow. Then the code is reusable even when we get a new weeks worth of data.

6) If you wanted I think you could beef up the comment on Line 91, as is it doesn't really tell us that much. Also, there is extra space on line 83.


| Criteria|Points (max 3)|Written Assessment|
|---|---|---|
|Readability|1| Had to give you a 1 since they were missing. Thought most of your variables were really well named though!|
|Style|3|Not a single PEP8 error. Flawless. Also just pretty editing in general|
|Code Awesome|3|Thought it was a really nice code!|
|---|---|---|
|*Total Score*|7| :)|
