import os
# put both uber and data_prep file in the same folder, the data directory will be created there too

# create data directory and subdirs
os.system('mkdir data')
os.system('mkdir data/train_jasmin')
os.system('mkdir data/test_jasmin')

# prepare the data
os.system('python data_prep_jasmin.py')



