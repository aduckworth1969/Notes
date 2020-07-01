import sys
import os
from datetime import date
from sys import exit
import pypandoc
from notion.client import NotionClient
from md2notion.upload import upload
from notion.block import PageBlock

# menu for application
def notes_menu():
    print("________________________")
    print("\n1. Set directory.\n")
    print("2. Add tags.\n")
    print("3. Process file.\n")
    print("4. Convert markdown to Word.\n")
    print("5. Upload to Notion.\n")
    print("6. Quit.\n")
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
        notion_upload()
    elif menu_selection == "6":
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

def notion_upload():
    notion_page = input("Notion page URL:> ")
    file_upload = input("File:> ")
    file_title = input("Page title:> ")
    client = NotionClient(token_v2="1082148eb4f64df07b7e7e3abde9615282978abcbc0724769bf05548243e304164bf94bfd110c1646930be92239dc75c72bb61ff15f6888a0454958a983484ce5c3f52ea7048feaf3f5aa9025b47")
    page = client.get_block(notion_page)
    with open(file_upload, 'r', encoding='utf-8') as mdfile:
        newPage = page.children.add_new(PageBlock, title=file_title)
        upload(mdfile, newPage) # appends the converted contents fo markdown file to new page
    new_upload = input("Upload new file?> ")
    if new_upload == "yes" or new_upload == "y":
        notion_upload()
    if new_upload == "no" or new_upload == "n":
        notes_menu()

# variable for time format
today = date.today()
date_append = today.strftime("%Y%m%d")

tag_list = []

tag_file = open('taglist.txt', 'r')
tag_process = tag_file.readlines()

notes_menu()
