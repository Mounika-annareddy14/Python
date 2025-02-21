"""
Learn to store values in containers for later use.Variables is a concept in programming that allows us to give a label
to a piece of data so that we can refer or reference that data using the chosen variable name.
"""
name = input("Enter your name?")
print(name)

#checking the length of user input
name = input("Enter a your Name?")
print(name)
print(len(name))

glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp
print(glass1)
print(glass2)

"""
       VARIABLE NAMING:
Learn the rules of variable naming
Make sure your variable names are descriptive
Dont have spaces between words
Dont use special words like print or input

"""