#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import os 
import os.path

## DIRECTORIES ##
# data dir, e.g.; "/vol/tensusers3/nvhelleman/jasmin/data/"
filedir = "/vol/tensusers3/nvhelleman/jasmin/data/"
# tier dir, e.g.; "/vol/tensusers3/nvhelleman/jasmin/20210326/tier/"
original = "/vol/tensusers3/nvhelleman/jasmin/20210326/tier/"
# wav files to use dir, e.g.; "/vol/tensusers3/nvhelleman/jasmin/20210326/wav_files_to_use/"
soundfile = "/vol/tensusers3/nvhelleman/jasmin/20210326/wav_files_to_use/"
# rec to use file
rec = "/vol/tensusers3/nvhelleman/jasmin/20210326/rec_to_use.txt"

## TRAIN / TEST SET ##
train = []
test = []
for name in os.listdir(original):
    if re.search("^fn000",name):
        test.append(name)   # => test set
    elif re.search("^fn000.",name):
        train.append(name)     # => train set

## TEXT ##
def text(filenames):
    results = []
    for name in filenames:
        file = open(original + name)
        basename = name.split('.')[0]
        transcript = ""
        number = 1
        for line in file:
          if "text =" in line:
            if re.findall('"([^"]*)"', line)[0] != "":
              transcript += " "+ re.findall('"([^"]*)"', line)[0]
              if "." in line:
                results.append("{} {}".format(basename+"_"+str(number).zfill(4), transcript))
                number += 1
                transcript = ""
    return '\n'.join(sorted(results))

with open(filedir+'train_jasmin/text', 'w', encoding='utf-8') as train_text, open(filedir+'test_jasmin/text', 'w', encoding='utf-8') as test_text:
    train_text.write(text(train))
    test_text.write(text(test))

## UTT2SPK ##
def utt2spk(filenames):
    results = []
    for name in filenames:
      file = open(original + name)
      basename = name.split('.')[0]
      number = 1
      for line in file:
        if "text =" in line:
          if "." in line:
            results.append("{} {}".format(basename+"_"+str(number).zfill(4), basename))
            number += 1          
    return '\n'.join(sorted(results))

with open(filedir+'train_jasmin/utt2spk', 'w', encoding='utf-8') as train_text, open(filedir+'test_jasmin/utt2spk', 'w', encoding='utf-8') as test_text:
    train_text.write(utt2spk(train))
    test_text.write(utt2spk(test))

## WAV.SCP ##
def wav_scp(filenames):
    results = []
    for name in filenames:
        basename = name.split('.')[0]
        results.append("{} {}".format(basename, soundfile + name))
    return "\n".join(results)

with open(filedir+'train_jasmin/wav.scp', 'w', encoding='utf-8') as train_text, open(filedir+'test_jasmin/wav.scp', 'w', encoding='utf-8') as test_text:
    train_text.write(wav_scp(train))
    test_text.write(wav_scp(test))

## SPK2UTT ##
def spk2utt():
    os.system('../utils/utt2spk_to_spk2utt.pl data/test_jasmin/utt2spk > data/test_jasmin/spk2utt')
    os.system('../utils/utt2spk_to_spk2utt.pl data/train_jasmin/utt2spk > data/train_jasmin/spk2utt')

spk2utt()  

## SEGMENTS ##
def segments(filenames):
    results = []
    for name in filenames:
        file = open(original + name)
        basename = name.split('.')[0]
        begin = ""
        end = ""
        start = True
        number = 1
        for line in file:
          if "xmin =" in line and start:
            begin = line.split('= ')[1]
            start = False
          if "xmax =" in line:
            end = line.split('= ')[1]
          if "text =" in line:
            if "." in line:
              results.append("{} {} {} {}".format(basename+"_"+str(number).zfill(4), basename, begin, end))
              number += 1
              start = True     
    return '\n'.join(sorted(results))

with open(filedir+'train_jasmin/segments', 'w', encoding='utf-8') as train_text, open(filedir+'test_jasmin/segments', 'w', encoding='utf-8') as test_text:
    train_text.write(segments(train))
    test_text.write(segments(test))

## SPK2GENDER ##
def spk2gender(filenames):
    results = []
    for name in filenames:
        file = open(rec)
        basename = name.split('.')[0]
        for line in file:
          if basename in line:
            if "F" in line:
              results.append("{} {}".format(basename, "F"))
            elif "M" in line:
              results.append("{} {}".format(basename, "M"))
    return "\n".join(results)

with open(filedir+'train_jasmin/spk2gender', 'w', encoding='utf-8') as train_text, open(filedir+'test_jasmin/spk2gender', 'w', encoding='utf-8') as test_text:
    train_text.write(spk2gender(train))
    test_text.write(spk2gender(test))
