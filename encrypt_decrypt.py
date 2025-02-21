"""
letters = ['a' , 'b' , 'c' ,'d' ,'e' ,'f' , 'g' , 'h', 'i', 'j', 'k','l','m' ,'n', 'o' , 'p' ,'q', 'r', 's', 't','u','v', 'w', 'x', 'y','z']

direction = input("Type encode for encrypt and decode for decrypt?\n").lower()
text = input('Enter a message \n').lower()
shift_number = int(input('enter how number do you want to shift \n'))

#TODO 1 Create function called 'encrypt()' that takes 'original text' and 'shift amount' as 2 inputs
#TODO 2 Inside the encrypt() function , shift each letter of the 'original_text' forwards in the alphabet
#by the shift amount and print the encrypted text
def encrypt(original_text , shift_amount):
    cipher_text = ''
    for letter in original_text:
        shifted_position =letters.index(letter) + shift_amount

        shifted_position %= len(letters) # to maintain range in 0 to 25
        cipher_text+=letters[shifted_position]

    print(f'Here is the encoded result {cipher_text}')

#TODO 4 What happens if you try to shift z forwards by 9? can you fix the code?

#TODO 3 Call the encrypt() function and pass in the user inputs you should be able to test the code and encrypt a message
encrypt(text , shift_number)



DECODE

direction = input("Type encode for encrypt and decode for decrypt?\n").lower()
text = input('Enter a message \n').lower()
shift_number = int(input('enter how number do you want to shift \n'))

def decrypt(original_text , shift_amount):
    cipher_text1 = ''
    for letter  in original_text:
        shifted_position = letters.index(letter) - shift_amount
        shifted_position %= len(letters)
        cipher_text1+=letters[shifted_position]

    print(f'here is decoded result {cipher_text1}')

decrypt(text , shift_number)
"""




















"""
CAESAR PHAR CODE
"""

letters = ['a' , 'b' , 'c' ,'d' ,'e' ,'f' , 'g' , 'h', 'i', 'j', 'k','l','m' ,'n', 'o' , 'p' ,'q', 'r', 's', 't','u','v', 'w', 'x', 'y','z']

direction = input("Type encode for encrypt and decode for decrypt?\n").lower()
text = input('Enter a message \n').lower()
shift_number = int(input('enter how number do you want to shift \n'))

def caesar(original_text , shift_amount , encode_or_decode):
    output_text = ""
    for letter in original_text:
        if encode_or_decode == 'decode':
            shift_amount *= -1
        shifted_position = letters.index(letter) + shift_amount
        shifted_position %= len(letters)
        output_text+=letters[shifted_position]
    print(f'here is your {encode_or_decode}d result {output_text}')
caesar(text , shift_number , direction)
