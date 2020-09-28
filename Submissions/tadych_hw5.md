# **HAS Tools - Homework 5**

### *Danielle Tadych -  9/28/2020*

**Forecast Prediction Summary:**
Was not very fancy here.  I used almost the same logic as before regarding comparing to 2019 (super dry year) but this time I made monthly plots for the semester months (Sep-Dec).  For my one and 2 weekly forecast, I made a plot of September 2019 and 2020 flow values (Figure 1). Since 2020 is much dryer right now with no rain in sight I predicted ~60cms.  I then gradually added October, November, and December months to my plot and made predictions visually based on week.

*note*: will make much prettier graphs next time

![](/Users/danielletadych/Documents/FALL2020/Coding/homework-dtadych/assignment_5/sepflow20192020.png)
**Figure 1.** Rough graph of 2019 and 2020 Flow values in september, with day of the month on the x-axis and flow on the y-axis. Orange is 2019 and blue is 2020.  

**Questions:**

1. Provide a summary of the data frames properties.
 - What are the column names? **datetime,flow, code, year, month, day**
 - What is its index? **The row index is a range of values beginning at [0]**
 - What data types do each of the columns have? **Objects**
2. Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.
 | Stats | Flow (cms) |
 | ----------- | ----------- |
 | Count  | 11,592 |
 | mean | 345|
 | std | 1410 |
 |min|19.0|
 |max|63,400|
 |*Quartiles:*|
 |25%|93.7|
 |50%|158.0|
 |75%|216.0|

3. Provide the same information but on a monthly basis. (Note: you should be able to do this with one or two lines of code)

![Flow Stats by Month](/Users/danielletadych/Documents/FALL2020/Coding/homework-dtadych/assignment_5/flowmonthstats.png)

4. Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values in your summary.
:
**Highest:**

|Date|Month|Flow (cms)|
| --- |---|---|
|1993-01-08|1|63400|
|1993-02-20|2|61000|
|1995-02-15|2|45500|
|2005-02-12|2|35600|
|1995-03-06|3|30500|

**Lowest:**

|Date|Month|Flow (cms)|
| --- |---|---|
|2012-06-29|6|22.5|
|2012-06-30|6|22.1|
|2012-07-01|7|19|
|2012-07-02|7|20.1|
|2012-07-03|7|23.4|


5. Find the highest and lowest flow values for every month of the year (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.

|month|max|min|max year|min year|
|---|---|---|---|---|
|1|63400|158|1993|2003
|2|62000|136|1993|1991
|3|30500|97|1995|1989
|4|49600|64.9|1991|2018
|5|546|46.0|1992|2004
|6|481|22.1|1992|2012
|7|1040|19.0|2006|2012
|8|5360|29.6|1992|2019
|9|5590|36.6|2004|2020
|10|1910|69.9|2010|2012
|11|4600|117|2004|2016
|12|28700|155|2004|2012


6. Provide a list of historical dates with flows that are within 10% of your week 1 forecast value. If there are none than increase the %10 window until you have at least one other value and report the date and the new window you used

**I could not figure out how to put the list in here but it is in my python script line 168.  It has 588 values with the following range
152      1989-06-02
153      1989-06-03
160      1989-06-10
162      1989-06-12
163      1989-06-13
            ...    
11587    2020-09-22
11588    2020-09-23
11589    2020-09-24
11590    2020-09-25
11591    2020-09-26**

Prediction: 60cms
