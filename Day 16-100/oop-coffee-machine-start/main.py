from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
machine = CoffeeMaker()
coins = MoneyMachine()

machine_running = True


while machine_running:
    choice = input(f"What would you like? {drinks.get_items()}: ")
    if choice == "off":
        machine_running = False
    elif choice == "report":
        machine.report()
        coins.report()
    else:
        drink = drinks.find_drink(order_name=choice)
        if machine.is_resource_sufficient(drink):
            if coins.make_payment(drink.cost):
                machine.make_coffee(drink)
