# Create a file and directory using names specified by user
# then list all files that exist in directory

import os
import datetime

# within loop print cwd
while True:
    print("Current directory: " + os.getcwd())
    # ask user for directory name and store name in variable
    new_directory = input("Choose a name for new directory: ")
    # create desired directory, navigate to
    os.mkdir(new_directory)
    os.chdir(new_directory)
    # print new cwd
    print("Current directory: " + os.getcwd())
    # if condition that will check if dir exists
    if new_directory:
        try:
            # ask user for filename, store in variable
            file_name = input("Choose filename: ")
            # open newly created file with read/write perms
            with open(f'{file_name}.txt', "w+") as new_file:
                # message telling user file was created, current datetime
                new_file.write('Good job! File created on: ' + str(datetime.datetime.now()))
                # list contents of cwd, add break
                print('The following files are in cwd: ' + str(os.listdir()))
                break
        except:
            print("Error unknown, please try again.")
