import sys
import os
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
import submission_preprocessing as sp
import submission_postprocess as postpro
from sklearn import svm
from sklearn import cross_validation
from sklearn import metrics
from configuration import CONFIG
import pandas as pd
import time

t1 = time.time()

print('preprocessing...')
preprocessing = fp.feature_preprocessing()
preprocessing.full_preprocess(used_columns=['WEEK_DAY', 'YEAR', 'YEAR_DAY', 'ASS_ID', 'TIME', 'CSPL_CALLS'])

sub_p = sp.submission_preprocessing()
sub_p.full_preprocess(used_columns=['WEEK_DAY', 'YEAR', 'YEAR_DAY', 'ASS_ID', 'TIME', 'CSPL_CALLS'])
submission_data = sub_p.data
print(submission_data.columns)

data = preprocessing.data


prediction = []

print('data loaded, beginning prediction...')

for i in range(submission_data.shape[0]):
    x = pd.Series(submission_data.iloc[i])
    xwd = x['WEEK_DAY']
    xa = x['ASS_ID']
    xt = x['TIME']
    yd = x['YEAR_DAY']
    xy = x['YEAR']
    #if xa == 35:
    d = data.query('WEEK_DAY == @xwd and ASS_ID ==@xa and TIME == @xt and YEAR == @xy')
    #else:
    #    d = data.query('WEEK_DAY == @xwd and ASS_ID ==@xa and TIME == @xt')

    calls = d['CSPL_CALLS']
    if calls.empty:
        prediction.append(0)
    else:
        mean = calls.mean()
        prediction.append(mean)

    if i%1000 == 0:
        print(i)
print(prediction)


post = postpro.submission_postprocess()
post.premier_submit(prediction, name = "result_submission_axa3.txt")

t2 = time.time()

print(t2 - t1)
#clf = svm.SVR(kernel='poly', degree=3)
#scores = cross_validation.cross_val_score(clf, X_train, Y_train, cv=2)
#print(scores)
