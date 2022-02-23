import calendar
import os
import random
import smtplib
import datetime as dt


def get_line(path: str):
    if os.path.exists(path):
        with open(path, "r") as file:
            return file.readline().replace("\n", "")
    else:
        print(f"Missing required '{path}' file.")


def get_random_quote():
    if os.path.exists("quotes.txt"):
        with open("quotes.txt", "r") as file:
            return random.choice(file.readlines())


# ------------- DATETIME MANAGER -------------------
now = dt.datetime.now()
day_of_week = calendar.day_name[now.weekday()]
print(f"Day: {day_of_week}")

# ------------- SENDING TO -------------------
email_list = []
emails = []

# ------------- EMAIL CONTENTS -------------------
SUBJECT = f"Motivational {day_of_week}"
QUOTE = get_random_quote()
SIGNATURE = "Have a great day!"

# ------------- LOGIN -------------------
my_email = get_line(".email.txt")
my_password = get_line(".pass.txt")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # Encrypts connection
    server.login(user=my_email, password=my_password)

    if day_of_week == "Monday":
        print(f"Sending quote: {QUOTE}")
        for email in emails:
            server.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:{SUBJECT}\n\n{QUOTE}\n\n{SIGNATURE}"
            )
            print(f"Email sent to {email}")
