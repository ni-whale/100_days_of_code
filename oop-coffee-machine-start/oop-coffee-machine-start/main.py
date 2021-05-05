from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1: Print report
coffee_machine = CoffeeMaker()


# TODO 2: Check resources sufficient
coffee = Menu()


# TODO 3: Process coins
money = MoneyMachine()

# TODO 4: Transaction validation
# TODO 5: Making a coffee

def off():
    exit()


def taking_the_order():
    input_error = True
    the_report_chose = False
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
            coffee_machine.report()
            money.report()
            taking_the_order()
        else:
            coffee_machine.is_resource_sufficient(coffee.find_drink(choice))
            # taking_the_order()
            # inserted_money = money.process_coins()
            # if money.make_payment(money.process_coins()):
            #     print("seems fine")
            #     coffee_machine.make_coffee(coffee.find_drink(choice))
            print(money.make_payment(money.process_coins()))

taking_the_order()
