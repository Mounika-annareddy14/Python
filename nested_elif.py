print("Welcome to the Rollercoaster!")
height = int(input("What was your height?"))

if height >=120:
    print("You can ride Happily❤️😊")
    age=int(input("Enter you age"))
    if age <= 12:
        print("please pay 5$💰")
    elif age <= 18:
        print("Please pay 7$💰")
    else:
        print("please pay 12$💰")

        print("Credited!Now you can go for a ride")
else:
    print("Sorry!❤️😒You want to grow taller before you can ride")


weight = 85
height = 1.85
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi > 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")