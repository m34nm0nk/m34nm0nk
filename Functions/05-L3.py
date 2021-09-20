# learn how a global scope influences variables

global_var = 5
changed_global_var = 20

def local_change():
    # change value of the first variable and print
    global_var = 10
    print("inside function global_var's value: ", global_var)
    # within func, declare second variable as global
    # changes global value of variable
    global changed_global_var
    # within func, change second variable
    changed_global_var += 5
    print("inside function changed_global_var's value: ", changed_global_var)
# invoke
local_change()
# prints values of both functions after invocation
print("outside function global_var's value: ", global_var)
print("outside function changed_global_var's value: ", changed_global_var)
