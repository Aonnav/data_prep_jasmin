#!/bin/bash

# Input folder: $1
# Output folder: $2
rm -rf $2
mkdir $2


#enter input encoding here
#FROM_ENCODING="UTF-16"
#output encoding(UTF-8)
TO_ENCODING="UTF-8"
#loop to convert multiple files 
echo 'Converting all (tier) text files to utf-8...'
for  file  in  $1/*.awd; do
     FROM_ENCODING=$(file -i "$file" | sed -n 's/.*charset=//p')
     #echo $CONVERT   "$file"  -o  "$2/${file##*/}"
     iconv -f $FROM_ENCODING -t $TO_ENCODING "$file" -o "$2/${file##*/}"
done
exit 0
