# -*- coding: utf-8 -*-
"""stockmarketforecasting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/169ZjmUslIBgoTgv8q8owT5-fq0izPIt7
"""

pip install yfinance

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import random

#setup
#code
ticker = yf.Ticker('NKE') #import data
aapl_df = ticker.history(period="5y") #get data from 5 year period in dataframe
aapl_df.drop(['High','Low','Close','Volume','Dividends','Stock Splits'], axis=1, inplace=True) #only have two columns, not seven
data = np.empty(shape = (1259), dtype = float)
data=aapl_df[['Open']].to_numpy()

X = np.zeros((1256,3))
Y = [0]*1256

print(len(data))
counter = 1
while counter < len(data) - 3:
  Y[counter] = data[counter+2]
  X[counter] = [data[counter-1], data[counter], data[counter +1]]
  counter = counter +1
print(X)
print(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)


regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)


# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
count = 0
sum = 0
misseddays = 0
for item in y_test:

  error = y_test[count]- y_pred[count]
  error = abs(error)
  if y_test[count] <1:
    errorpercent = 0
    misseddays = misseddays+1
  else:
    errorpercent = error/ y_test[count]
  sum = sum + errorpercent
  count = count+1

count = count - misseddays
print(misseddays)
averageerror = sum/count
print(averageerror)

# The coefficient of determination: 1 is perfect prediction


# Plot outputs
# plt.scatter(X_test, y_test, color="black")
# plt.plot(X_test, y_pred, color="blue", linewidth=3)

# plt.xticks(())
# plt.yticks(())

# plt.show()

neuralregr = MLPRegressor(random_state=1, max_iter=500).fit(X_train, y_train)
neuralpredict = neuralregr.predict(X_test)

count = 0
sum = 0
misseddays = 0
for item in y_test:

  error = y_test[count]- neuralpredict[count]
  error = abs(error)
  if y_test[count] <1:
    errorpercent = 0
    misseddays = misseddays+1
  else:
    errorpercent = error/ y_test[count]
  sum = sum + errorpercent
  count = count+1

count = count - misseddays
print(misseddays)
averageerror = sum/count
print(averageerror)

print("Mean squared error: %.2f" % mean_squared_error(y_test, neuralpredict))


npredictvalue = neuralregr.predict(X_test)
lpredictvalue = regr.predict(X_test)

w1 = 0.5
w2 = 0.5
newpredict = []
for x in range(0,len(npredictvalue)-1, 1):
  predictedvalue = (w1* npredictvalue[x] )+(w2 *lpredictvalue[x])
  error1 = abs(y_test[x] - npredictvalue[x])
  error2 = abs(y_test[x]- lpredictvalue[x])
  newpredict.append(predictedvalue)
  w1 = w1/(2**error1)
  w2 = w2/(2**error2)
  sum = w1+w2
  w1= w1/sum
  w2 = w2/sum

money = 10000
stocks = 0

prediction = neuralregr.predict(X)
for i in range(1,len(X),1):
  if money > Y[i-1]*2:
    if prediction[i] > Y[i-1]:
      stocks = stocks +2
      money = money - Y[i-1]
  if stocks > 2:
    if prediction[i]< Y[i-1]:
      stocks = stocks -2
      money = money + Y[i-1]
soldstocks = stocks* Y[-2]
stocks = 0
money = money + soldstocks
print("Stocks: "+ str(stocks))
print("Money: " + str(money))

## adjust the number of stocks for the accuracy rate and the amount of money you have
## analytical report for the code and bot that we did

## https://www.lumiere-education.com/post/15-journals-to-publish-your-research-in-high-school#:~:text=Journal%20of%20Research%20High%20School,but%20release%20publications%20each%20month
## make a list of confrences to submit the work to

## make a random trading bot!


money = 10000
stocks = 0

prediction = neuralregr.predict(X)
rand = random.randint(0,2)
for i in range(1,len(X),1):
  if money > Y[i-1]*2:
    if rand == 0:
      stocks = stocks +2
      money = money - Y[i-1]
  if stocks > 2:
    if rand == 1:
      stocks = stocks -2
      money = money + Y[i-1]
soldstocks = stocks* Y[-2]
stocks = 0
money = money + soldstocks
print("Stocks: "+ str(stocks))
print("Money: " + str(money))

## adjust the number of stocks for the accuracy rate and the amount of money you have
## analytical report for the code and bot that we did

## https://www.lumiere-education.com/post/15-journals-to-publish-your-research-in-high-school#:~:text=Journal%20of%20Research%20High%20School,but%20release%20publications%20each%20month
## make a list of confrences to submit the work to

## make a random trading bot!