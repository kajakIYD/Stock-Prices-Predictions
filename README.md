# Stock-Prices-Predictions
Prediction of stock prices based on couple of approximators. So far these are SVR (like SVM, but for regression tasks - Support Vector Regression):
- SVR linear kernel
- SVR sigmoid kernel
- SVR poly kernel (for now with degree=1)
- SVR rbf kernel
<br>
All models are regularized.
Naturally, much more regression models are available. For instance: linear regression, softmax regression, logistic regression...

Company 1:
<br>
![Pic1](https://github.com/kajakIYD/Stock-Prices-Predictions/blob/master/Pic1.PNG)

Company 2:
<br>
![Pic2](https://github.com/kajakIYD/Stock-Prices-Predictions/blob/master/Pic2.PNG)

It seems, that sigmoid kernel is not a good choice to make predictions. So let's see how the predictions look like without using  this kind of kernel:

Company 1:
![Company1WithoutSigmoid](https://github.com/kajakIYD/Stock-Prices-Predictions/blob/master/Company1WithoutSigmoid.PNG)

Company 2:
![Company2WithoutSigmoid](https://github.com/kajakIYD/Stock-Prices-Predictions/blob/master/Company2WithoutSigmoid.PNG)

Much better, but not perfect. What is also remarkable, linear kernel is useless for this task, so it will be removed. Now I would like to introduce poly kernel, but with higher degree (for example 10) and more strict regularization.

...
