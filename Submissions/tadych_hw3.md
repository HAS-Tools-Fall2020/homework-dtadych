## Danielle Tadych  - 9/14/2020 - Homework 3

Summary:
  First I downloaded new data up to Saturday.  For the week 1 forecast, I created an empty list that I wanted to put historical week 1 values in. Then I used a for loop to  pull out flow values in September with week 1 days and append them into my week 1 forecast list.  Then I printed some statistics regarding week 1 historical data.  Since it's a very dry year I went with the minimum.  I followed the same methodology with the other forecasts.  For the seasonal forecast, I just changed the days


Homework Questions:
1. Describe the variables `flow`, `year`, `month`, and `day`. What type of objects are they, what are they composed of, and how long are they?
  All are lists.  Flow is average daily flow (cms) and the others are date integers
2. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
  99.9%
3. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
  Since I went with minimum values for, all, it's still 99.9% for both parameters
4. How does the daily flow generally change from the first half of September to the second?
  The Second half of September has more variation but a lower average flow compared to the first half.  Also, the maximum flow value is about 4x higher in the second half of September compared to the first

    First half statistics:
      Min: 48.6
      Max: 1280.0
      Avg: 182.
      Stdev: 172.
    Second half statistics
      length: 465
      Min: 51.2
      Max: 5590.0
      Avg: 169.
      Stdev: 371.
