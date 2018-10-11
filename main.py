# Predict stock prizes of a couple of companies based on its history
# (so it is kind of approximation)

import quandl
import numpy as np
import datetime

import modeling
import plotting


def data_to_date(data):
    dates = []
    for value in data:
        dates.append(str(value)[:(str(value).rfind('-') + 3)])
    return dates


print("Let's play!")
start_date = "2010-01-01"
today = str(datetime.date.today())

print('Acquire data...')
data_list = []
dates_list = []

xxx = quandl.get("xxx", start_date=start_date, end_date=today, collapse="monthly", returns="pandas")
data_list.append(xxx['Open'])
dates_list.append(data_to_date(xxx.reset_index()['Date']))

yyy = quandl.get("yyy", start_date=start_date, end_date=today, collapse="monthly",
                         returns="pandas")
data_list.append(yyy['local_price'])
dates_list.append(data_to_date(yyy.reset_index()['Date']))

for data, dates in zip(data_list, dates_list):
    print('Fit data...')
    x, models = modeling.fit_data(np.reshape(np.arange(0, len(data.values)), (len(data.values), 1)), data.values)

    print('Predict data...')
    predictions = modeling.predict_data(x, models)

    print('Plot data...')

    plotting.plot_data(dates, data.values, predictions, models)

    print('Done for set of data for one company')

print('All actions done!')
