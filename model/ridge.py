import sys
import os
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import metrics
import numpy as np

preprocessing = fp.feature_preprocessing()
preprocessing.full_preprocess()

data = preprocessing.data
Y = data['CSPL_CALLS']
X = data.drop(['CSPL_CALLS'], axis=1)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.4, random_state=0)

print X_train
clf = linear_model.Ridge (alpha = .5)
clf.fit(X_train, y_train)

clf.fit(X_train, y_train)

y_predict = clf.predict(X_test)
print(y_predict)
print(clf.score(X_test, y_test))