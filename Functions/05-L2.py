# create several functions that return a type of value/ID it

# declare function that accepts two parameters
def returned_list(first, second):
    return [first, second]
# second function
def returned_dict(first, second):
    return {first:second}
# third function
def returned_tup(first, second):
    return first, second
# fourth function
def returned_none(first, second):
    # make function perform add op on params
    res = first + second

def main():
    val1 = input("Please enter a value: ")
    val2 = input("Please enter another value: ")
    # saves first function's result
    list_res = returned_list(val1, val2)
    dict_res = returned_dict(val1, val2)
    tup_res = returned_tup(val1, val2)
    none_res = returned_none(val1, val2)
    # prints results and types
    print(f"{list_res} and its type is: {type(list_res)}")
    print(f"{dict_res} and its type is: {type(dict_res)}")
    print(f"{tup_res} and its type is: {type(tup_res)}")
    print(f"{none_res} and its type is: {type(none_res)}")
main()
