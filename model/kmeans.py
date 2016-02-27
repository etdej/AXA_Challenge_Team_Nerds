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



def mydist(x, y):
    distance_assignement = (0. if x[0]==y[0] else 1.)
    distance_time = (0. if x[2]==y[2] else 1.)
    distance_day = (0. if x[1]==y[1] else 1.)
    #distance_week_day = (1 if x[0]==y[0] else 0)
    #distance_time = abs(x[3] - y[3])%1440

    distance = distance_assignement + distance_time + distance_day
    return distance

#dist = neighbors.DistanceMetric.get_metric('pyfunc', func=distance)

preprocessing = fp.feature_preprocessing()
preprocessing.full_preprocess(used_columns=['ASS_ID', 'WEEK_DAY', 'TIME', 'CSPL_RECEIVED_CALLS'])
data = preprocessing.data[:1000]
Y = data['CSPL_RECEIVED_CALLS']
X = data.drop(['CSPL_RECEIVED_CALLS'], axis=1)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.1, random_state=0)

neigh = RadiusNeighborsRegressor(radius=0.5, metric='pyfunc', func=mydist, algorithm='auto')
print('fitting...')
neigh.fit(X_train, y_train)
print('fitted')
#error = neigh.score(X_test, y_test)

#print(error)

y_pred = neigh.predict(X_test, verbose=True)

print(np.spatial.distance.sqeuclidean(y_pred, y_test))
print(np.array(data.iloc[0]))