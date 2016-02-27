import sys
import os
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
from sklearn import svm
from sklearn import cross_validation
from sklearn import metrics
from configuration import CONFIG
import pandas as pd
import numpy as np
import numexpr
import time

t1= time.time()
preprocessing = fp.feature_preprocessing()
preprocessing.full_preprocess(used_columns=['DATE', 'WEEK_DAY', 'YEAR_DAY', 'ASS_ASSIGNMENT', 'ASS_ID', 'TIME', 'CSPL_RECEIVED_CALLS'])

data = preprocessing.data
Y = data['CSPL_RECEIVED_CALLS']
X = data

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.005, random_state=0)
t3 = time.time() - t1
print('data_preprocessing :'+str(t3))

score = 0
overtel = 0
over = 0
over_techaxa = 0
total_tel = 0
total_techaxa = 0

for i in range(X_test.shape[0]):
    x = pd.Series(X_train.iloc[i])
    xwd = x['WEEK_DAY']
    xa = x['ASS_ID']
    xt = x['TIME']
    yd = x['YEAR_DAY']
    d = X_train.query('WEEK_DAY == @xwd and ASS_ID ==@xa and TIME == @xt and abs(YEAR_DAY - @yd) < 30')

    calls = d['CSPL_RECEIVED_CALLS']
    mean = calls.mean()

    if x['ASS_ID'] == 35:
        total_tel +=1
    if x['ASS_ID'] == 29:
        total_techaxa +=1

    dif = (x['CSPL_RECEIVED_CALLS']-mean)**2
    if dif > 500:
        if x['ASS_ID'] == 35:
            overtel +=1
        if x['ASS_ID'] == 29:
            over_techaxa +=1
        over +=1
        #rint(mean)
        #print(calls.shape)
        #print()
    score += dif
    if i%1000 == 0:
        print score/i


score = score/X_train.shape[0]
print(score)
print(float(over_techaxa)/over)
print(float(total_techaxa)/X_test.shape[0])
print(float(overtel)/over)
print(float(total_tel)/X_test.shape[0])

t2 = time.time()

print(t2-t1)

#clf = svm.SVR(kernel='poly', degree=3)
#scores = cross_validation.cross_val_score(clf, X_train, Y_train, cv=2)
#print(scores)
