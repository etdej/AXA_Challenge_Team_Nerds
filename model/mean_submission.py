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
preprocessing = fp.feature_preprocessing()
preprocessing.full_preprocess(used_columns=['WEEK_DAY', 'ASS_ASSIGNMENT', 'TIME', 'CSPL_CALLS'])

sub_p = sp.submission_preprocessing()
sub_p.full_preprocess(used_columns=['WEEK_DAY', 'ASS_ASSIGNMENT', 'TIME', 'CSPL_CALLS'])
submission_data = sub_p.data
print(submission_data.columns)

data = preprocessing.data


prediction = []
for i in range(submission_data.shape[0]):
    x = pd.Series(submission_data.iloc[i])
    d = data[(data['WEEK_DAY'] == x['WEEK_DAY']) & (data['ASS_ASSIGNMENT'] == x['ASS_ASSIGNMENT']) & (data['TIME'] == x['TIME'])]

    calls = d['CSPL_CALLS']
    mean = calls.mean()

    prediction.append(mean)

print(prediction)


post = postpro.submission_postprocess()
post.premier_submit(prediction)
#clf = svm.SVR(kernel='poly', degree=3)
#scores = cross_validation.cross_val_score(clf, X_train, Y_train, cv=2)
#print(scores)
