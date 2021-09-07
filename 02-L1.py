# create a script that collects user input for two variables
x_string = input("Enter 1st number: ")
y_string = input("Enter 2nd number: ")

print("Sum as string: ", x_string+y_string)

# must turned into integer for mathematical operations OR ELSE it prints results as strings
x = int(x_string)
y = int(y_string)
print("Sum: ", x+y)
print("Difference: ", x-y)
print("Multiplication: ", x*y)
print("Division: ", x/y)
print("Remainder: ", x%y)