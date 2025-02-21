"""
Functions:
A function in its simplest form is just a wrapper name for a
block of code.You give it name and then when you call the function
by that name,all the code within the function block will be executed.
It can help us save time and reduce repeated code.
"""
"""
the loop continuous working while particular condition is true
"""

"""
INPUT FUNCTIONS
"""
def greet_with(name,location):
    print(f"hey {name}❤️")
    print(f"Where are you from? I am from  {location}🎯")

greet_with('mounika' , 'hyderabad')   # positional argument

def greet_with(name , location):
    print(f"hey {name}❤️")
    print(f"Where are you from? I am from  {location}🎯")
greet_with(name = 'Mounika' , location = 'hyderabad')      # keyword arguments



def weeks_in_life(age):
    weeks_left = (90-age) * 52  # per year we have total 52 weeks
    print(f'You have {weeks_left} weeks left')
    #return weeks_left
weeks_in_life(12)


"""
LOVE CALCULATOR
"""
def calculate_love(name1 ,  name2):
    a='TRUE'
    b='LOVE'

    name1 = name1.upper()
    name2 = name1.upper()

    count_true = 0
    for i in name1 + name2:
        if i in a:
            count_true+=1

    count_love = 0
    for i in name1 + name2:
        if i in b:
            count_love+=1

    love_score = print(int(f'{count_true}{count_love}'))
    return love_score

calculate_love('mounika','python')





