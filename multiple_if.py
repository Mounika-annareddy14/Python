print("Welcome To the Rollercoaster!")
height = int(input("What is your height?"))
if height >=120:
    print("You can Ride Happily❤️😊")

    age = int(input("What was your age?"))
    if age <= 12:
        bill = 5
        print("child ticket 5$💰")
    elif age <= 18:
        bill = 7
        print("youth ticket 7$💰")
    elif age>=45 and age<=55:
        print("Everything is going to be ok!have a free ride❤️")
    else:
        bill = 12
        print("older ticket 12$💰")
    want_photo = input("did you want to take a photo while ride y for yes and n for no?")
    if want_photo == 'y':
        bill+=3
    print(f"your final bill is {bill}$💰")
else:
    print("sorry!you want to grow taller before you ride❤️😒")