from data import MENU, resources
current_resources = resources


# TODO: 1. Printing of the report with the current value of available ingredients & earned money.


def report():
    current_resources["money"] = 0
    print(f"Water: {current_resources['water']}")
    print(f"Milk: {current_resources['milk']}")
    print(f"Coffee: {current_resources['coffee']}")
    print(f"Money: {current_resources['money']}")


# TODO: 2. Check if resources are sufficient.

def resource_checking(client_choice):
    print(MENU["latte"]["ingredients"])


# TODO: 3. Processing of coins.

# TODO: 4. Checking if the transaction was successful.

# TODO: 5. Making a coffee.


def taking_the_order():
    input_error = True
    while input_error:
        try:
            choice = input("What would you like? (espresso/latte/cappuccino): ")
            if choice == "espresso" or choice == "latte" or choice == "cappuccino":
                break
        except NameError("espresso", "latte", "cappuccino"):  # Not sure which exception should be there to print the result. Need to google it.
            print("Oops! That was not valid input. Try again...")
    if resource_checking(client_choice=choice) == 'ok':
        ...
    else:
        print(f"Sorry there is not enough {resource_checking(client_choice=choice)}")


# taking_the_order()

