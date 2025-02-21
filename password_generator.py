import random
letters = ['a','b' , 'c' , 'd' ,'e' , 'f' , 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!' ,'#','$' , '%' ,'&' , '(' ,')', '*' ,'+' ,'@']

print("Welcome to password Generator")
nr_letters = int(input('Number of letters do you like in your Password?\n'))
nr_numbers = int(input("Number of numbers do you like in your Passwords?\n"))
nr_symbols = int(input("Number of symbols do you like in your password?\n"))
"""
General Password
"""
# password = " "
#
# for i in range(0,nr_letters):
#     password+=random.choice(letters)
#
# for i in range(0,nr_numbers):
#     password+=random.choice(numbers)
#
# for i in range(0,nr_symbols):
#     password+=random.choice(symbols)
#
# print(password)
"""
Strong password
"""
password_list =  []
for i in range(0,nr_letters):
    password_list.append(random.choice(letters))

for i in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

for i in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

#joining
password = ""
for char in password_list:
    password += char
print(password)
