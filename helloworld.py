print("Hello World!")
print("How are you?")

print("---------------------------")

if 5>2:
	print("Five is greater than 2")
if 10>2:
	print("Ten is greater than two!")

print("---------------------------")

first_name = "Troy"
last_name = "Baker"
age = 20

print(first_name)
print(last_name)
print(age)

""" multi-line comment here
Print("Testing")
Print("Testing")
Print(Testing")
""" #multi-line comment ends

print("---------------------------")

print("I will now rename the first_name variable")

first_name = "Simon"
print(first_name)

print("I will now rename the first_name variable again")
first_name = "Tony"
print(first_name)
print("I will now change the first_name variable type to an integer")
first_name = 9865.456
print(first_name)

print("---------------------------") #print("The End!")

print("VARIABLES")
#Casting - specify the data type
x = int(3)
y = str(3)
z = float(3)
print(x) 
print(y)
print(z)

print("---------------------------")

print(type(first_name))
print(type(last_name))
print(type(age))

print("---------------------------")

#Quotes ('') or ("")
name_1 = 'James'
name_2 = "James"
print(type(name_1))
print(type(name_2))
print(name_1)
print(name_2)

print("---------------------------")
#variable names are case sensitive
NAME_1 = "John"
NAME_2 = 'Marcus'

print(name_1)
print(NAME_1)
print(name_2)
print(NAME_2)
print(type(NAME_2))

print("---------------------------")

#variable names
print("camelCase")
print("PascalCase")
print("snake_case")

print("---------------------------")

#Many values to multiple variables
a, b, c = "apple", "banana", "cherry"
print(a)
print(b)
print(c)
#1 value to multiple variables
x = y = z = "Lilac"
print(x)
print(y)
print(z)
#unpacking: many values to variables
primary_colours = ["red", "yellow", "blue"]
r, y, b = primary_colours
print(r)
print(y)
print(b)