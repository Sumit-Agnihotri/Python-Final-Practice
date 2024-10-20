# PYTHON LISTS
print("Lists are used to store multiple items in a single variable.")
print("Lists are one of 4 built-in data types in Python used to store collections of data\n, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.")
# Lists are mutable, meaning that the elements inside a list can be changed!

# Creating a List
fruits = ["apple", "banana", "cherry"]
print(fruits)

# We can put duplicate values in a list
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruits)

# List Length
print(len(fruits))

# List Data Types
mixed_list = ["apple", "banana", "cherry", 1, 2, 3]
print(type(mixed_list))

# The list() Constructor
fruits = list(("apple", "banana", "cherry")) # note the double round-brackets