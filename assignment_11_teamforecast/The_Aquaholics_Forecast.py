# Team Forecast: The Aquaholics
# Members: Diana, Danielle, Xenia and Camilo
# November 2020

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import os
import json
import urllib.request as req
import urllib
from sklearn.linear_model import LinearRegression
from matplotlib.dates import DateFormatter

# %% Functions
""" Estimate the parameters of an Auto Regressive Model (AR)

Parameters:
----------
df: Dataframe containing the flow information.
initial_date: Initial date for the training period in format 'YYYY-MM-DD'.
final_date: Final date for the training period in format 'YYYY-MM-DD'.
time_shifts: Number of time shifts to consider in the AR model.

Returns:
---------
model_intercept: The intercept of the AR Model
model_coefficients: The coefficients of the AR Model (size=[time_shifts,1])
r_sq: Determination Coefficient R2 of the AR Model
"""


def AR_model_estimate(df, initial_train_date, final_train_date, time_shifts):

    # Define the type of model to use
    model_LR = LinearRegression()

    # Start the shift listing with the string 'Flow'
    shift_list = ['flow']

    # Create additional columns to the dataframe to include desired time \
    # shifts
    for i in range(1, time_shifts+1):
        num_shift = 'flow_tm'+str(i)
        df[num_shift] = df['flow'].shift(i)
        shift_list.append(num_shift)

    # Create a dataframe of training data including all columns of df
    train_data = df[initial_train_date:final_train_date][shift_list]

    # Create the dependent array for the AR model
    y_data = train_data['flow']

    # Create the set of independent variables for the AR Model.
    x_data = train_data[shift_list[1:len(shift_list)]]

    # Fit the corresponding AR Model
    model_LR.fit(x_data, y_data)

    # Save the results of the AR Model
    r_sq = np.round(model_LR.score(x_data, y_data), 4)
    model_intercept = np.round(model_LR.intercept_, 2)
    model_coefficients = np.round(model_LR.coef_, 2)

    # Print the results to the user
    print('AR Model with ', time_shifts, ' shifts')
    print('coefficient of determination:', r_sq)
    print('intercept:', model_intercept)
    print('slope:', model_coefficients)

    return model_intercept, model_coefficients, r_sq


""" Forecast the flows for a given number of periods based on flow timeseries

Parameters:
-----------
flow_daily: Dataframe containing the daily flow information. The index of \
        the df should be the date and this df should only include 'flow'.
time_shifts: Number of time shifts to consider in the AR Model
start_train_date: Initial date for the training period in format 'YYYY-MM-DD'.
end_train_date: Final date for the training period in format 'YYYY-MM-DD'.
start_for_date: Initial date for the forecast in format 'YYYY-MM-DD'.
end_for_date: Final date for the forecast in format 'YYYY-MM-DD'.
seasonal: Binary condition telling the scale of time of the forecast.

Returns:
-----------
flow_daily: Dataframe with the forecasts in a daily basis
flow_weekly: Dataframe with the forecasts in a weekly basis
model_intercept: Intercept from the AR Model
model_coefficients: List of coefficients from the AR Model
"""


