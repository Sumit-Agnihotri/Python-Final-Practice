print("Hello") # Output: Hello
print('Hello') # Output: Hello
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# Quote inside Quotes
print("It's alright!") # Output: It's alright!
print("'Sumit' and 'Ruby' are friends") # It's a single quote inside double quotes.
print('"Sumit" and "Ruby" are friends') # It's a double quote inside single quotes.

# Multi-line Strings
print("""Sumit and Ruby are friends.
      They are best friends.""") # Output: Sumit and Ruby are friends.
print('''Sumit and Ruby are friends.
      They are best friends.''') # Output: Sumit and Ruby are friends.

# Strings are Arrays
a="Hello, World!"
print(a[1]) # Output: e

# Looping through a String
for x in "banana":
      print(x) # Output: b a n a n a
      
# String Length
a="Hello, World!"
print(len(a)) # Output: 13

# Check String
txt="The best things in life are free!"
print("free" in txt) # Output: True, it checks if the specified value is present in the string.