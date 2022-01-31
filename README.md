# jasmin

Automatic data preparation for the Kaldi files for DART

## Execution steps

Ponyland:

 1. `ssh rarity`
 2. `cd /home/ctejedor/python-scripts/data_prep_jasmin`
 3. `ln -s $KALDI_ROOT/egs/wsj/s5/utils/ utils` 
 4. `cp -r vol/tensusers3/nvhelleman/jasmin/20210326/ .`
 5. Change the paths inside `/home/ctejedor/python-scripts/data_prep_jasmin.py`: `filedir, original, test_set, train_set, rec`
 6. `python3 uber_jasmin.py`
