import os
from datetime import datetime

# variable for time format

# changes the working directory to Notes in icloud
# os.chdir('/Users/aduckworth/icloud/Notes')

# user input to define variables for tags
begin_tag = input("What is the beginning tag? > ")
con_tag = "E"
end_tag = con_tag + begin_tag

# user input to define variable for file to open
file_to_open = input("What file do you want to open? > ")

# user input to define variable for file to save
file_to_save = input("What do you want to call the save file? > ")

# reads the file that was identified via the variable from user input
# read_file = open(file_to_open, 'r')

# pulls text out of the file as a variable
# my_file_contents = read_file.read()

with open(file_to_open) as infile, open(file_to_save, 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == begin_tag:
            copy = True
            continue
        elif line.strip() == end_tag:
            copy = False
            continue
        elif copy:
            outfile.write(line)
