import random


def get_bot_attack():
    attacks = ["rock", "paper", "scissors"]
    return random.choice(attacks)


def get_user_attack():
    choice = int(input("How would you like to attack?\n1. Rock\n2. Paper\n3. Scissors\n"))
    if choice == 1:
        return "rock"
    if choice == 2:
        return "paper"
    if choice == 3:
        return "scissors"


def conclude_battle(user_attack, bot_attack):
    if user_attack == "rock":
        if bot_attack == "rock":
            return "Tie"
        if bot_attack == "paper":
            return "Lost"
        if bot_attack == "scissors":
            return "Win"

    if user_attack == "paper":
        if bot_attack == "rock":
            return "Win"
        if bot_attack == "paper":
            return "Tie"
        if bot_attack == "scissors":
            return "Lost"

    if user_attack == "scissors":
        if bot_attack == "rock":
            return "Lost"
        if bot_attack == "paper":
            return "Win"
        if bot_attack == "scissors":
            return "Tie"


def announce_winner():
    user_choice = get_user_attack()
    bot_choice = get_bot_attack()
    result = conclude_battle(user_choice, bot_choice)

    if result is None:
        return print("You've made an invalid selection.")

    print(f"You attack with {user_choice}.\nBot attacks with {bot_choice}\nYou {result}!")


if __name__ == "__main__":
    announce_winner()