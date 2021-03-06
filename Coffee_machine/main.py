from data import MENU, resources

current_resources = resources
current_resources['money'] = 0


# TODO: 1. Printing of the report with the current value of available ingredients & earned money.

def report():
    print(f"Water: {current_resources['water']}")
    print(f"Milk: {current_resources['milk']}")
    print(f"Coffee: {current_resources['coffee']}")
    print(f"Money: ${current_resources['money']}")


# TODO: 2. Check if resources are sufficient.

def resource_checking(client_choice):
    if client_choice == "report":
        return "report"
    for item in MENU[client_choice]["ingredients"]:
        if current_resources[item] - MENU[client_choice]["ingredients"][item] <= 0:
            return item
        else:
            current_resources[item] = current_resources[item] - MENU[client_choice]["ingredients"][item]
    return "OK"


# TODO: 3. Processing of coins.

def coins_checking(inserted_coins):
    sum_of_inserted_coins = inserted_coins["quarters"] * 0.25 + inserted_coins["dimes"] * 0.10 + \
                            inserted_coins["nickles"] * 0.05 + inserted_coins["pennies"] * 0.01
    return sum_of_inserted_coins


def coins_input_validation(coin):
    while True:
        try:
            user_input = int(input(f"How many {coin}: "))
            return user_input
        except ValueError:
            print("Oops! That was no valid number. Try again...")


# TODO: 4. Checking if the transaction was successful.

def transaction_checking(inserted_coins, users_choice):
    if inserted_coins < MENU[users_choice]["cost"]:
        return "not OK"
    elif inserted_coins > MENU[users_choice]["cost"]:
        change = inserted_coins - MENU[users_choice]["cost"]
        current_resources['money'] += MENU[users_choice]["cost"]
        return round(change, 2)
    else:
        current_resources['money'] += inserted_coins


# TODO: 5. Making a coffee.

def off():
    exit()


def taking_the_order():
    input_error = True
    the_report_chose = False
    # validation of the user's choice
    while not the_report_chose:
        while input_error:
            try:
                choice = input("What would you like? (espresso/latte/cappuccino): ")
                if choice == "espresso" or choice == "latte" or choice == "cappuccino" or choice == "report" \
                        or choice == "off":
                    break
            except NameError():  # Not sure which exception should be there to print the result. Need to google it.
                print("Oops! That was not valid input. Try again...")
        if choice == "off":
            off()
        elif choice == "report":
            report()
        else:
            the_report_chose = True
            if resource_checking(client_choice=choice) == 'OK':
                continue
                # print("Seems everything is fine")
            else:
                print(f"Sorry there is not enough {resource_checking(client_choice=choice)}.")
                taking_the_order()
    # end of validation choice part

    # checking if money is sufficient
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0,
    }
    print("Please insert the coins:")
    for coin in coins:
        coins[coin] = coins_input_validation(coin)
    # print(coins_checking(inserted_coins=coins))
    transaction = transaction_checking(inserted_coins=coins_checking(inserted_coins=coins), users_choice=choice)
    if transaction == "not OK":
        print("Sorry that's not enough money. Money refunded.")
    elif isinstance(transaction, float):
        print(f"Here is your change. ${transaction}")
    else:
        print(f"Enjoy your {choice}!")

    taking_the_order()


taking_the_order()


