import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "$", "%", "^", "&", "*", "(", ")", "#"]

print("Welcome to KeesPass Generator")
nr_letters = int(input("How many letters would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))


def get_letters():
    r_letters = []
    for letter in range(0, nr_letters):
        rand = random.randint(0, 1)

        if rand == 0:
            r_letters.append(random.choice(letters).capitalize())
            continue

        r_letters.append(random.choice(letters))

    return r_letters


def get_numbers():
    r_numbers = []
    for number in range(0, nr_numbers):
        r_numbers.append(random.choice(numbers))

    return r_numbers


def get_symbols():
    r_symbols = []

    for symbol in range(0, nr_symbols):
        r_symbols.append(random.choice(symbols))

    return r_symbols


def generate_password():
    password_list = get_letters() + get_numbers() + get_symbols()
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    return password


def announce_password():  # we should never announce our passwords...
    pw = generate_password()
    print(f"Your password is: {pw}")


if __name__ == "__main__":
    announce_password()
