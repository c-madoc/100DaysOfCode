import random


def get_names():
    names_string = input("Enter each name, separated with a comma.")
    names = names_string.split(",")
    return [name.strip() for name in names]


def get_random_name():
    names = get_names()
    return random.choice(names)


print(f"{get_random_name()} is going to pay for the meal today.")
