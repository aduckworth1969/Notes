import pypandoc
import os
import sys

# function for processing file to Word
def file_process():
	input_file = input("What file do you want to convert? > ")

	output_file = input("Save file as: > ")

	output = pypandoc.convert_file(input_file, 'docx', outputfile=output_file)
	assert output == ""
	sys.exit()

# set working directory
current_directory = os.getcwd()
print(f"Use this directory? {current_directory}")
directory_choose = input("y or n > ")
if directory_choose == "yes" or directory_choose == "y":
	file_process()
if directory_choose == "no" or directory_choose =="n":
	change_directory = input("Type directory path: ")

# function call
file_process()
