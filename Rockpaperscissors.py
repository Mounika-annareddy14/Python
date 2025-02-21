import random
print("Welcome to the ROCK PAPER SCISSORS GAME")
user_choice = int(input("What do you choose Type 0 for Rock  1 for paper 2 for scissors?\n"))

computer_choice = random.randint(0,2)
print(f"Computer choice {computer_choice}")

if user_choice>= 3 or user_choice < 0:
    print("It is an invalid number. You lose!")
elif user_choice ==0 and computer_choice==2:
    print("You Wins🏆")
elif user_choice > computer_choice:
    print("you Wins!")
elif computer_choice > user_choice:
    print("you lose!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")


