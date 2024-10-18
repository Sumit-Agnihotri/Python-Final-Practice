a="hello"
# capitalize() Capitalizes the first letter of a string
print(a.capitalize())
# casefold() Converts string into lower case
print(a.casefold())
# center() Returns a centered string
print(a.center(20))
# count() Returns the number of times a specified value occurs in a string
print(a.count("l"))
# encode() Returns an encoded version of the string
print(a.encode())
# startswwith() Returns true if the string starts with the specified value
print(a.startswith("h"))
# endswith() Returns true if the string ends with the specified value
print(a.endswith("o"))
# expandtabs() Sets the tab size of the string
print(a.expandtabs(2))
# find() Searches the string for a specified value and returns the position of where it was found
print(a.find("l"))
# upper() Converts a string into upper case
print(a.upper())
# lower() Converts a string into lower case
print(a.lower())
# title() Converts the first character of each word to upper case
print(a.title())
# swapcase() Swaps cases, lower case becomes upper case and vice versa
print(a.swapcase())
# strip() Removes any whitespace from the beginning or the end
print(a.strip())
# rstrip() Removes any whitespace from the end
print(a.rstrip())
# lstrip() Removes any whitespace from the beginning
print(a.lstrip())
# replace() Returns a string where a specified value is replaced with a specified value
print(a.replace("h","j"))
# partition() Returns a tuple where the string is parted into three parts
print(a.partition("l"))
# rpartition() Returns a tuple where the string is parted into three parts
print(a.rpartition("l"))
# split() Splits the string at the specified separator, and returns a list
print(a.split("l"))
# rsplit() Splits the string at the specified separator, and returns a list
print(a.rsplit("l"))
# splitlines() Splits the string at line breaks and returns a list
print(a.splitlines())
# isspace() Returns True if all characters in the string are whitespaces
print(a.isspace())
# isalpha() Returns True if all characters in the string are in the alphabet
print(a.isalpha())
# isalnum() Returns True if all characters in the string are alphanumeric
print(a.isalnum())
# isdecimal() Returns True if all characters in the string are decimals
print(a.isdecimal())
# isdigit() Returns True if all characters in the string are digits
print(a.isdigit())
# isidentifier() Returns True if the string is an identifier
print(a.isidentifier())
# islower() Returns True if all characters in the string are lower case
print(a.islower())
# isupper() Returns True if all characters in the string are upper case
print(a.isupper())  
# istitle() Returns True if the string follows the rules of a title
print(a.istitle())
# join() Joins the elements of an iterable to the end of the string
print(a.join("world"))
# ljust() Returns a left justified version of the string
print(a.ljust(10))
