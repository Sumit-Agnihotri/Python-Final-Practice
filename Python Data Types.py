print("PYTHON DATA TYPES")
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# How to find the data type of a variable
x=50
y="Sumit"
z=True
print(type(x))
print(type(y))
print(type(z))

# Text Type
text_example = "Hello, World!"
print(type(text_example), text_example)

# Numeric Types
int_example = 10
print(type(int_example), int_example)

float_example = 10.5
print(type(float_example), float_example)

complex_example = 1 + 2j
print(type(complex_example), complex_example)

# Sequence Types
list_example = [1, 2, 3]
print(type(list_example), list_example)

tuple_example = (1, 2, 3)
print(type(tuple_example), tuple_example)

range_example = range(5)
print(type(range_example), list(range_example))

# Mapping Type
dict_example = {"name": "Alice", "age": 25}
print(type(dict_example), dict_example)

# Set Types
set_example = {1, 2, 3}
print(type(set_example), set_example)

frozenset_example = frozenset({1, 2, 3})
print(type(frozenset_example), frozenset_example)

# Boolean Type
bool_example = False
print(type(bool_example), bool_example)

# Binary Types
bytes_example = b"Hello"
print(type(bytes_example), bytes_example)

bytearray_example = bytearray(5)
print(type(bytearray_example), bytearray_example)

memoryview_example = memoryview(bytes(5))
print(type(memoryview_example), memoryview_example)

# None Type
none_example = None
print(type(none_example), none_example)



# Commonly asked data types in interviews

# String
string_example = "Interview"
print(type(string_example), string_example)

# Integer
integer_example = 42
print(type(integer_example), integer_example)

# Float
float_example = 3.14
print(type(float_example), float_example)

# List
list_example = [1, 2, 3, 4, 5]
print(type(list_example), list_example)

# Dictionary
dict_example = {"key": "value"}
print(type(dict_example), dict_example)

# Tuple
tuple_example = (1, 2, 3)
print(type(tuple_example), tuple_example)

# Set
set_example = {1, 2, 3}
print(type(set_example), set_example)

# Boolean
boolean_example = True
print(type(boolean_example), boolean_example)