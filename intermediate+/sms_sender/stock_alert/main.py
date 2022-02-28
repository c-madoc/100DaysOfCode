from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from tools.utils import *

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock = StockData(ticker=STOCK, threshold=1)
news = StockNews(company_name=COMPANY_NAME, news_pieces=1)
sms = SMS()


def alert_stock():
    if stock.stock_past_threshold():
        text = f"{stock.build_string()}{news.build_string()}"
        sms.send_sms(text=text)


if __name__ == "__main__":
    print("Stock Alert started.")
    scheduler = BlockingScheduler()
    alert_schedule = CronTrigger(day_of_week="mon-sun", hour=6, timezone="Canada/Mountain")
    scheduler.add_job(alert_stock, alert_schedule)
    scheduler.start()
