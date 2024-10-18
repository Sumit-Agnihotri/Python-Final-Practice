# PYTHON BOOLEANS
# Booleans represent one of two values: True or False.
# Boolean Values
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
print(10>9)
print(10<9)
print(10==9)
# When you run a condition in an if statement, Python returns True or False:
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
# Example
print(bool("Hello"))
print(bool(15))

# These will always return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# These will always return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})