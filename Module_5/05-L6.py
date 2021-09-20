# Program that identifies items in a list of integers and other data types
# and prints only numbers within nested lists

lst = [1, 2, "a", [4, 5, "b", 6], [7, [8, "d", 9]]]
# function to accept parameter
def print_numbers(item_list):
    # iterate over accepted parameter
    for item in item_list:
        # checks if iterated item is an int, print if yes
        if type(item) == int:
            print(item)
        # continues condition, if item = list invoke function again with item as provided parameter
        elif type(item) == list:
            print_numbers(item)
print_numbers(lst)
