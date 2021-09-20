# Create a script that checks if users can legally purchase an alcoholic beverage
# Receive user input for two variables; name and age
# Use conditional operators to compare the age variable against the legal age

name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello {}, your age is {}".format(name, age))

if age >= 21:
    print("You CAN buy an alcoholic beverage, drink responsibly :)")
else:
    print("WARNING!WARNING!WARNING!\nYou CANNOT buy an alcoholic beverage")
