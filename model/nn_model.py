import numpy as np
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from sklearn.metrics import mean_squared_error as MSE


import sys
import os
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
import submission_preprocessing as sp
import submission_postprocess as pp
from math import sqrt

output_predictions_file = 'predictions.txt'

preprocessing = fp.feature_preprocessing()
preprocessing.full_preprocess()
print(len(preprocessing.data.columns))
train = np.asarray(preprocessing.data)
x_train = train[:,0:-1]
y_train = train[:,-1]
y_train = y_train.reshape( -1, 1 )
input_size = x_train.shape[1]
target_size = y_train.shape[1]
hidden_size = 100
epochs = 7200

ds = SDS(input_size,target_size)

ds = SDS( input_size, target_size )
ds.setField( 'input', x_train )
ds.setField( 'target', y_train )

net = buildNetwork( input_size, hidden_size, target_size, bias = True )
trainer = BackpropTrainer( net,ds )

print "training for {} epochs...".format( epochs )

for i in range( epochs ):
	mse = trainer.train()
	rmse = sqrt( mse )
	print "training RMSE, epoch {}: {}".format( i + 1, rmse )

submission = sp.submission_preprocessing()
submission.full_preprocess()
data_to_predict = np.asarray(submission.data)
x_used_for_prediction = data_to_predict[:,0:-1]
y_to_predict = data_to_predict[:,-1]
y_to_predict = y_to_predict.reshape( -1, 1)

ds_predcition = SDS(input_size,target_size)
ds_predcition.setField('input',x_used_for_prediction)
ds_predcition.setField('target',y_to_predict)

p = net.activateOnDataset( ds_predcition )




np.savetxt( output_predictions_file, p, fmt = '%.6f' )