def forecast_flows(flow_daily, time_shifts, start_train_date, end_train_date,
                   start_for_date, end_for_date, seasonal):

    # Get the location (index) for the day before the start forecasting \
    # date in the original dataframe (data)

    temp_data = flow_daily
    temp_data = temp_data.reset_index()
    temp_data['datetime'] = flow_daily.index  # .strftime('%Y-%m-%d')

    if seasonal == 'week':
        date_before_start = (pd.to_datetime(start_for_date) +
                             dt.timedelta(days=-1)).date()
        index_lag1 = temp_data.loc[temp_data.datetime == str(
            date_before_start)].index[0]
    elif seasonal == 'seasonal':
        flow_daily = flow_daily.resample("W-SUN", closed='left', label='left')\
            .mean()
        index_lag1 = flow_daily.shape[0]-1
        print(index_lag1)
    else:
        print('Please choose a valid time horizon for forecast')

    # Create a list of dates (daily) for the forecast period
    if seasonal == 'week':
        forecast_period = pd.date_range(start=start_for_date,
                                        end=end_for_date, freq='D')
    elif seasonal == 'seasonal':
        forecast_period = pd.date_range(start=start_for_date,
                                        end=end_for_date, freq='W')

    # Estimate the parameters for the best-fit AR Model
    model_intercept, model_coefficients, r_sq = AR_model_estimate(
        flow_daily, start_train_date, end_train_date, time_shifts)

    # Calculate the Forecasts for the indicated time range based on the \
    # selected timeshifts.
    # "lag_i" is used to extract the flow value based on the order of the \
    # AR Model using the index located for the day before the start of \
    # forecast.
    lag_i = index_lag1+1

    # Using a nested conditional, the forecasts are calculated between \
    # the desired range of dates, and then appended to the dataframe

    if time_shifts == 1:
        for i in range(0, forecast_period.shape[0]):
            forecast_val = model_intercept + model_coefficients[0] * \
                flow_daily.iloc[lag_i - 1]['flow']
            lag_i += 1  # Update the counter
            flow_daily.loc[forecast_period[i], ['flow']] = forecast_val
    elif time_shifts == 2:
        for i in range(0, forecast_period.shape[0]):
            forecast_val = model_intercept + model_coefficients[0] * \
                flow_daily.iloc[lag_i - 1]['flow'] + \
                model_coefficients[1] * \
                flow_daily.iloc[lag_i - 2]['flow']
            lag_i += 1  # Update the counter
            flow_daily.loc[forecast_period[i], ['flow']] = forecast_val
    elif time_shifts == 3:
        for i in range(0, forecast_period.shape[0]):
            forecast_val = model_intercept + model_coefficients[0] * \
                flow_daily.iloc[lag_i - 1]['flow'] + \
                model_coefficients[1] * \
                flow_daily.iloc[lag_i - 2]['flow'] + \
                model_coefficients[2] * \
                flow_daily.iloc[lag_i - 3]['flow']
            lag_i += 1  # Update the counter
            flow_daily.loc[forecast_period[i], ['flow']] = forecast_val
    elif time_shifts == 4:
        for i in range(0, forecast_period.shape[0]):
            forecast_val = model_intercept + model_coefficients[0] * \
                flow_daily.iloc[lag_i - 1]['flow'] + \
                model_coefficients[1] * \
                flow_daily.iloc[lag_i - 2]['flow'] + \
                model_coefficients[2] * \
                flow_daily.iloc[lag_i - 3]['flow'] + \
                model_coefficients[3] * \
                flow_daily.iloc[lag_i - 4]['flow']
            lag_i += 1  # Update the counter
            flow_daily.loc[forecast_period[i], ['flow']] = forecast_val
    else:
        print('Please modify the code to include more time shifts')

    # Resampling the forecast in a weekly basis, starting on Sundays and \
    # setting the labels and closed interval at the left
    if seasonal == 'week':
        flow_weekly = flow_daily.loc[start_for_date:end_for_date][['flow']].\
            resample("W-SUN", closed='left', label='left').mean()
    elif seasonal == 'seasonal':
        flow_weekly = flow_daily.loc[start_for_date:end_for_date][['flow']]

    # Print the forecasts for the competition
    for i in range(flow_weekly.shape[0]):
        print('\n Week #', str(i+1), '-', flow_weekly.iloc[i].name, '(cfs): ',
              np.round(flow_weekly.iloc[i]['flow'], 2))

    return flow_daily, flow_weekly, model_intercept, model_coefficients

# %%

# Data retrieval of streamflows from USGS


# URL Variables
site = '09506000'
start = '2009-03-02'  # Adjusted according to information availability
end = '2020-11-04'
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
      "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end

stream_data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                                     'datetime', 'flow', 'code'],
                            parse_dates=['datetime'], index_col='datetime')

stream_data.index = stream_data.index.strftime('%Y-%m-%d')
stream_data = stream_data.set_index(pd.to_datetime(stream_data.index))


# %%
# Forecasts for Week 10

# Common dataframe for both forecasts including only the flow column
daily_flow = stream_data[['flow']]
daily_flow = daily_flow.set_index(pd.to_datetime(stream_data.index))

# Two-week forecast

# Training period for the AR Model
start_train_date = '2009-10-01'
end_train_date = '2009-11-30'

# Forecasting period
start_for_date = '2020-11-01'
end_for_date = '2020-11-14'

# Used parameters for the model
# Number of shifts
time_shifts = 3

# Function Call
flow_daily_2w, flow_weekly_2w, model_intercept, model_coefficients = \
    forecast_flows(daily_flow, time_shifts, start_train_date,
                   end_train_date, start_for_date, end_for_date, 'week')

# %%
# Seasonal Forecast for weeks between Aug. 22 to Oct. 31

# Training period for the AR Model for first 6 weeks
start_train_date = '2019-08-25'
end_train_date = '2019-11-10'

# Forecasting period for first 6 weeks
start_for_date = '2020-08-22'
end_for_date = '2020-10-31'

# Number of shifts
time_shifts = 3

# Common dataframe for both forecasts including only the flow column
daily_flow_16w = stream_data.loc['1989-01-01':start_for_date][['flow']]

# Function Call
flow_daily_seas, flow_weekly_seas, model_intercept16, model_coefficients16 = \
    forecast_flows(daily_flow_16w, time_shifts, start_train_date,
                   end_train_date, start_for_date, end_for_date, 'seasonal')

# %%
# Seasonal Forecast for weeks between Nov. 01 to Dec. 12
# NOTE: I did not use the outputs printed by the model to make the forecasts.\
# Rather, I used the model determined by the function.

# Training period for the AR Model for first 6 weeks
start_train_date = '2009-10-01'
end_train_date = '2009-11-30'

# Forecasting period for first 6 weeks
start_for_date = '2020-11-01'
end_for_date = '2020-12-12'

# Number of shifts
time_shifts = 3

# Common dataframe for both forecasts including only the flow column
daily_flow_16w = stream_data.loc['1989-01-01':start_for_date][['flow']]

# Function Call
flow_daily_seas, flow_weekly_seas, model_intercept16, model_coefficients16 = \
    forecast_flows(daily_flow_16w, time_shifts, start_train_date,
                   end_train_date, start_for_date, end_for_date, 'seasonal')

# %%
