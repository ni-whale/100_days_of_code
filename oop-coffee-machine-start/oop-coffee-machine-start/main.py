from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1: Print report

coffee_machine = CoffeeMaker()


# TODO 2: Check resources sufficient

def resource_checking(users_choice):
    coffee = MenuItem(name=users_choice)
    # coff


# TODO 3: Process coins
# TODO 4: Transaction validation
# TODO 5: Making a coffee

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
            coffee_machine.report()
        else:
            the_report_chose = True
            if coffee_machine.is_resource_sufficient(choice):
                continue
                # print("Seems everything is fine")
            else:
                print(f"Sorry there is not enough {resource_checking(client_choice=choice)}.")
                taking_the_order()
    # end of validation choice part


# print(report.report())
taking_the_order()