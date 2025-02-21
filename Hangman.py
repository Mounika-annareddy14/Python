# HANGMAN GAME:
import random
word_list = ['Mango' , 'apple' , 'camel']
lives = 6

# TODO1: Randomly chose a word from a word_list and assign it to a variable called chosen_word.Then print it.
chosen_word = random.choice(word_list)

# Todo2: Ask the user to guess a letter and assign their answer to a variable called guess. and lower
# guess = input('Guess a Letter: ').lower()
#
# # TODO3: check if the letter the user guessed (guess) is one of the letters in the chosen_word.print Right if the
# # guessed letter is right else print wrong
# for letter in chosen_word:
#     if guess == letter:
#         print('Right')
#     else:
#         print('Wrong')



#create a placeholder with same number of blanks as the chosen word
placeholder = ''
word_len = len(chosen_word)
for i in range(word_len):
    placeholder += "-"


# guess = input('Guess a Letter: ').lower()
#
# #create  a display to place a guess letter in the right position and _ in wrong position
# display = ''
# for letter in chosen_word:
#     if letter == guess:
#         display+=letter
#     else:
#         display+='-'


#while loop
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: \n").lower()

    if guess in correct_letters:
        print(f'You have already guessed a {guess}')
    display = ''
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display +='-'
    print(display)

    if guess not in chosen_word:
            lives  -=1
            print(f"you guessed {guess} not in chosen word so you lost a lives .you have remaining {lives} lives")
            if lives ==0:
                game_over = True
                print('You lose')

    if '-' not in display:
        game_over = True
        print("you win")
