# Program that will print all files in a directory, as well as the name and size
# of each file and iterate through any directories found

import os
import sys

# variable to act as separator between outputs
line = "<--------------------------------------------------------------------------------------------------------------------->"
# var to store sys type, print
system = sys.platform
print(f'You are using: {system}')
# var to store user input of directory path
root_folder = input("Enter folder: ")

# function that accepts a parameter that will be dir path
# dedicated to handling mapping operation
def mapper(path):
    try:

    # loop to iterate over dir contents
        for item in os.listdir(path):
            # var to store full path of iterated item
            full_path = r'{}\{}'.format(path, item)
            # condition to check if full path leads to file
            if os.path.isfile(full_path):
                # if path leads to a file, create var to save file size, print
                size = os.stat(full_path).st_size
                print(f"Found {full_path} -> weighs {size}")

            # if path leads to dir, print message stating that program
            # is entering dir, invoke recursively
            elif os.path.isdir(full_path):
                print(f'{line}\nEntering folder {item}\n{line}')
                mapper(full_path)
            # if path leads to anything but dir/file, print 'unknown'
            else:
                print("Unknown.")

    # catch potential exception
    except Exception as error:
        print(error)

# invoke mapping function
mapper(root_folder)
