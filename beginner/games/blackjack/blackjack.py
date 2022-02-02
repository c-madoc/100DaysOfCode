import random
from datetime import datetime

from cards import deck

player_hand = {"total": 0, "cards": []}
dealer_hand = {"total": 0, "cards": []}


def shuffle_shoe(shoe):
    """
    Shuffles the shoe from the default layout for more randomness
    :param shoe:
    :return:
    """

    random.seed(str(datetime.now()))
    random.shuffle(shoe)


def deal(deal_to: dict):
    """
    Deals a card to the specified player
    :param deal_to:
    :return:
    """

    # setting seed with current date time to prove randomness
    random.seed(str(datetime.now()))

    # choose a random card from the shoe
    chosen = random.choice(shoe)

    # remove the card from the shoe so we can't re-pick it
    shoe.remove(chosen)

    # add the value to the total value of the players hand
    deal_to['total'] += chosen['value']

    # add the card to the players list of cards
    deal_to['cards'].append(f"({chosen['value']}) {chosen['card']} of {chosen['suit']}")


def initial_deal():
    deal(player_hand)
    deal(dealer_hand)
    deal(player_hand)


def player_busts():
    if player_hand['total'] > 21:
        print("BUST! YOU LOSE")
        return True
    return False


def dealer_bust():
    if dealer_hand['total'] > 21:
        print("DEALER BUST! YOU WIN")
        return True
    return False


def process_action(action):
    if action == "hit":
        deal(player_hand)

    elif action == "stand":
        pass

    elif action == "fold":
        player_hand['cards'].clear()
        player_hand['total'] = 0

    else:
        print("Invalid command!")


def show_cards():
    print(f"Player: ({player_hand['total']}) {[card for card in player_hand['cards']]}")
    print(f"Dealer: ({dealer_hand['total']}) {[card for card in dealer_hand['cards']]}")


if __name__ == "__main__":
    decks = 8
    shoe = deck * decks
    shuffle_shoe(shoe)
    initial_deal()
    in_game = True
    player_turn = True
    dealer_turn = False

    while in_game:
        show_cards()

        while player_turn:
            action = input("Would you like to HIT, STAND, or FOLD?: ").lower()
            process_action(action)
            show_cards()

            if player_busts():
                in_game = False
                break

            if action == "stand":
                print("Standing")
                player_turn = False
                dealer_turn = True
                break

        while dealer_turn:
            while dealer_hand['total'] < 16:
                deal(dealer_hand)
                show_cards()
                if dealer_bust():
                    dealer_turn = False
                    break

            if dealer_hand['total'] > player_hand['total']:
                print(f"DEALER WINS (DEALER: {dealer_hand['total']} vs PLAYER: {player_hand['total']})")
            elif dealer_hand['total'] == player_hand['total']:
                print(f"DRAW (DEALER: {dealer_hand['total']} vs PLAYER: {player_hand['total']})")
            else:
                print(f"YOU WIN (DEALER: {dealer_hand['total']} vs PLAYER: {player_hand['total']})")

            dealer_turn = False
            in_game = False
            break

