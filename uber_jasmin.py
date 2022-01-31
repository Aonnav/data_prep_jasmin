#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
# create data directory and subdirs
os.system('mkdir data')
os.system('mkdir data/train_jasmin')
os.system('mkdir data/test_jasmin')

# prepare the data
if os.path.exists('utils'):
    print('Directory utils/ exists.')

    # prepare the data
    os.system('python3 data_prep_jasmin.py')

    # check the data
    os.system('./utils/validate_data_dir.sh data/train_jasmin/ --no-feats')
    os.system('./utils/validate_data_dir.sh data/test_jasmin/ --no-feats')
else:
   print('You need a valid utils/ folder:\n Try this command: ln -s $KALDI_ROOT/egs/wsj/s5/utils/ utils') 
