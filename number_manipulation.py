"""
Flooring  a Number
we can floor a number or remove all decimal points using the int()  function which converts a floating point number (with deciaml
places) into an integer (whole number).
"""

print(int(3.77895))

"""
Rounding a number
However if you want to round a decimal number to the nearest whole number using the 
traditional mathematical way where anything over .5 rounds up and anything below rounds down
then u can use the round() function
"""
print(round(3.77895))
print(round(3.77895,2))

"""
Assignment operators
Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the 
variable on the left and assign the new value  to the variable.
+=
-=
*=
/=
"""
score = 0
score +=1
print(score)

"""
f-Strings
In python , We can use f-strings to insert a variable or an expression into a string
"""
score = 1
height = 1.67
is_winning = True

print(f"Your score is  {score} , your height is {height} and your winning chance is {is_winning}")