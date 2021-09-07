# create script that will extract text from a file provided
# by user and read one line at a time

# Lorem Ipsum.txt as file
# C:\Users\Joao\Desktop  as path

# receive file path from user and set it to variable
path = input("Enter a directory path for the text file: ")

# receive filename from user set to diff variable
filename = input("Enter full filename: ")

# open file with read perms using 'open()' function with path and
# filename variables
file = open(path+"\\"+filename, "r")
# create for loop to print each line in file
for line in file:
    print(line)

# close file at end of loop
file.close()
