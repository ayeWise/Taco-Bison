from urllib.parse import uses_relative


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

#TODO 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
#TODO 2. Turn off the Coffee Machine by entering "off" to the prompt.
#TODO 3. Print a report
#TODO 4. Check resources sufficient?
#TODO 5. Process coins.
#TODO 6. Check transaction successful?
#TODO 7. Make Coffee.

profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns True when oreders can be made, False when orders are insufficient"""

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    """Returns the total calculated from coins inserted"""

    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!☕")

is_on = True

while is_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
         drink = MENU[user_choice]
         if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])