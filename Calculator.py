def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multipy(n1 , n2):
    return n1 * n2

def division(n1 , n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multipy,
    "/":division
}

def calculator():
    should_accumulate = True
    num1 = float(input('what is your first number?'))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation:")
        num2 = float(input("What is the next number"))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} ={answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} , or type 'n' for new calculation")

        if choice =="y":
            num1 = answer
        else:
                should_accumulate = False
                print('\n'*20)
                calculator()
calculator()