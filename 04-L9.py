# SYS module provides various functions and variables that are
# used to manipulate diff parts of the Python runtime environment

import sys
import os
# outputs version of Python interpreter
# print(sys.version)
# # list out all the paths
# print(sys.path)

# prints current directory
print(os.path.curdir)

# checks whether specified path is an existing directory/not
# returns True/False
print(os.path.isdir('.'))

# return True if path refers to existing path/open file
print(os.path.exists("C:/Users/Joao/PycharmProjects/Module_4"))

# get size of file specified
print(os.path.getsize('file.txt'))


# Signal module