print("Welcome to pizza order deliveries!🍕🍕😜")
size = input("What size of the pizza do you want S , M , L ?")
pepperoni = input("Do you want pepperoni Y or N?")
extRa_cheese = input("do you want extra cheese y or n")

bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print('please Enter correct input formats!')

if pepperoni =='Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extRa_cheese == 'y':
    bill += 1

print("Thanks for ordering🍕❤️")
print(f"Your final bill is {bill}$💰")
print("Please Visit Again❤️🫂")
