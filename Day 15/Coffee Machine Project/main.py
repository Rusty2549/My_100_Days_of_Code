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
def gather_coins():
    print("please insert coins")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total
def is_resource_sufficient(drink, res):
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > res[ingredient]:
            return False
    return True
def make_coffee(drink_name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name}☕️ , enjoy!")
machine_is_on = True
chosen_drink = ""
money = 0
while machine_is_on:
    drink_choice = input("What would you like? espresso/latte/cappuccino? ")
    if drink_choice == "off":
        machine_is_on = False
    elif drink_choice == "report":
        for key, value in resources.items():
            if key == "coffee":
                print(f"{key} Remaining: {value}grams")
            else:
                print(f"{key} Remaining: {value}ml")
        print(f"Money: {money}")
    elif drink_choice in MENU:
        chosen_drink = MENU[drink_choice]
        if is_resource_sufficient(chosen_drink, resources):
            payment = gather_coins()
            if payment >= chosen_drink["cost"]:
                total_amount = round(payment - chosen_drink["cost"], 2)
                money += chosen_drink["cost"]
                # noinspection PyTypeChecker
                make_coffee(drink_choice, chosen_drink["ingredients"])
                print(f"Here is your change: ${total_amount}")
            else:
                print("Sorry, that's not enough money. Money refunded.")


        else:
            print(f"Sorry not enough resources to make your drink")

    else:
        print("Sorry that drink is invalid.")
