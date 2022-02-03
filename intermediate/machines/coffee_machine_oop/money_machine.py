class MoneyMachine:
    CURRENCY = "$"

    COINS = {
        "dollars": 1,
        "quarters": 0.25,
        "dimes": 0.10,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profits"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted"""
        print("Please insert coins.")

        for coin in self.COINS:
            coins_in = int(input(f"How many {coin}?: "))
            self.money_received += coins_in * self.COINS[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient"""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0.0:
                print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False