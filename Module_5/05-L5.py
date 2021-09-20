# Get familiar with 'random' module, implement function separation/execution

# Create two functions that allow implementation of random number
# generation and comparison with user input

import random

# function that generates random number
def gen_random():
    # saves random int between 1-10 to variable, returns
    number = random.randint(1,10)
    return number

# main function
def main():
    # request number from user, cast to int
    guessed_number = int(input("Please select random number between 1-10: "))
    # invoke first function, saves random number to variable
    random_number = gen_random()
    # condition that checks if user number = random number
    if guessed_number == random_number:
        print("Successful Guess!")
    # condition if guess != random number
    else:
        print("Wrong Guess!")

# condition that runs program only if file is executed directly
if __name__ == '__main__':
    main()