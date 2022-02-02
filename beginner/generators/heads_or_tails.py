import random


def flip():
    rand_int = random.randint(0, 1)

    if rand_int == 0:
        return "Heads"
    return "Tails"


if __name__ == "__main__":
    print(f"You flipped {flip()}")
