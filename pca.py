# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 20:39:10 2014

@author: Goren
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model, decomposition
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
import load_data

logistic = linear_model.LogisticRegression()

#read data from csv
loader = load_data.train_loader('train_processed')
(X,y)=loader.training_data(range(1,9),9)

loader.scale(range(9))
###############################################################################

pca = decomposition.PCA(n_components=2)
# Plot the PCA spectrum
pca.fit(X)

plt.figure(1, figsize=(4, 3))
plt.clf()
plt.axes([.2, .2, .7, .7])
plt.plot(pca.explained_variance_, linewidth=2)
plt.axis('tight')
plt.xlabel('n_components')
plt.ylabel('explained_variance_')

################################################################################
#pipe = Pipeline(steps=[('pca', pca), ('logistic', logistic)])
## Prediction
#
#n_components = [20, 40, 64]
#Cs = np.logspace(-4, 4, 3)
#
##Parameters of pipelines can be set using ‘__’ separated parameter names:
#
#estimator = GridSearchCV(pipe,
#                         dict(pca__n_components=n_components,
#                              logistic__C=Cs))
#estimator.fit(X, y)
#
#plt.axvline(estimator.best_estimator_.named_steps['pca'].n_components,
#            linestyle=':', label='n_components chosen')
#plt.legend(prop=dict(size=12))
#plt.show()