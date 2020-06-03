import pypandoc

input_file = input("What file do you want to convert? > ")

output_file = input("Save file as: > ")

output = pypandoc.convert_file(input_file, 'docx', outputfile=output_file)
assert output == ""
