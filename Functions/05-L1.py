# program that performs simple mathematical calculations and
# is separated into functions

# request input of two numbers and operator
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number:"))
operator = input("Please enter one of the following operators: +,-,*,/ : ")

# define a function that accepts two parameters for add
def add(num1, num2):
    # config function to return result of add and description
    description = f"{num1} + {num2}"
    return f"The result of {description} = {num1 + num2}"
def sub(num1, num2):
    # same for subtraction
    description = f"{num1} - {num2}"
    return f"The result of {description} = {num1 - num2}"
def multiply(num1, num2):
    # etc
    description = f"{num1} * {num2}"
    return f"The result of {description} = {num1 * num2}"
def divide(num1, num2):
    description = f"{num1} / {num2}"
    return f"The result of {description} = {num1 / num2}"
# creates main function that will handle the execution of calc commands
def calc():
    # dictionary to connect between the selected parameter and
    # appropriate function
    allowed_calcs = {"+": add, "-": sub, "*": multiply, "/": divide}
    # allows execution of on of the calculation functions
    # to be performed according to the selected parameter/print
    try:
        result = allowed_calcs[operator](num1, num2)
        print(result)
    except KeyError:
        print("The parameter doesn't exist.")
calc()
