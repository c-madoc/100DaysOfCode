import menu


class CoffeeMaker:
    def __init__(self):

        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def has_sufficient_resources(self, drink: menu.MenuItem) -> bool:
        """Returns True when the coffee machine has enough ingredients,
        False if they are insufficient"""

        # for every ingredient in the drinks ingredients
        for item in drink.ingredients:

            # if the machine doesnt have enough ingredients
            if drink.ingredients[item] > self.resources[item]:
                return False
        return True

    def make_coffee(self, drink: menu.MenuItem):
        """Deducts the required ingredients from the resources"""
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Thank you for you purchase. Enjoy your {drink.name} ☕ ! ")

    def refill(self):
        print("You refill the coffee maker.")
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
