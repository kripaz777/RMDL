'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
RMDL: Random Multimodel Deep Learning for Classification

 * Copyright (C) 2018  Kamran Kowsari <kk7nc@virginia.edu>
 *
 * This file is part of  RMDL project, University of Virginia.
 *
 * Free to use, change, share and distribute source code of RMDL
 *
 *
 * Refrenced paper : RMDL: Random Multimodel Deep Learning for Classification
 *
 * Refrenced paper : An Improvement of Data Classification using Random Multimodel Deep Learning (RMDL)
 * 
 * Comments and Error: email: kk7nc@virginia.edu
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys
sys.path.append('../src')
sys.path.append('../Download_datasets')
import os
os.environ["THEANO_FLAGS"] = "mode=FAST_RUN,device=gpu,floatX=float32"
os.environ['KERAS_BACKEND'] = 'tensorflow'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ["CUDA_VISIBLE_DEVICES"]="2,1,0"
from RMDL import text_feature_extraction as txt
from Download import Download_WOS as WOS
from RMDL import RMDL_Text as RMDL
import sys
sys.path.append('../Download_datasets')
from sklearn.cross_validation import train_test_split
import numpy as np



if __name__ == "__main__":
    path_WOS = WOS.download_and_extract()
    fname = os.path.join(path_WOS,"WebOfScience/WOS5736/X.txt")
    fnamek = os.path.join(path_WOS,"WebOfScience/WOS5736/Y.txt")
    with open(fname, encoding="utf-8") as f:
        content = f.readlines()
        content = [txt.text_cleaner(x) for x in content]
    with open(fnamek) as fk:
        contentk = fk.readlines()
    contentk = [x.strip() for x in contentk]
    Label = np.matrix(contentk, dtype=int)
    Label = np.transpose(Label)
    np.random.seed(7)
    print(Label.shape)
    X_train, X_test, y_train, y_test = train_test_split(content, Label, test_size=0.2, random_state=4)

    batch_size = 100
    sparse_categorical = 0
    n_epochs = [5, 500, 500]  ## DNN--RNN-CNN
    Random_Deep = [3, 0, 0]  ## DNN--RNN-CNN

    RMDL.Text_Classification(X_train, y_train, X_test, y_test, batch_size, sparse_categorical, Random_Deep,
                            n_epochs)
