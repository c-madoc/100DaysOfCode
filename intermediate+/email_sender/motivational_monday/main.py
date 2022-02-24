import smtplib
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import tools.utils as util


# ------------- EMAIL CONTENTS -------------------

QUOTE = util.get_random_quote()
SIGNATURE = "Happy Monday!\nAll the best,\n\nK"
SIGNATURE2 = "All the best,\n\nK"


# ------------- SEND EMAILS -------------------

def send_quote() -> None:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Encrypts connection
        server.login(user=util.smtp_login(), password=util.smtp_password())

        for user in util.get_recipients():

            server.sendmail(
                from_addr=util.smtp_login(),
                to_addrs=user['email'],
                msg=(
                    f"Subject:Motivational Monday\n\n"
                    f"Good morning, {user['name']}\n\n"
                    f"{QUOTE}\n\n"
                    f"{util.get_weather(user)}\n\n"
                    f"{SIGNATURE}")
            )
            print(f"Sent email to {user['email']}")


def send_weather() -> None:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Encrypts connection
        server.login(user=util.smtp_login(), password=util.smtp_password())

        for user in util.get_recipients():

            server.sendmail(
                from_addr=util.smtp_login(),
                to_addrs=user['email'],
                msg=(
                    f"Subject:Weather Report\n\n"
                    f"Good morning, {user['name']}\n\n"
                    f"{util.get_weather(user)}\n\n"
                    f"{SIGNATURE2}")
            )
            print(f"Sent email to {user['email']}")


if __name__ == "__main__":
    print("Emailer started.")
    send_weather()
    scheduler = BlockingScheduler()
    motivational_mondays = CronTrigger(day_of_week="mon", hour=8, timezone="Canada/Mountain")
    weather_updates = CronTrigger(day_of_week="tue-sun", hour=8, timezone="Canada/Mountain")
    scheduler.add_job(send_quote, motivational_mondays)
    scheduler.add_job(send_weather, weather_updates)
    scheduler.start()
