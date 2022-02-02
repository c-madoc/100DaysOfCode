bids = []


def create_bid():
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bids.append({"name": name,
                 "bid": bid})


def get_winner():
    return sorted(bids, key=lambda d: d['bid'])[0]


if __name__ == "__main__":
    continue_bidding = True

    while continue_bidding:
        create_bid()
        continue_bidding = input("Would you like to continue? (Y/N): ").lower()

        if continue_bidding == "n":
            continue_bidding = False

    print(f"{get_winner()['name']} won with ${get_winner()['bid']}")
