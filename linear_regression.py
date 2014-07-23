# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 12:06:56 2014

@author: Goren
"""
import numpy as np
def prediction_error(predict,test):
    return np.array([abs(diff) for diff in predict-test])    

import load_data
train = load_data.loader('train_processed').read()
test_size=886
#train set
X= train[0:-test_size,0:9]
y_c=train[0:-test_size,9]
y_r=train[0:-test_size,10]
#test set
test_X= train[-test_size:,0:9]
test_y_c=train[-test_size:,9]
test_y_r=train[-test_size:,10]

from sklearn.linear_model import LinearRegression
linreg=LinearRegression(fit_intercept=True, normalize=True)
linreg.fit(X,y_c)
print "Linear coefficients:"
print linreg.decision_function(X)

predict_y_c=linreg.predict(test_X)
error_y_c=prediction_error(predict_y_c,test_y_c)
print "Max Value: {}, Average error: {}".format (test_y_c.max(),error_y_c.mean())


import matplotlib.pyplot as plot
plot.title("Cost vs. number of iterations")
plot.plot(test_X[:,0],predict_y_c,'b')
plot.plot(test_X[:,0],test_y_c,'g')
plot.plot(test_X[:,0],error_y_c,'r')

plot.figure()
plot.title("Linear Regression")