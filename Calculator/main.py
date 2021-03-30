# Add
def add(n1, n2):
    """Summarise 2 different digits"""
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

function = operations[operation_symbol]
first_answer = function(n1=num1, n2=num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")
condition = True
while condition:
    the_next_action = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit: ")
    if the_next_action == 'y':
        operation_symbol = input("Pick an another operation: ")
        num3 = int(input("What is the next number?: "))
        function = operations[operation_symbol]
        second_answer = function(first_answer, num3)
        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        first_answer = second_answer
    else:
        print("Good bye!")
        condition = False







