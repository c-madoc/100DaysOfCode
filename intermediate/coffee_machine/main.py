from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":

    shutdown = False
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    while not shutdown:
        drink = input(f"What drink would you like? ({menu.get_items()}): ").lower()

        if drink == "report":
            money_machine.report()
            continue

        elif drink == "refill":
            coffee_maker.refill()
            continue


        drink = menu.find_drink(order_name=drink)

        if drink is None:
            print("That's an invalid selection.")
            continue

        if coffee_maker.has_sufficient_resources(drink=drink):
            if money_machine.make_payment(cost=drink.cost):
                coffee_maker.make_coffee(drink=drink)
            continue
        else:
            print(f"Sorry, we have run out of {drink.name}s!")
