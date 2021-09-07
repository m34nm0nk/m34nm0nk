# write program that calculates product of four numbers provided by user
# and prints results, use try/except statements to ensure program will not
# fail when input is not a valid number

# create for loop that performs 4 iterations
product = 1
for i in range(4):
    # place user input/math op in  try block
    try:
        # ask user tp provide number, cast number to int, assign new variable
        # multiply each input by the 'product' variable and assign result
        # to same variable
        num = int(input("Enter a number: "))
        product *= num
    # prints message if input is not an integer
    except:
        print("The input is not a valid number!")
# print message telling user product of four numbers, cast variable
# to string
print("The product of the 4 numbers is: " + str(product))
