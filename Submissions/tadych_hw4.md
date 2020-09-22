# **HAS Tools - Homework 4**

### *Danielle Tadych -  9/21/2020*

___
### Grade
3/3 - nice job, I like your reasoning for your forecast. Next time include the plots in your  markdown.
___

**Forecast Prediction Summary:**
Since it's a really dry year I searched for years in which flows in september were below 60.  Those were 2002, 2004, 2011, 2019, and then of course this year.  I then got summary stats for all of the dry years, include quantile analyses.  For my 1 week prediction, I went with the 50% quantile (53.3cfs) for 2020, and then for the 2 week out prediction I was more optimistic and went with the higher 2019 50% quantile (61.1cfs). For the seasonal forecast, I took a slightly different approach just to change things up.  I plotted monthly 2019 histograms for each of the remaining months, and went with approximately the most common flow value for that month.


**Questions:**
1. Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.

***After finding that the driest years, I conducted a quantile analysis on each of the years, setting the flow limit to 200.  I also plotted flow histograms in September for all years and dry years together and individual dry years.  In the end, since 2019 is eerily similar to 2020, I went with the 50% (most common) quantile for my 2-week prediction and 2020 50% quantile for 1 week. For the other seasonal forecast, I simply plotted histograms and went with roughly the most common flow value for each month in 2019.***

2. Describe the variable flow_data:
  - What is it?  ***It is a numpy data array***

  - What type of values is is composed of?
     ***float***
  - What is are its dimensions, and total size? ***4 cols x 11,585 rows***

3. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?

***Percent exceeded prediction: 97.26 %***


4. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)

***Percent exceeded prediction before 2000: 56.02 % \
Percent exceeded prediction after 2010: 94.46 %***

5. How does the daily flow generally change from the first half of September to the second?

*Although the first half of September generally has higher average flows, the second half has more variability and also has higher maximum flow.*

***First half:***\
max: 1280.0 \
min: 36.6\
mean: 178.0727083333333\
median: 134.5\
quantile: [ 36.6   60.96 134.5  303.  ]

***Second half:***\
max: 5590.0\
min: 51.2\
mean: 168.88400852878465\
median: 111.0\
quantile: [ 51.2   77.98 111.   238.  ]
