#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Please, modify all TODO instances (x3)

import re
import os
import glob
import sys
import shutil
from pathlib import Path

# Change these two values
date = '20220211' # TODO-1
myfolder = os.path.join('/home/ctejedor/python-scripts/data_prep_jasmin', date)  # TODO-2 root folder

# Default paths (Ponyland)
jasmin_folder = '/vol/bigdata/corpora/JASMIN/'
recordings = '/vol/bigdata/corpora/JASMIN/CDdoc/data/meta/text/nl/recordings.txt'
selected_recordings = os.path.join(myfolder, 'rec_to_use.txt')
wav_folder = os.path.join(myfolder, 'wav_files_to_use')
wav_folder_train = os.path.join(myfolder, 'wav_files_to_use_train')
wav_folder_test = os.path.join(myfolder, 'wav_files_to_use_test')
ort_folder = os.path.join(myfolder, 'ort_files_to_use')
hmi_folder = os.path.join(myfolder, 'hmi_files_to_use')
awd_folder = os.path.join(myfolder, 'awd_files_to_use')

# remove my old folder
shutil.rmtree(myfolder, ignore_errors=True)

# create myfolder
path_to_myfolder = Path(myfolder)
path_to_myfolder.mkdir()
praat_folder = os.path.join(myfolder,'praat_files_to_use')
tier_folder =  os.path.join(myfolder,'tier')
os.mkdir(praat_folder)
os.mkdir(tier_folder)

# generate selected recordings, change the if statement accordingly
with open(recordings,'r', encoding='utf-8') as f_in, open(selected_recordings,'w', encoding='utf-8') as f_out:
    for line in f_in:
        w_lst = line.split()
        if w_lst[3] == '1': # TODO-3 groups or component (see columns in file "$recordings")
            f_out.write(line)

# create folders if not exist, remove folders if exist
myfolder_lst = [wav_folder, ort_folder, hmi_folder, awd_folder, wav_folder_train, wav_folder_test]
for myfolder in myfolder_lst:
    if os.path.isdir(myfolder):
        filelist = [f for f in os.listdir(myfolder)]
        for f in filelist:
            os.remove(os.path.join(myfolder,f))
    else:
        os.mkdir(myfolder)

# put selected recordings .wav .ort .hmi and .awd in my folders
name_lst = []
with open(selected_recordings, 'r', encoding='utf-8') as f:
    for line in f:
        name_lst.append(line.split()[0])

wav_file_lst = []
ort_file_lst = []
hmi_file_lst = []
awd_file_lst = []
# Cristian: this is not optimized at all... but it works :)
for i in name_lst:
    for dirpath, dirnames, filenames in os.walk(jasmin_folder):
        for filename in filenames:
            if i in filename:
                if filename.endswith('.wav'):
                    wav_file_lst.append(os.path.join(dirpath, filename))
                if filename.endswith('.ort'):
                    ort_file_lst.append(os.path.join(dirpath, filename))
                if filename.endswith('.hmi'):
                    hmi_file_lst.append(os.path.join(dirpath, filename))
                if filename.endswith('.awd'):
                    awd_file_lst.append(os.path.join(dirpath, filename))

print('wav_file_lst',len(wav_file_lst))
for j in wav_file_lst:
    #print(j)
    shutil.copy(j, wav_folder)

print('ort_file_lst',len(ort_file_lst))
for m in ort_file_lst:
    #print(m)
    shutil.copy(m, ort_folder)

print('hmi_file_lst',len(hmi_file_lst))
for n in hmi_file_lst:
    #print(n)
    shutil.copy(n, hmi_folder)

print('awd_file_lst',len(awd_file_lst))
for q in awd_file_lst:
    #print(q)
    shutil.copy(q, awd_folder)
