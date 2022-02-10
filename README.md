
# jasmin

Automatic data selection and preparation for JASMIN (`'/vol/bigdata/corpora/JASMIN/`) corpus.

## Requirements
- Linux: Kaldi, Python3
- Windows: Praat


## Execution steps

Ponyland:

 1. `ssh rarity`
 2. `lm` (or you can activate your own lamachine). We need Kaldi to create a link to the `utils` folder.
 3. `cd <this_project_path>` (e.g., */home/ctejedor/python-scripts/data_prep_jasmin*)
 4. `ln -s $KALDI_ROOT/egs/wsj/s5/utils/ utils`
 5. `rm -rf data`
 6. Change all ***TODO*** instances in `data_sel_jasmin.py` and run it: `python3 data_sel_jasmin.py`
 7. Run these two scripts on Windows (you need Praat and the recently generated folder`awd_files_to_use`):
    - `step_1_tg_to_std_format.praat` 
      - Input: `awd_files_to_use`, output `praat_files_to_use`.
    - `step2_extract_tier.praat` 
      - Input: `praat_files_to_use`, output `tier`.
 8. Make sure you have a folder called `tier` (on Linux, *copy&paste* the content of the folder `tier` from Windows to Linux), which has been just generated with the last Praat script.
 9. Change the paths inside `data_prep_jasmin.py`: 
    - `filedir, original_prev` (the same path as *tier* folder), `test_set, train_set, rec`.
 10. *Copy&paste* the files you want from to `wav_files_to_use` to `wav_files_to_use_test` and `wav_files_to_use_train`. This step could be done manually or automatically (depends on your project).
 11. `python3 uber_jasmin.py`