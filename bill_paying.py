import random

friends = ["mounika" , "jahnifar" ,"Alex" ,'python']

#option 1
print(random.choice(friends))

#option2
random_index = random.randint(0,4)
print(friends[random_index])