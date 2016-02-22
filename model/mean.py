import sys
import os
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
from sklearn import svm
from sklearn import cross_validation
from sklearn import metrics

preprocessing = fp.feature_preprocessing()
preprocessing.full_preprocess()

data = preprocessing.data
Y = data['CSPL_CALLS']
X = data.drop(['CSPL_CALLS'], axis=1)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.4, random_state=0)
clf = svm.SVR(kernel='rbf', C=1e3, gamma=0.1)

clf.fit(X_train, y_train)

y_predict = clf.predict(X_test)
print(y_predict - y_test)
print(clf.score(X_test, y_test))

#clf = svm.SVR(kernel='poly', degree=3)
#scores = cross_validation.cross_val_score(clf, X_train, Y_train, cv=2)
#print(scores)
