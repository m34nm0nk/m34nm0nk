# Create variable to be used as a counter and set its value
# to zero since it will be the counter's starting point
counter = 0

# Create while loop with a condition that checks if the counter's value
# is less than 10
while counter < 10:
    counter += 1
    if counter == 7:
        print("Found!")
        pass
    else:
        print(f'Check {counter}')
