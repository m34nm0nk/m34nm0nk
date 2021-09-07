# Construct interactive script that asks the user for the name of
# a service and a port number, and assigns the values in a dictionary as
# a key:value pair, then creates a while loop whereby if the user chooses
# 0 as either input the loop will end

servicePorts = {}

# create variable that asks for a service name
while True:
    service = input("Please enter a service's name or type '0' to stop: ")
    # add if condition in while loop to break the loop if input is 0
    if service == '0':
        break
    # in while loop ask for port number in variable
    port = input("Please enter a matching port number for service or type '0' to stop: ")

    # if condition to break if input is 0
    if port == '0':
        break
    # insert data from service and port variables as key:value pairs in dict
    servicePorts[service] = port
print(servicePorts)
