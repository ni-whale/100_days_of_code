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

# num1 = int(input("What's the first number?: "))
# num2 = int(input("What's the second number?: "))
#
# for symbol in operations:
#     print(symbol)
# operation_symbol = input("Pick an operation from the line above: ")

# function = operations[operation_symbol]
# answer = function(n1=num1, n2=num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")
# condition = True
# while condition:
#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
#         operation_symbol = input("Pick an another operation: ")
#         num3 = int(input("What is the next number?: "))
#         function = operations[operation_symbol]
#         next_answer = function(answer, num3)
#         print(f"{answer} {operation_symbol} {num3} = {next_answer}")
#         answer = next_answer
#     else:
#         print("Good bye!")
#         condition = False

num1 = int(input("What's the first number?: "))


for symbol in operations:
    print(symbol)
should_continue = True
symbol_check = True

while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    function = operations[operation_symbol]
    answer = function(n1=num1, n2=num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
        num1 = answer
    else:
        print("Good buy")
        should_continue = False

















