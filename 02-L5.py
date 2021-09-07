# construct interactive script that will ask user for IP address
# and convert it to a binary value

ipA = input('Please enter a valid IP address: ')

# split each octet using '.' as a delimiter and store it in a new variable
# this will divide input string into list format
ipOctet = ipA.split('.')
print(ipOctet)

# store the octets in a variable as an integer
first = int(ipOctet[0])
second = int(ipOctet[1])
third = int(ipOctet[2])
fourth = int(ipOctet[3])

# condition to verify IP address is in range
if first > 255:
    print("INVALID IP address!!")
elif second > 255:
    print("INVALID IP address!!")
elif third > 255:
    print("INVALID IP address!!")
elif fourth > 255:
    print("INVALID IP address!!")
else:
# print octets binary value by 'casting'
    print(f'{first}: {bin(first)[2:]}\n' f'{second}: {bin(second)[2:]}\n' f'{third}: {bin(third)[2:]}\n' f'{fourth}: {bin(fourth)[2:]}')

# [2:] removes the 0b before binary value, prints at index 2 and onwards
