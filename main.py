# Predict stock prizes of a couple of companies based on its history
# (so it is kind of approximation)

import quandl
import numpy as np
import datetime

import modeling
import plotting



print("Let's play!")
start_date = "2010-01-01"
today = str(datetime.date.today())

print('Acquire data...')
xxx = quandl.get("xxx", start_date=start_date, end_date=today, collapse="monthly", returns="pandas")
data = xxx['Open']

print('Fit data...')
x, models = modeling.fit_data(np.reshape(np.arange(0, len(data.values)), (len(data.values), 1)), data.values)

print('Predict data...')
predictions = modeling.predict_data(x, models)

print('Plot data...')
dates = []
date_mod = data.reset_index()['Date']
for value in date_mod:
    dates.append(str(value)[:10])

plotting.plot_data(dates, data.values, predictions, models)

print('Done!')

