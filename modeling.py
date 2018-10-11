# Module holding all modeling-stuff

from sklearn.svm import SVR   # Support Vector Machine -> Support Vector Regression used for prediction
# could be use for regression as well


def predict_data(x, models):
    predictions = []
    for model in models:
        predictions.append(model.predict(x))
    return predictions


def fit_data(x, y):
    print('Set up models...')
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=1)  # the same as linear:p
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

    print('Fit models...')
    models = [svr_lin, svr_poly, svr_rbf]
    for model in models:
        print(str(model.kernel) + "...")
        model.fit(x, y)
    return [x, models]
