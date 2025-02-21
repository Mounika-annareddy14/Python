print("Welcome to the Treasure Island")
print("Our Mission is to find the treasure")

choice1 = input("You're at cross road , where do you want to go? type 'left' or 'right'.\n").lower()
if choice1 == 'left':
    choice2 = input('you \'ve come to a lake.There is an island in the middle of the lake.'
                    'Type "wait" to wait for a boat.'
                    'Type "swim" to swim across\n').lower()
    if choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed."
                        "there is house with 3 doors. One red ,"
                        "one yellow and one blue"
                        "Which color do you want to choose?\n").lower()
        if choice3 == 'red':
            print("Room is full of red fire🔥!Game Over")
        elif choice3 == 'yellow':
            print("You found the treasure❤️!You win the Game🎯🏆")
        elif choice3 == 'blue':
            print('Room is filled with beasts!Game Over')
        else:
            print("You choose a door that does not exist.Game Over")


    else:
        print("You got attacked by an angry trout😒!Game over")
else:
    print("You fell into a hole.Game Over😒")

