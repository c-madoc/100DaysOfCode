import datetime
import time

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
    "coffee": 100
}

coins = {
    "dime": {
        "amount": 0,
        "value": 0.10
    },
    "quarter": {
        "amount": 0,
        "value": 0.25
    },
    "dollar": {
        "amount": 0,
        "value": 1
    }
}


def get_request():
    return input(f"Make a selection:\n"
                 f"  Espresso: ${MENU['espresso']['cost']}\n"
                 f"  Latte: ${MENU['latte']['cost']}\n"
                 f"  Cappuccino: ${MENU['cappuccino']['cost']}\n--> ").lower()


def report():
    report_string = ""
    for k, v in resources.items():
        measure_type = ""
        if k.lower() == "water" or k.lower() == "milk":
            measure_type = "ml"
        elif k.lower() == "coffee":
            measure_type = "g"

        report_string += f"{k.capitalize()}: {v}{measure_type}\n"

    report_string += "\n"
    total_money = 0
    for coin, details in coins.items():
        total_money += details['value'] * details['amount']
        report_string += f"{coin.capitalize()}: {details['amount']}\n"

    report_string += (f"Total Money: ${total_money}\n"
                      f"Total Orders: {orders}\n\n")

    print(report_string)


def get_money():
    money_in = 0

    dime = int(input("How many dimes?: "))
    quarter = int(input("How many quarters?: "))
    dollar = int(input("How many dollars?: "))

    money_in += dime * coins['dime']['value']
    money_in += quarter * coins['quarter']['value']
    money_in += dollar * coins['dollar']['value']

    coins['dime']['amount'] += dime
    coins['quarter']['amount'] += quarter
    coins['dollar']['amount'] += dollar

    return money_in, [dime, quarter, dollar]


def can_make_coffee(requested: str) -> bool:
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    for ingredient, amount in MENU[requested]['ingredients'].items():
        if resources[ingredient] < amount:
            return False

    return True


def make_coffee(requested: str) -> None:
    for coffee, items in MENU.items():
        if requested == coffee:

            for ingredient, amount in items['ingredients'].items():
                resources[ingredient] -= amount

    # if requested == "espresso":
    #     print("Heating the espresso...")
    #     time.sleep(1.5)
    #     print("Adding espresso...")
    #     time.sleep(1)
    #     print("Complete!")
    #
    # if requested == "latte":
    #     print("Heating the espresso...")
    #     time.sleep(1.5)
    #     print("Pouring the milk...")
    #     time.sleep(0.5)
    #     print("Steaming the milk...")
    #     time.sleep(1)
    #     print("Adding espresso...")
    #     time.sleep(1)
    #     print("Complete!")
    #
    # if requested == "cappuccino":
    #     print("Heating the espresso...")
    #     time.sleep(1.5)
    #     print("Pouring the milk...")
    #     time.sleep(0.5)
    #     print("Steaming the milk...")
    #     time.sleep(1)
    #     print("Adding milk foam...")
    #     time.sleep(1)
    #     print("Adding espresso...")
    #     time.sleep(1)
    #     print("Complete!")


def refund_order(coins):
    dime = coins[0]
    quarter = coins[1]
    dollar = coins[2]

    coins['dime']['amount'] -= dime
    coins['quarter']['amount'] -= quarter
    coins['dollar']['amount'] -= dollar


def refund_change(drink_cost, total_paid):
    refund = round(total_paid - drink_cost, 2)

    dollars = int(refund // 1)
    coins['dollar']['amount'] -= int(dollars)
    refund %= 1

    quarters = int(refund // .25)
    coins['quarter']['amount'] -= int(quarters)
    refund %= .25

    dimes = int(refund // .10)
    coins['dime']['amount'] -= int(dimes)
    refund %= .10

    if dollars != 0 or quarters != 0 or dimes != 0:
        print(f"You paid ${total_paid}, but the order was ${drink_cost}\n"
              f"You've been returned ${round(total_paid - drink_cost, 2)} (Dimes: {dimes} | Quarters: {quarters} | Dollars: {dollars})\n")


def restock():
    return {
        "water": 300,
        "milk": 200,
        "coffee": 100
    }


if __name__ == "__main__":
    shutdown = False

    orders = []

    while not shutdown:
        # if orders > 0:
        # time.sleep(5)
        request = get_request()

        # shut down the coffee machine
        if request == "off":
            shutdown = True
            print("Shutting down.")
            print(f"Summary: {orders}")
            break

        # send machine report
        if request == "report":

            orders.append({
                "type": "REPORT",
                "timestamp": datetime.datetime.now()
            })

            report()
            continue

        # restocks the coffee machine
        if request == "restock":

            orders.append({
                "type": "RESTOCK",
                "timestamp": datetime.datetime.now()
            })

            resources = restock()
            continue

        if request not in ['espresso', 'latte', 'cappuccino']:
            print("Invalid selection. Please try again. \n")
            continue

        # if we have ingredients to make the coffee
        if can_make_coffee(request):
            money, given_coins = get_money()

            # check if the user put enough money into the machine
            if money < MENU[request]['cost']:
                print("That is not enough money! Refunding...\n")
                refund_order(given_coins)
                continue

            # refund extra change the user gives
            refund_change(MENU[request]['cost'], money)

            # make the coffee
            make_coffee(request)

            # track each order
            orders.append({
                "type": "ORDER",
                "item": request,
                "price": MENU[request]['cost'],
                "timestamp": datetime.datetime.now()
            })

            print(f"Here is your ☕ {request} ☕ - thank you for your purchase!\n\n")
            request = None
            continue

        # if we do not have ingredients to make the coffee
        else:
            print("\nOUT OF STOCK!\n")
