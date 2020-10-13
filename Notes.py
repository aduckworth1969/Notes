import sys
import os
from datetime import date
from sys import exit
import pypandoc
from notion.client import NotionClient
from md2notion.upload import upload
from notion.block import PageBlock
from pick import pick

# Selection menu for application to choose directory, add tags, add Notion page, process a 
# file, convert markdown to Word, upload to Notion or quit app.
def notes_menu():
    print('_' * 24)
    print(f'\n1. Change directory?\n   (current directory is)\n' + os.getcwd())
    print('2. Add tags.\n')
    print('3. Add Notion page.\n')
    print('4. Process file.\n')
    print('5. Convert markdown to Word.\n')
    print('6. Upload to Notion.\n')
    print('7. Quit.\n')
    print('_' * 24, '\n')
    menu_selection = input("Make selection:> ")
    if menu_selection == "1":
        change_directory = input("Type the path to your directory: ")
        set_directory(change_directory)
    elif menu_selection == "2":
        add_tags()
    elif menu_selection == "3":
        add_notion_pages()
    elif menu_selection == "4":
        set_file()
    elif menu_selection == "5":
        set_file_word()
    elif menu_selection == "6":
        set_file_notion()
    elif menu_selection == "7":
        exit(0)
    else:
        print(os.getcwd())

# This function sets the current to what the user selected for menu option 1.
def set_directory(directory_name):
    os.chdir(directory_name)
    notes_menu()

def add_tags():
    new_tag = input("Tag name:> ")
    tag_list.append(new_tag)
    with open('taglist.txt', 'w') as write_tags:
        for item in tag_list:
            write_tags.write(item + "\n")
    more_tags = input("Add more tags?> ")
    if more_tags == 'y' or more_tags == 'yes':
        add_tags()
    elif more_tags == 'n' or more_tags == 'no':
        notes_menu()
    else:
        add_tags()

def add_notion_pages():
    add_pages = input('Add Notion pages? ')
    if add_pages == 'yes' or add_pages == 'y':
        new_page = input('Notion page URL:> ')
        notion_pages.append(new_page)
        with open('notionpage.txt', 'w') as write_pages:
            for item in notion_pages:
                write_pages.write(item + '\n')
            notes_menu()
    elif add_pages == 'no' or add_pages == 'n':
        notes_menu()

def set_file():
    directory_list = os.listdir()
    directory_files = [s for s in directory_list if s.endswith('.md')]
    title = 'Choose file for processing:> '
    file_to_open, index = pick(directory_files, title)

# user input for file to open
#    file_to_open = input("What file do you want to open? > ")
    file_process(file_to_open)

def file_process(openFile):
# user input for tags
    title = 'Choose tag for processing:> '
    begin_tag, index = pick(tag_list, title)
    con_tag = "E"
    end_tag = con_tag + begin_tag

# user input for file to save
    print(f"Selected tag is {begin_tag}")
    file_to_save = input("Save file:> ")

# opens file for processing and saves file
<<<<<<< HEAD
    with open(file_to_open) as infile, open(date_append + file_to_save + ".md", 'w') as outfile:
=======
    with open(openFile) as infile, open(file_to_save + date_append + ".md", 'w') as outfile:
>>>>>>> dev
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
        file_process()
    if restart == "n" or restart == "no":
        print("Have a great day!. Goodbye.")
        notes_menu()

def set_file_word():
    global open_word_file
    directory_list = os.listdir()
    directory_files = [s for s in directory_list if s.endswith('.md')]
    title = 'Choose file for processing:> '
    open_word_file, index = pick(directory_files, title)

    convert_word()

def convert_word():
    output_file = input("Save file:> ")
    output = pypandoc.convert_file(open_word_file, 'docx', outputfile=date_append + output_file + ".docx")
    assert output == ""
    more_files = input("Convert another file? ")
    if more_files == "yes" or more_files == "y":
        set_file_word()
    if more_files == "no" or more_files == "n":
        notes_menu()

def set_file_notion():
    global file_upload
    directory_list = os.listdir()
    directory_files = [s for s in directory_list if s.endswith('.md')]
    title = 'Choose file to upload:> '
    file_upload, index = pick(directory_files, title)
    notion_upload()

def notion_upload():
    notion_title = 'Choose Notion page:> ' 
    notion_page, index = pick(notion_pages, notion_title)
    file_title = input("Page title:> ")
    client = NotionClient(token_v2="InsertToken")
    page = client.get_block(notion_page)
    with open(file_upload, 'r', encoding='utf-8') as mdfile:
        newPage = page.children.add_new(PageBlock, title=file_title)
        # appends the converted contents of markdown file to new page
        upload(mdfile, newPage) 
    new_upload = input("Upload new file?> ")
    if new_upload == "yes" or new_upload == "y":
        notion_upload()
    if new_upload == "no" or new_upload == "n":
        notes_menu()

os.system('clear')
# variable for time format
today = date.today()
date_append = today.strftime("%Y%m%d")

tag_list = []

tag_file = open('taglist.txt', 'r')
tag_process = tag_file.readlines()
for element in tag_process:
    tag_list.append(element.strip())

notion_pages = []

notion_page_file = open('notionpage.txt', 'r')
notion_page_process = notion_page_file.readlines()
for element in notion_page_process:
    notion_pages.append(element.strip())

notes_menu()
