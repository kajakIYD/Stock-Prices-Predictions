# Predict stock prizes of a couple of companies based on its history
# (so it is kind of approximation)

import quandl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR   # Support Vector Machine -> Support Vector Regression used for prediction
# could be use for regression as well
import datetime


def fit_data(x, y):
    print('Set up models...')
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=1) # the same as linear:p
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

    print('Fit models...')
    models = [svr_lin, svr_poly, svr_rbf]
    for model in models:
        print(str(model.kernel) + "...")
        model.fit(x, y)

    return [x, models]


def predict_data(x, models):
    predictions = []
    for model in models:
        predictions.append(model.predict(x))
    return predictions


def plot_data(x, reference, predictions, models):
    plt.scatter(x, reference, s=1, marker=',', color='black', label='Reference Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Approximation/prediction model comparison')

    for model, prediction in zip(models, predictions):
        plt.plot(x, prediction, label=str(model.kernel))

    labels = x[:10]
    plt.xticks(range(0, len(x), 10), labels, rotation='vertical')
    tmp = range(0, len(x), 10)

    plt.legend()
    plt.show()


print("Let's play!")
start_date = "2010-01-01"
today = str(datetime.date.today())

print('Acquire data...')
xxx = quandl.get("xxx", start_date=start_date, end_date=today, collapse="monthly", returns="pandas")
data = xxx['Open']

print('Fit data...')
x, models = fit_data(np.reshape(np.arange(0, len(data.values)), (len(data.values), 1)), data.values)

print('Predict data...')
predictions = predict_data(x, models)

print('Plot data...')
dates = []
date_mod = data.reset_index()['Date']
for value in date_mod:
    dates.append(str(value)[:10])

plot_data(dates, data.values, predictions, models)

print('Done!')

