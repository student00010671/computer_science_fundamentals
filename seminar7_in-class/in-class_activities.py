# Creating an empty dictionary
eng2uz = dict()
print(eng2uz)   # prints {}


# Adding items
eng2uz['one'] = 'bir'
print(eng2uz)   # prints {'one': 'bir'}

# Creating new dictionary
eng2uz = {'one': 'bir', 'two': 'ikki', 'three': 'uch'}
print(eng2uz)   # prints {'one': 'bir', 'two': 'ikki', 'three': 'uch'}

# Retrieving keys from dictionary
print(eng2uz['two'])   # Returns ikki

# Boolean logic in dictionary using 'in' operator
print('one' in eng2uz)   # Returns True
print('uno' in eng2uz)   # Returns False
