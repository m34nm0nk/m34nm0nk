# OOP practice, creating a class and its attributes

# creates class named 'Car'
class Car:
    # defines initialization method of the class
    def __init__(self, color, windows_number, price):
        # assign data passed by the parameters to the 'self' variable
        self.color = color
        self.windows_number = windows_number
        self.price = price

# creates new class objects, pass required parameters
car1 = Car("Red", 4, 100000)
car2 = Car("Blue", 2, 300500)

# prints attributes of 'Car' objects
print(car1.color)
print(car2.price)
