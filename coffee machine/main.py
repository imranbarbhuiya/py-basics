from os import system

from coffee_data import MENU, resources

is_on = True
profit = 0


def is_resource_sufficient(order_ingredients):
    """Checks if the coffee machine has enough resources to make the order"""
    for ingredient in order_ingredients:
        if resources[ingredient] < order_ingredients[ingredient]:
            print(f"Sorry, we don't have enough {ingredient}")
            return False
    return True


def process_coin():
    """Returns the amount of money inserted by the user"""
    print("Please insert coin")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successfull(money_received, cost_of_coffee):
    """Returns True if the transaction was successful, False otherwise"""
    if money_received >= cost_of_coffee:
        change = round(money_received - cost_of_coffee, 2)
        print(f"Here is ${change} change")
        global profit
        profit += cost_of_coffee
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredient from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name} ☕")


while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "off":
        print("​Goodbye")
        is_on = False
    elif choice == "report":
        print("Current resource values are: ")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successfull(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
