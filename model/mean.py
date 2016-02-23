import sys
import os
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
from sklearn import svm
from sklearn import cross_validation
from sklearn import metrics
from configuration import CONFIG
import pandas as pd
preprocessing = fp.feature_preprocessing()
preprocessing.full_preprocess(used_columns=['WEEK_DAY', 'ASS_ASSIGNMENT', 'TIME', 'CSPL_CALLS'])

data = preprocessing.data
Y = data['CSPL_CALLS']
X = data

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.3, random_state=0)

score = 0

for i in range(X_train.shape[0]):
    x = pd.Series(X_train.iloc[i])
    d = X_train[(X_train['WEEK_DAY'] == x['WEEK_DAY']) & (X_train['ASS_ASSIGNMENT'] == x['ASS_ASSIGNMENT']) & (X_train['TIME'] == x['TIME'])]

    calls = d['CSPL_CALLS']
    mean = calls.mean()


    dif = (x['CSPL_CALLS']/mean - 1)**2
    print(dif)
    score += dif
    if i%1000 == 0:
        print score/i


score = score/X_train.shape[0]
print(score)


#clf = svm.SVR(kernel='poly', degree=3)
#scores = cross_validation.cross_val_score(clf, X_train, Y_train, cv=2)
#print(scores)
