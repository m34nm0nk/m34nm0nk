# Create script that will simulate shopping experience
money = 50
shopping_cart = []
fruits = {"Apple": 5, "Raspberry": 10, "Lemon": 20}

# create infinite loop
while True:
    if money <= 0:
        print("Thanks for shopping!")
        break
    # else block to if condition asks user to buy fruit of their choice
    # title() to cause it input to begin with capital
    else:
        choice = input(f'Please make a selection {fruits}: ').title()
        # if statement to check if user chose a fruit that exists in dict
        if choice in fruits:
            # in  user's choice condition that checks if the user has
            # enough money to buy fruit
            if money >= fruits[choice]:
                shopping_cart.append(choice)
                # decrease amount of money available to user in accordance
                # with fruit purchased
                money -= fruits[choice]
                # when fruit purchased, print current state of shop list/money
                print(f'Shopping cart: {shopping_cart} \nMoney left: {money}')
            else:
                print("You don't have enough money to make this purchase.")
        else:
            print("Invalid choice.")
