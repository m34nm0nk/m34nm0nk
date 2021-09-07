# write a code in which the 'range' function is modified in
# accordance with input from the user

# create variable that gets a number from the user to be used as the
# range functions upper limit
upper_bound = int(input("Choose the range upper bound --> "))
# create a 'for' loop with the 'range' function where its starting point
# is 1 and its upper limit is the input from the user
for x in range(1, upper_bound):
    # print function in the for loop that prints the result of each iteration
    print(f'The next number in line is {x}')
