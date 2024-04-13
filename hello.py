print("Hello world!") # hello world
print("printing stuff")

# variables - str, int, float and bools
name = "jonnathan moore"
print(name)
print("Hello " + name)
print(type(name)) # checks and prints the type
age = 22
age += 1
print(age)
print(type(age))

#typecasting
print("Your age is " + str(age))
print("Your height is " + str(250.5))

# multiple assignment
Spongebob, Patrick, Sandy = 25, 30, 35
print("Spongebob, Patrick and Sandy's age: " + str(Spongebob) + str(Patrick) + str(Sandy))

# string methods
print(len(name))
print(name.find("M")) # find the index, remember it's zero indexed
print(name.capitalize())
print(name)
print(name.upper())
nameandnum = ""
print(nameandnum.isdigit()) # can only contain digits
print(nameandnum.isalpha()) # can only contain letters of alphabet
print(nameandnum.isalnum()) #can contain either or both to be true but not if empty
print(name.count("m")) # case sensitive, count how many of that value there is in the variable
first_name = name[0:9]
print(first_name)
reversed_name = first_name[::-1]
print(reversed_name)
