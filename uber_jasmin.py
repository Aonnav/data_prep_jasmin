#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
# create data directory and subdirs
os.system('mkdir -p data')
os.system('mkdir -p data/train_jasmin')
os.system('mkdir -p data/test_jasmin')

if os.path.exists('utils'):
    print('Directory "utils/" exists :)')

    # 1. DATA SELECTION
    # Optional: uncomment the following lines to select and praat the files
    os.system('python3 data_sel_jasmin.py')
    # You need to run these two scripts on Windows (not working on Linux yet)
    # TODO: change the parameters accordingly
    os.system('/usr/bin/praat --run step1_tg_to_std_format.praat "20220211/awd_files_to_use" "20220211/praat_files_to_use" ".awd" ".awd" > _step1.txt')
    # TODO: change the parameters accordingly
    os.system('/usr/bin/praat --run step2_extract_tier.praat "20220211/praat_files_to_use" "20220211/tier" > _step2.txt')

    
    # 2. DATA PREPARATION
    input("Before data preparation, prepare your train and test wav folders and press [ENTER]...")
    os.system('python3 data_prep_jasmin.py')

    # 3. DATA CHECKING
    os.system('./utils/validate_data_dir.sh data/train_jasmin/ --no-feats')
    os.system('./utils/validate_data_dir.sh data/test_jasmin/ --no-feats')
else:
   print('You need a valid utils/ folder:\n Try this command: ln -s $KALDI_ROOT/egs/wsj/s5/utils/ utils') 
