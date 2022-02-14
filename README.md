
# jasmin

Automatic data selection and preparation for JASMIN (`/vol/bigdata/corpora/JASMIN/`) corpus.

## Requirements
- Linux: Kaldi, Python3 and Praat


## Execution steps

Tested on Ponyland:

 1. `ssh rarity`
 2. `lm` (or you can activate your own lamachine). We need this command to create a link to the `utils` Kaldi folder (in step 4).
 3. `this_project_path=/home/ctejedor/python-scripts/data_prep_jasmin && local_jasmin=20220211`
 4. `cd $this_project_path`
 5. `ln -s $KALDI_ROOT/egs/wsj/s5/utils/ utils`
 6. `python3 uber_jasmin.py $local_jasmin $this_project_path .awd .awd`
   - `$local_jasmin`: name of the folder in which the selected JASMIN data will be generated.
   - `$this_project_path`: path to the project.
   - `.awd`: format of the original source files to transform into standard files.
   - `.awd`: format of the (output) standard files.
 7. In another Linux terminal, *copy&paste* the files you want from to `$local_jasmin/wav_files_to_use` to `$local_jasmin/wav_files_to_use_test` and `$local_jasmin/wav_files_to_use_train`. This step could be done manually or automatically (depends on your project).
 8. Press [Enter]
