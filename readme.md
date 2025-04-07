#1 fileTypes.py contains a list of different filetypes and saves it to a csv
called fileTypes.csv


#2 generateFiles.py goes through fileTypes.csv and creates "n" number of files per
filetype and outputs it to the folder "filesToSort"


#3 script.py goes through files to sort, and creates a new folder in "sortedFiles"
per filetype, and moves each file accordingly to their respective folder.



# python3 generateFiles.py --value 100
# python3 script.py --delete

# generates 100 files in a folder called filesToSort
# after sorting them and adding them to sortedFiles, delete the files from filesToSort
