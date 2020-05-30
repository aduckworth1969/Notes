import os
from datetime import date

# variable for time format
today = date.today()
date_append = today.strftime("%Y%m%d")

# set directory
current_dir = os.getcwd()
change_directory = input("Type the path to your directory: ")

# user input to define variable for file to open
file_to_open = input("What file do you want to open? > ")

def file_process():

# changes the working directory to user selection
	os.chdir(change_directory)

# user input to define variables for tags
	begin_tag = input("What is the beginning tag? > ")
	con_tag = "E"
	end_tag = con_tag + begin_tag

# user input to define variable for file to save
	file_to_save = input("What do you want to call the save file? > ")

# opens file for processing and saves file
	with open(file_to_open) as infile, open(file_to_save + date_append + ".md", 'w') as outfile:
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
	restart()

def restart():
	restart = input("Do you have more tags to process? ")
	if restart == "yes" or restart == "y":
		file_process()
	if restart == "n" or restart == "no":
		print("Script terminating. Goodbye.")

file_process()
