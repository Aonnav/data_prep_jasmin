#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
# create data directory and subdirs
os.system('mkdir data')
os.system('mkdir data/train_jasmin')
os.system('mkdir data/test_jasmin')

# prepare the data
os.system('python data_prep_jasmin.py')



