## HAS Tools - Homework 12

#### *Danielle Tadych -  11/16/2020*
___
### Grade

___

**Forecast Prediction Summary:**

For my actual one and two week forecast, I took the average of November 2020 flows and used this as my week 1 prediction.  Then for week 2 prediction, I added the standard deviation to the mean.  For my seasonal forecast I decided to just stick with last week's team prediction.

---

**Added Dataset Summary:**

I chose NCAR NCEP runoff dataset because I suspect this is why we are getting higher flows despite almost no precipitation.  I chose the suggested bounding box for my area and I also requested a greater time frame because I wanted to see historical runoff over the semester.  This somehow resulted in me downloading 35K .nc files.  Due to me being eaten by exams, I have not had time to attempt aggregating the dataset and getting anything useful from it, but my plan was to use the starter code, create a new environment since I found conflicts with other packages, and try to pick 1 .nc file to dig into understand it better.  Then I was going to aggregate the .nc files by watershed and create an average runoff time series.  This is what I will do this afternoon if I can get it running and will add any resulting graph to the slide deck.

**More detailed information about the dataset:**
The NCEP operational Global Forecast System analysis and forecast grids are on a 0.25 by 0.25 global latitude longitude grid. Grids include analysis and forecast time steps at a 3 hourly interval from 0 to 240, and a 12 hourly interval from 240 to 384. Model forecast runs occur at 00, 06, 12, and 18 UTC daily

**Temporal Range:** 2015-01-15 00:00 +0000 to 2020-11-29 18:00 +0000

**Requested Range:** 2020-08-16 to 2020-11-30
