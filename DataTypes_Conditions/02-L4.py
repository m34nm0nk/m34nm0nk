# construct interactive script that returns which service
# is associated with specific port number

ProtocolDict = {'FTP':'21', 'DNS':'53', 'LDAP':'389', 'MySQL':'3306', 'HTTP':'80'}

# variable to ask user which port being used
question = input("For which protocol would you like to know the port number?: ")

# condition to check if the value in 'question' variable exists in dict
if question in ProtocolDict.keys():
# select a value from dict with the question variable as a key
    answer = ProtocolDict[question]
    print('The protocol number for protocol ' + question + ' is ' + answer + '!')
else:
    print('The protocol cannot be found')
