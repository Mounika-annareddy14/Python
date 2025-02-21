"""
                DATATYPES:-
1. STRINGS
2.INTEGERS
3.FLOAT
4.BOOLEANS
"""

#Subscripting
print("Hello"[0])

#string
print("123" + "456") #concatenation

# whole numbers = Integers
print(123 + 456)

# Large integers
print(123_456_789)

#Float = floating number point
print(13.56)

#boolean
print(True)
print(False)

"""
Type Errors:
These error occurs when you are using the wrong data type eg:len(12345)
Because you can only give the len() function strings.It will refuse to work
and give you a type error if you give it a number(integer)
"""
#len(123456)
"""
Fixing error in len function
"""
len("123")

"""
type checking
"""
print(type("1234"))

print(type("1234"))
print(type(1234))
print(type(12.3))
print(type(True))

"""
TYPE CONVERSIONS:
we can convert data into different data types using special functions:
eg:
str()
int()
float()
bool()
"""

print(int("123") + int("456"))
#print(int('abc'))

name_of_the_user = input("Enter you name")
length_of_name = len(name_of_the_user)

print(type(name_of_the_user))
print(type(length_of_name))

print("Number of letters in name:" + str(length_of_name))