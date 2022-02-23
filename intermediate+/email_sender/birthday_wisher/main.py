##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
from tools import utils

birthday = utils.get_birthday()
letter = utils.write_letter(birthday)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(user=utils.smtp_login(), password=utils.smtp_password())
    server.sendmail(
        from_addr=utils.smtp_login(),
        to_addrs=birthday['email'],
        msg=f"Subject: Happy Birthday!\n\n{letter}"
    )

