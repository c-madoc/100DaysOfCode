import time
import smtplib
import tools.utils as util

# ------------- NOTES -------------------
"""
You must include an .email.txt, .pass.txt, and .recipients.csv in the ./data/ folder
.recipients.csv must have the following:
    name,email,latitude,longitude,timezone,city

timezones can be found here: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
"""

# ------------- SEND EMAILS -------------------

def send_iss_location() -> None:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Encrypts connection
        server.login(user=util.smtp_login(), password=util.smtp_password())

        for user in util.get_recipients():
            if util.iss_above(user) and util.dark_outside(user):
                server.sendmail(
                    from_addr=util.smtp_login(),
                    to_addrs=user['email'],
                    msg=(
                        f"Subject:ISS Overhead\n\n"
                        f"Hi, {user['name']}\n\n"
                        f"The ISS is currently above {user['city']}."
                    )
                )
                print(f"Sent email to {user['email']}")


if __name__ == "__main__":
    while True:
        send_iss_location()
        time.sleep(60)

