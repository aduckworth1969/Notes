import sys
import os
from datetime import date
from sys import exit

# menu for application
def notes_menu():
    print("________________________")
    print("\n1. Set directory.\n")
    print("2. Add tags.\n")
    print("3. Process file.\n")
    print("4. Quit.\n")
    print("________________________\n")
    menu_selection = input("Make selection:> ")
    if menu_selection == "1":
        set_directory()
    elif menu_selection == "2":
        add_tags()
    elif menu_selection == "3":
        file_process()
    elif menu_selection == "4":
        exit(0)
    else:
        print(tag_list)

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
    file_to_open = input("What file do you want to open? > ")

# opens file for processing and saves file
    infile = open(file_to_open, 'r')
    infile_read = infile.read()
    line = infile_read.readlines()
    for tag in tag_list:
        print(f"current tag is {tag}")
        file_to_save = input("What do you want to call the save file? > ")
        outfile = open(file_to_save + date_append + ".md", 'w')
    if line.strip() == tag:
        outfile.write(line)
#    elif line.strip() != tag:
#        continue
#            elif line.strip() == end_tag:
#                copy = False
#                continue
#            elif copy:
#               outfile.write(line)
    else:
        notes_menu()
#            restart()

def restart():
    restart = input("Do you have more tags to process? ")
    if restart == "yes" or restart == "y":
        file_process()
    if restart == "n" or restart == "no":
        print("Have a great day!. Goodbye.")
        sys.exit()

# variable for time format
today = date.today()
date_append = today.strftime("%Y%m%d")

tag_list = []

tag_file = open('taglist.txt', 'r')
tag_process = tag_file.readlines()

notes_menu()
