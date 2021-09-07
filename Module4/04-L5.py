# Perform a ping to 8.8.8.8 to verify that a network connection exists
# in the system, save to file, print info based on results
import os

# create variable, assign filename value provided by user
file_name = input("Choose a filename: ")

# os.system() to perform ping
# save results to new file with name chosen by user
os.system(r'ping 8.8.8.8 >>' + file_name + ".txt")
# use open() function to read file
with open(file_name + ".txt", "r") as file:
    # create if condition to check if file contains 'ms' (milliseconds)
    if "ms" in file.read():
        # message if 'ms' found
        print("You have connection.")
    # add else is 'ms' not found
    else:
        print("You do NOT have connection.")
