# These values do not matter on Linux (only on Windows) -- BEGIN
form Read multiple files
	sentence source_directory 20220211/praat_files_to_use
	sentence save_directory 20220211/tier
endform
# These values do not matter on Linux (only on Windows) -- END

Create Strings as file list... list 'source_directory$'/*
Sort

string_ID = selected("Strings")
number_of_files = Get number of strings

for ifile to number_of_files
	select Strings list
	file_name$ = Get string... ifile
	#writeInfoLine: "file name is", file_name$

	Read from file... 'source_directory$'/'file_name$'
	Extract one tier: 1
	Save as text file... 'save_directory$'/'file_name$'
endfor 

select 'string_ID'
Remove
