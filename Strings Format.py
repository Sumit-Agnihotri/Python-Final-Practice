age = 20
name = "Sumit"
print("My name is "+ name +" and I am "+ str(age) +" years old.")
print("My name is",name,"and I am ",age,"years old.\n")

# F-Strings

print("F-Strings\n")
age = 20
name = "Sumit"
print(f"My name is {name} and I am {age} years old.")

# Placeholders and Modifiers

print("\nPlaceholders and Modifiers\n")
price=100
txt = "The price is {:.2f} dollars"
print(txt.format(price))

print("This price is ${20*5} dollars!")