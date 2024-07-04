MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# TODO: 1. ask for a prompt from user.... latte/espresso/cappuccino.
def prompt():
    """Asks the user for input and returns the user-input."""
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    return user_input


# TODO: 2. report - prints the resources along with money the machine has.
def report():
    print(f" Water: {resources['water']}ml ")
    print(f" Milk: {resources['milk']}ml ")
    print(f" Coffee: {resources['coffee']}gm ")
    print(f" Money: ${resources['money']} ")


# TODO: 3. check resources sufficient?
def check(response):
    """Takes a drink as input.Checks whether the resources are sufficient and returns boolean and a string in a list."""
    is_sufficient = [True, ""]
    if resources["water"] < MENU[response]['ingredients']['water']:
        is_sufficient[0] = False
        is_sufficient[1] = "water"
    if resources["milk"] < MENU[response]['ingredients']['milk']:
        is_sufficient[0] = False
        is_sufficient[1] = "milk"
    if resources["coffee"] < MENU[response]['ingredients']['coffee']:
        is_sufficient[0] = False
        is_sufficient[1] = "coffee"
    return is_sufficient


# TODO: 4. process coins
def coins():
    """Asks to insert coins. Processes and returns the total money in $"""
    print("Please insert coins.")
    q = int(input("How many Quarters: "))
    d = int(input("How many Dimes: "))
    n = int(input("How many Nickels: "))
    p = int(input("How many Pennies: "))
    total_money = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    return total_money


# TODO: 5. check transaction successful?
def transaction(response):
    user_money = coins()
    money_required = MENU[response]['cost']
    change = round(user_money - money_required, 2)
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here's ${change} in change.")
        print(f"Here's your {response} ☕. Enjoy!")
        resources["milk"] -= MENU[response]["ingredients"]["milk"]
        resources["water"] -= MENU[response]["ingredients"]["milk"]
        resources["coffee"] -= MENU[response]["ingredients"]["coffee"]
        resources["money"] += MENU[response]["cost"]


# TODO: 6. Make coffee
def make_coffee():
    switch = True
    while switch:
        user_input = prompt()
        if user_input == "off":
            switch = False
        elif user_input == "report":
            report()
        else:
            sufficient = check(user_input)
            if not sufficient[0]:
                print(f"Sorry there is not enough {sufficient[1]}")
            else:
                transaction(user_input)


make_coffee()