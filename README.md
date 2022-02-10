
# jasmin

Automatic data selection and preparation for JASMIN (`'/vol/bigdata/corpora/JASMIN/`) corpus.

## Requirements
- Linux: Kaldi, Python3 and Praat


## Execution steps

Tested on Ponyland:

 1. `ssh rarity`
 2. `lm` (or you can activate your own lamachine). We need Kaldi to create a link to the `utils` folder.
 3. `cd <this_project_path>` (e.g., */home/ctejedor/python-scripts/data_prep_jasmin*)
 4. `ln -s $KALDI_ROOT/egs/wsj/s5/utils/ utils`
 5. `rm -rf data`
 6. Change all ***TODO*** instances in `data_sel_jasmin.py`
 7. Change the values of the variables `source_directory`, `save_directory`, `read_file_extension` and `save_file_extension`of the files:
    - `step_1_tg_to_std_format.praat` 
    - `step2_extract_tier.praat` 
 8. You also need to change the same values of step 7 in the file: `uber_jasmin.py` (*TODO* line).
 9. Change the *TODO* paths inside `data_prep_jasmin.py`: 
    - `filedir, original_prev` (the same path as *tier* folder), `test_set, train_set, rec`.
 10. `python3 uber_jasmin.py`
 11. *Copy&paste* the files you want from to `wav_files_to_use` to `wav_files_to_use_test` and `wav_files_to_use_train`. This step could be done manually or automatically (depends on your project).
 12. Press [Enter]