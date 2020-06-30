from notion.client import NotionClient
from md2notion.upload import upload
from notion.block import PageBlock
import sys
import os


# function for file process into Notion. Follow the instructions at https://github.com/jamalex/notion-py#quickstart to setup Notion.py
def file_process():
	client = NotionClient(token_v2="InsertToken")
	page = client.get_block(notion_page)

	with open("test.md", "r", encoding="utf-8") as mdFile:
    		newPage = page.children.add_new(PageBlock, title=file_title)
    		upload(mdFile, newPage) #Appends the converted contents of TestMarkdown.md to newPage
	sys.exit()

notion_page = input("Paste Notion URL: ")

file_upload = input("Name of file: ")

file_title = input("Title for Notion page: ")

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

