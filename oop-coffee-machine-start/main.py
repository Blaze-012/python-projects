from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def report():

    coffee_maker.report()
    money_machine.report()


switch = True
while switch:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        switch = False
    elif choice == "report":
        report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)