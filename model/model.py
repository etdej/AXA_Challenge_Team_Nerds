import sys
import os
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
import submission_preprocessing as sp
from sklearn import cross_validation
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
import pandas as pd
from sklearn import linear_model

data_preprocessing = fp.feature_preprocessing()
data_preprocessing.full_preprocess()



data = data_preprocessing.data
Y = data['CSPL_CALLS']
X= data.drop(['CSPL_CALLS'], axis=1)
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.4, random_state=0)
#RandomForest


clf = RandomForestRegressor(n_estimators=1000, oob_score=True)
clf.fit(X_train,Y_train)
print(clf.score(X_test,Y_test))
scores = cross_val_score(clf, X ,Y)

predict = clf.predict(X_test)

result = predict-Y_test



#AdaboostRegression

clf2 = AdaBoostRegressor(n_estimators=100)
clf2.fit(X_train,Y_train)
predict_2 = clf2.predict(X_test)
print(clf2.score(X_test,Y_test))

