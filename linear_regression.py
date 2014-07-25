# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 12:06:56 2014

@author: Goren
"""
import numpy as np
def prediction_error(predict,test):
    return np.array([abs(diff) for diff in predict-test])    

import load_data
loader = load_data.bikeshare_loader()
loader.preprocess()
#train set
(X,y_c)= loader.training_data(range(9),9)
(X,y_r)= loader.training_data(range(9),10)
#test set
(test_X,test_y_c)= loader.test_data(range(9),9)
(test_X,test_y_c)= loader.test_data(range(9),10)

from sklearn.linear_model import LinearRegression
linreg=LinearRegression(fit_intercept=True, normalize=True)
linreg.fit(X,y_c)
print "Linear coefficients:"
print linreg.decision_function(X)

predict_y_c=linreg.predict(test_X)
error_y_c=prediction_error(predict_y_c,test_y_c)
print "Max Value: {}, Average error: {}".format (test_y_c.max(),error_y_c.mean())


import matplotlib.pyplot as plt
plt.figure()
plt.title("Linear Regression")
plt.plot(test_X[:,0],predict_y_c,'b')
plt.plot(test_X[:,0],test_y_c,'g')
plt.plot(test_X[:,0],error_y_c,'r')