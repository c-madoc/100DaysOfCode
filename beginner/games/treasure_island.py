def greeting():
    print("Welcome to Treasure Island.\nRiches are waiting to be found...")


def first_question():
    return input("You find yourself at a fork in the road. What way would you like to go? (Left / Right)\n").lower()


def second_question():
    return input("As you walk down the path, you find a parade blocking your way.\n"
                 "Do you want to wait, or try and sneak past? (Wait / Sneak)\n").lower()


def third_question():
    return input(
        "You come across 3 doors: red, blue, and yellow. Which one do you choose? (Red / Blue / Yellow)\n").lower()


if __name__ == "__main__":
    greeting()
    if first_question() == "right":
        if second_question() == "wait":
            third = third_question()
            if third == "yellow":
                print("As you open the door, you find a glowing chest. Congratulations, you found the treasure!")

            elif third == "red":
                print("As you open the door, lava suddenly starts pouring out! You get engulfed by the lava and die.")

            elif third == "blue":
                print("As you open the door, water suddenly starts pouring out! With nowhere to go, you drown and die.")
        else:
            print(
                "As you try to sneak past the parade, your jacket gets stuck! Before you know it, you are being trampled by the entire parade! You died.")
    else:
        print(
            "As you continue walking down the right path, a bear comes out of the woods and mauls you! You bleed out and die.")
