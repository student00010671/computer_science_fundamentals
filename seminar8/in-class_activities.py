# Creating a tuple
t = 'a', 'b', 'c', 'd', 12.2

# To create a tuple with a single element use comma
t1 = 'a',
print(type(t1))  # prints <class 'tuple'>
t2 = 'a'
print(type(t2))  # prints <class 'str'>

# Another way to create a tuple
t3 = tuple()

t4 = tuple('westminster')
print(t4)  # prints ('w', 'e', 's', 't', 'm', 'i', 'n', 's', 't', 'e', 'r')


# Accessing a tuple value by using index
print(t4[2])  # prints s

# Accessing index by using tuple value
print(t4.index('s'))  # prints 2


# To select a range of values in a tuple use Slice operator
print(t4[0:4])  # prints ('w', 'e', 's', 't')


# Tuples are immutable
# t4[0] = 'A',  # TypeError: 'tuple' object does not support item assignment

# Create a new tuple instead
t5 = ('A',) + t4[1:]
print(t5)  # prints ('A', 'e', 's', 't', 'm', 'i', 'n', 's', 't', 'e', 'r')


# Relational operators and tuples
# Python firstly compares the first elements from each sequence. If they are equal, it goes on to the next elements
# and so on, until it finds elements that differ!

print((10, 3, 333) < (10, 4, 1))  # prints True
print((10, 3, 333) < (10, 1, 333))   # prints False
print((2, 3) == (2, 3))  # prints True
print((2, 3) == (3, 2))  # prints False


# To swap variables we can use this primitive technique
a = 3
b = 7

temp = a
a = b
b = temp

# Or we can use tuples for more conventional solution
a, b = b, a
print("a = " + str(a) + " b = " + str(b))  # prints ( a = 3 b = 7)  Remember we already swapped them above

# The number of variables and values must be equal on both sides
# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)

# Also the right side side can be any kind of sequence
address = 'info@wiut.uz'
uname, domain = address.split('@')
print(uname, domain)  # prints info wiut.uz


# Tuples and return values with divmod built-in function
# divmod function receives a dividend and a divisor and returns a tuple with a quotient and a remainder
t6 = divmod(7, 3)  # 7 is a divisor & 3 is a divisor
print(t6)  # prints (2, 1) where 2 is a quotient & 1 is a remainder

# if you want to store the quotient and the remainder use tuple assignments
qout, rem = divmod(7, 3)
print(qout)  # prints 2
print(rem)  # prints 1


# Variable-length argument tuples
# use * to gather all arguments of a tuple to the parameter of the function
def printall(*args):  # args is preferred name of the parameter
    print(args)


printall(1, 2.2, '3', True)  # prints (1, 2.2, '3', True)


# zip built-in function
s = "abc"
t7 = [0, 1, 2]
zip(s, t)  # zip knows gow to iterate through the pairs

# zip is commonly used in for loop
for pair in zip(s, t7):
    print(pair)

# prints
# ('a', 0)
# ('b', 1)
# ('c', 2)

# zip object is a kind of iterator, which iterates through a sequence
# Unlike lists, you can't use an index to select an element from an iterator


# However, if you want to use list operators and methods, you can use a zip object ot make a list
t8 = list(zip(s, t7))
print(t8)  # prints [('a', 0), ('b', 1), ('c', 2)]

for letter, number in t8:
    print(number, letter)

# prints
# 0 a
# 1 b
# 2 c


# the function below checks if the elements with the same indexes in the list matches
# and it will return true if at least there is one match
def has_match(list1, list2):
    for x, y in zip(list1, list2):
        if x == y:
            return True
    return False


t9 = [1, ('b', 1)]
print(has_match(t8, t9))  # prints True


# enumerate built in function
#

# enumerate with a string
for index, element in enumerate('abc'):
    print(index, element)

# prints
# 0 a
# 1 b
# 2 c


# enumerate with tuple
t10 = ('A', 'B', 'C', 'D', 'E')
for i in enumerate(t10):
    print(i)

# prints
# (0, 'A')
# (1, 'B')
# (2, 'C')
# (3, 'D')
# (4, 'E')


# Dictionaries and tuples
# dictionaries have a method called items that returns a sequence of tuples, where each tuple is a key-valuer pair
d1 = {'a': 0, 'b': 1, 'c': 2}
t11 = d1.items()
print(t11)  # prints  dict_items([('a', 0), ('b', 1), ('c', 2)])

# can be used in a for loop also
for key, value in d1.items():
    print(key, value)

# prints
# a 0
# b 1
# c 2


# You can use a list of tuples to initialize a new dictionary (vice versa)
d2 = dict(t11)
print(d2)  # prints {'a': 0, 'b': 1, 'c': 2}


# Combining dict with zip yields a concise way to create a dictionary
d3 = dict(zip('efg', range(3)))
print(d3)  # prints {'e': 0, 'f': 1, 'g': 2}
