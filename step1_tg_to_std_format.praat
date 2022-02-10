# Run on Windows and change the paths

form Read multiple files
	sentence source_directory C:\Users\CRISTIAN\Desktop\awd_files_to_use
	sentence save_directory C:\Users\CRISTIAN\Desktop\praat_files_to_use
	# could be .tg or .awd
	sentence read_file_extension .awd
	sentence save_file_extension .awd
endform

Create Strings as file list... list 'source_directory$'/*'read_file_extension$'
Sort

string_ID = selected("Strings")
number_of_files = Get number of strings

for ifile to number_of_files
	select Strings list
	file_name$ = Get string... ifile
	length = length(file_name$) - 4
	file_save$ = left$(file_name$, length) + save_file_extension$ 
	Read from file... 'source_directory$'/'file_name$'
	Save as text file... 'save_directory$'/'file_save$'
endfor

select 'string_ID'
Remove
