import sys
import os
sys.path.append(os.path.abspath("../preprocessing/"))
import features_preprocessing as fp
import submission_preprocessing as sp
import submission_postprocess as pp
import pandas as pd

postprocess = pp.submission_postprocess()
data = pd.read_table('predictions.txt')
print(data)
postprocess.premier_submit(pred=data)