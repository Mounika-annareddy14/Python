def title_(f_name , l_name):
    formatted_f = f_name.title()
    formatted_l = l_name.title()
    return f"{formatted_f} {formatted_l}"
    #print(f"{formatted_f} {formatted_l}")

print(title_('MounIKa' , 'AnnaRedDY'))


def function(text):
    return text + text

def function1(text):
    return text.title()

print(function1(function('hello')))


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(add(2, multiply(5, divide(8, 4))))




