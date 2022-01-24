class TipCalculator:

    def __init__(self, currency: str, total: float, tip_percent: float, split: int):
        self.currency = currency
        self.total_bill = total
        self.split_between = split
        self.tip_percentage = tip_percent

    def _total_with_tip(self) -> float:
        return self.total_bill * (1 + self.tip_percentage)

    def _split_bill(self) -> float:
        return round(self._total_with_tip() / self.split_between, 2)

    def tip_total(self) -> str:
        tip = round((self.total_bill * (1 + self.tip_percentage)) - self.total_bill, 2)

        return f"{selected_currency}{tip / self.split_between}"

    def payment(self) -> str:
        return f"{selected_currency}{self._split_bill()}"


def _get_total_bill() -> (str, float):
    currency = ""
    total = input("What was the total bill?\n")
    rep = {"$": "", "€": "", "£": ""}

    # replace and capture the currency type used
    # convert the string to a float for the amount
    try:
        for x, y in rep.items():
            if x in total:
                currency = x
                total = float(total.replace(x, y))
                return currency, total
    except:
        currency = "$"
        total = float(total)
        return currency, total


def _get_tip() -> float:
    get_tip = int(input("How much of a tip would you like to give?\n"
                        "1: 10%\n"
                        "2. 12%\n"
                        "3: 15%\n"
                        "4: 20%\n"))

    if get_tip == 1:
        return 0.10

    if get_tip == 2:
        return 0.12

    if get_tip == 3:
        return 0.15

    if get_tip == 4:
        return 0.20


def get_split() -> int:
    return int(input("How many people should pay?\n"))


def announce_payment(split_between: int, payment: str, total_tip: str) -> None:
    if split_between <= 1:
        print(f"Your total bill including tip is {payment}. You are paying a tip of {total_tip}.")
        return

    print(f"Split between {split_between} people, including tip, each should pay {payment}.\n"
          f"Each person is tipping {total_tip}.")
    return


if __name__ == "__main__":
    selected_currency, total_bill = _get_total_bill()
    tip_percent = _get_tip()
    split_between = get_split()

    tip_calc = TipCalculator(selected_currency, total_bill, tip_percent, split_between)
    payment = tip_calc.payment()
    total_tip = tip_calc.tip_total()

    announce_payment(split_between, payment, total_tip)
