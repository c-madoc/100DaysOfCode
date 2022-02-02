class Order:
    def __init__(self, size, extra_pepperoni=False, extra_cheese=False):
        self.size = size
        self.extra_pepperoni = extra_pepperoni
        self.extra_cheese = extra_cheese
        self.order_total = 0

    def _price_size(self) -> None:
        ordered_size = self.size.lower()

        if ordered_size == "s":
            self.order_total += 5.00

        if ordered_size == "m":
            self.order_total += 7.50

        if ordered_size == "l":
            self.order_total += 10.00

    def _price_extras(self) -> None:
        if self.extra_pepperoni:
            self.order_total += 2.00

        if self.extra_cheese:
            self.order_total += 1.50

    def total(self):
        self._price_size()
        self._price_extras()
        return self.order_total


def ask_size() -> str:
    return input("What size of a pizza would you like? (S/M/L)\n").lower()


def ask_extras() -> (bool, bool):
    ask_pepperoni = input("Would you like extra pepperoni? (Y/N)\n").lower()
    ask_cheese = input("Would you like extra cheese? (Y/N)\n").lower()

    if ask_pepperoni == "y":
        add_pepperoni = True
    else:
        add_pepperoni = False

    if ask_cheese == "y":
        add_cheese = True
    else:
        add_cheese = False

    return add_pepperoni, add_cheese


def announce_order(pizza_size: str, add_pepperoni: bool, add_cheese: bool, total: float):
    order_string = "You ordered a "

    if pizza_size == "s":
        order_string += "small "

    elif pizza_size == "m":
        order_string += "medium "

    elif pizza_size == "l":
        order_string += "large "

    order_string += "pizza"

    if add_pepperoni or add_cheese:
        order_string += " with "

        if add_pepperoni:
            order_string += "extra pepperoni"

        if add_pepperoni and add_cheese:
            order_string += " and "

        if add_cheese:
            order_string += "extra cheese"

    order_string += f".\nYour total is ${total}."

    print(order_string)


if __name__ == "__main__":
    size = ask_size()
    pepperoni, cheese = ask_extras()
    order = Order(size, pepperoni, cheese)

    announce_order(size, pepperoni, cheese, order.total())
