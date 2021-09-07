"""
# create with() statement that opens a file in read mode
# then try to write to it (this will not work)

try:
    with open("text.txt", "r") as text:
        # write any text in opened file
        text.write("Test")

# create exception block to handle error and print error message
# explaining that an open file cannot be written to in read mode
except Exception:
    print("Unsupported Operation, cannot write in read mode.")

# create script that will open file, take input and use to write
# to a file before exiting
"""
# put code in try block
try:
    # open new file in append mode, set it to variable, append will create
    # file if it does not already exist
    file = open("file.txt", "a")
    # add infinite while loop that will take user input and set to variable
    while True:
        message = input("Enter text! ('Exit' to exit): ")
        # if input is 'exit' then exit program
        if message.lower() == 'exit':
            break
        # if input not 'exit' write input to file, move to next line
        else:
            file.write(message + "\n")
    # once loop done running use 'close()' to close file
    file.close()
# add except block after try to handle any unexpected errors
except:
    print("An error has occurred while trying to open file.")
# print contents of file.txt
# file = open("file.txt", "r")
# print(file.read())
# file.close()
#       OR
with open("file.txt", "r") as file:
    print(file.read())
file.close()

