# use the following data structure that contains a dictionary and
# a list to practice value extraction
# [{'Arizona': 'Phoenix', 'California': 'Sacramento',
# 'Hawaii':'Honolulu'},5000,6000,7000,['hat', 't-shirt', 'jeans']]

structure = [{'Arizona': 'Phoenix', 'California': 'Sacramento', 'Hawaii': 'Honolulu'},5000,6000,7000,['hat', 't-shirt', 'jeans']]
# dictionary of state/cities=[0]; 5000=[1]; 6000=[2]; 7000[3]; clothes=[4]

# print 5000 by extracting it from the variable
print(structure[1:4])
# print dictionary of states and cities from the variable
print(structure[0])
# print list of clothes from the variable
print(structure[4])
# print the word 'Pheonix' from the variable
print(structure[0]['Arizona'])
# print the word 'jeans' from the variable
print(structure[4][2])
# delete the value '7000' using del(), print new data
del(structure[3])
print(structure)
# append 'new value' to list using append(), print new data
structure.append('new value')
print(structure)
# append element to dictionary
structure[0]['Maryland'] = 'Baltimore'
print(structure)
# append new element clothes list
structure[3].append('shorts')
print(structure)
