import sys
import os
import pandas as pd
import numpy as np
import scipy.spatial.distance as norm
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
from sklearn.neighbors import RadiusNeighborsRegressor
from sklearn import cross_validation
from sklearn import metrics
from configuration import CONFIG
from sklearn import neighbors
from sklearn import linear_model
import scipy as sp

preprocessing = fp.feature_preprocessing()
preprocessing.full_preprocess(used_columns=CONFIG.days.values() + CONFIG.ass_assign +['TIME', 'CSPL_CALLS'])
data = preprocessing.data
Y = data['CSPL_CALLS']
X = data.drop(['CSPL_CALLS'], axis=1)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.1, random_state=0)

clf = linear_model.SGDRegressor()
clf.fit(X_train, y_train)
#error = neigh.score(X_test, y_test)

#print(error)

y_pred = clf.predict(X_test)
print(sp.spatial.distance.sqeuclidean(y_pred, y_test))
print(np.array(data.iloc[0]))