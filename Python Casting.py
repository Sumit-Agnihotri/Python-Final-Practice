print("Specify a Variable Type\nThere may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.\n\nCasting in python is therefore done using constructor functions:\n\n1-> int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)\n2-> float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)\n3-> str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals")
x=1
y=2
x,y=y,x
print(x)
print(y)