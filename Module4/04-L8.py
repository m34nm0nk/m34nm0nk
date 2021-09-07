# Create script to copy file in directory and assign diff filename
# modified to allow user input to create own dir and file
import os

# print cwd ask user for new dir name
cwd = (os.getcwd())
new_dir = input("Create a new directory: ")
# create new directory from cwd
try:
    os.mkdir(cwd + "\\" + new_dir)
# if new_dir entered go to exception
except:
    print("This directory already exists.")
# ask user for new file name, change dir to new_dir
new_file = input("Create new file name: ")
os.chdir(cwd + '\\' + new_dir)
# open a file in new dir in append mode
with open(f'{new_file}.txt', "a") as file:
    pass
    # print cwd which should be new_dir created above
    print("Current directory: " + os.getcwd())
# user input for dir and file, new name of file to be copied
path = input("Enter directory path: ")
filename = input("Enter filename: ")
copy_file = input("Enter new filename: ")

# create txt file to copy and use the system function from OS to
# execute copy command
os.system(r"copy {}\{} {}\{}".format(path, filename + '.txt', path, copy_file + '.txt'))
