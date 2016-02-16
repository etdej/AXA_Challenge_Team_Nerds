import sys 
import os
sys.path.append(os.path.abspath("../preprocessing/"))
from features_preprocessing import *

pp = feature_preprocessing()
print(pp.data.columns)

