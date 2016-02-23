import sys
import os
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
import submission_preprocessing as sp
from sklearn import cross_validation
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn import linear_model

data_preprocessing = fp.feature_preprocessing()
data_preprocessing.full_preprocess()

data = data_preprocessing.data
Y = data['CSPL_CALLS']
X= data.drop(['CSPL_CALLS'], axis=1)

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.4, random_state=0)

clf = RandomForestRegressor(n_estimators=1000, oob_score=True)
clf.fit(X_train,Y_train)
scores = cross_val_score(clf, X ,Y)

predict = clf.predict(X_test)


print(scores.mean())
