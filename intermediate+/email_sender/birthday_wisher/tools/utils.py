import calendar
import datetime
import os
import random
import datetime as dt

import pandas


def __get_line(path: str):
    if os.path.exists(path):
        with open(path, "r") as file:
            return file.readline().replace("\n", "")
    else:
        print(f"Missing required '{path}' file.")


def __get_random_letter():
    letter = random.choice(os.listdir("./templates/"))

    with open(f"./templates/{letter}", "r") as f:
        return f.read()


def smtp_login():
    return __get_line("./data/.email.txt")


def smtp_password():
    return __get_line("./data/.pass.txt")


def get_birthday():
    now = datetime.datetime.now()
    df = pandas.read_csv("./data/birthdays.csv")

    for i, person in df.iterrows():
        birthday = datetime.datetime(now.year, person['month'], person['day'])

        if birthday.date() == now.date():
            return person


def write_letter(person):
    raw_letter = __get_random_letter()

    return raw_letter.replace("[NAME]", person['name'])

