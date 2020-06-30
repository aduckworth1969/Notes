import sys
import os
from datetime import date
from sys import exit
import pypandoc

# menu for application
def notes_menu():
    print("________________________")
    print("\n1. Set directory.\n")
    print("2. Add tags.\n")
    print("3. Process file.\n")
    print("4. Convert markdown to Word.\n")
    print("5. Quit.\n")
    print("________________________\n")
    menu_selection = input("Make selection:> ")
    if menu_selection == "1":
        set_directory()
    elif menu_selection == "2":
        add_tags()
    elif menu_selection == "3":
        file_process()
    elif menu_selection == "4":
        convert_word()
    elif menu_selection == "5":
        exit(0)
    else:
        exit(0)

def set_directory():
    current_dir = os.getcwd()
    print(f"Correct dir? {current_dir}")
    directory_choose = input("y or n > ")
    if directory_choose == "yes" or directory_choose == "y":
        notes_menu()
    if directory_choose == "no" or directory_choose == "n":
        change_directory = input("Type the path to your directory: ")
        new_directory = os.chdir(change_directory)
        notes_menu()

def add_tags():
    for element in tag_process:
        tag_list.append(element.strip())
    add_tags = input("Add tags? ")
    if add_tags == "yes" or add_tags == "y":
        new_tag = input("Tag name (start with *)> ")
        tag_list.append(new_tag)
        with open('taglist.txt', 'w') as write_tags:
            for item in tag_list:
                write_tags.write(item + "\n")
        notes_menu()
    elif add_tags == "no" or add_tags == "n":
        notes_menu()

def file_process():

# user input for file to open
    file_to_open = input("What file do you want to open? > ")

# user input for tags
    begin_tag = input("Start tag:> ")
    con_tag = "E"
    end_tag = con_tag + begin_tag

# user input for file to save
    file_to_save = input("Save file:> ")

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

    restart = input("Do you have more tags to process? ")
    if restart == "yes" or restart == "y":
        file_extract()
    if restart == "n" or restart == "no":
        print("Have a great day!. Goodbye.")
        notes_menu()

def convert_word():
    input_file = input("File to convert:> ")
    output_file = input("Save file:> ")
    output = pypandoc.convert_file(input_file, 'docx', outputfile=output_file + date_append + ".docx")
    assert output == ""
    more_files = input("Convert another file? ")
    if more_files == "yes" or more_files == "y":
        convert_word()
    if more_files == "no" or more_files == "n":
        notes_menu()

# variable for time format
today = date.today()
date_append = today.strftime("%Y%m%d")

tag_list = []

tag_file = open('taglist.txt', 'r')
tag_process = tag_file.readlines()

notes_menu()
