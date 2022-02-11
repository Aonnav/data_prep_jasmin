
# jasmin

Automatic data selection and preparation for JASMIN (`/vol/bigdata/corpora/JASMIN/`) corpus.

## Requirements
- Linux: Kaldi, Python3 and Praat


## Execution steps

Tested on Ponyland:

 1. `ssh rarity`
 2. `lm` (or you can activate your own lamachine). We need this command to create a link to the `utils` Kaldi folder (in step 4).
 3. `cd <this_project_path>` (e.g., */home/ctejedor/python-scripts/data_prep_jasmin*)
 4. `ln -s $KALDI_ROOT/egs/wsj/s5/utils/ utils`
 5. `python3 uber_jasmin.py 20220211 /home/ctejedor/python-scripts/data_prep_jasmin .awd .awd`
   - `20220211`: name of the folder in which the selected JASMIN data will be generated.
   - `/home/ctejedor/python-scripts/data_prep_jasmin`: path to the project
   - `.awd`: format of the original source files to transform into standard files
   - `.awd`: format of the (output) standard files
 6. *Copy&paste* the files you want from to `wav_files_to_use` to `wav_files_to_use_test` and `wav_files_to_use_train`. This step could be done manually or automatically (depends on your project).
 7. Press [Enter]