from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from tools import utils


def check_and_text():
    if utils.Data().will_rain():
        print("it will rain.")
        utils.SMS().send_sms()


if __name__ == "__main__":
    print("Rain checker started.")
    scheduler = BlockingScheduler()
    schedule = CronTrigger(day_of_week="mon-sun", hour=20, minute=51, timezone="Canada/Mountain")
    scheduler.add_job(check_and_text, schedule)
    scheduler.start()
