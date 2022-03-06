import datetime as dt

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from dateutil.relativedelta import *

from tools.flight import FlightFinder
from tools.sheety import Sheety
from tools.sms import SMS

sheets = Sheety()
sheets_data = sheets.get_data()
flight_finder = FlightFinder()
sms = SMS()

FLY_FROM_IATA = "LON"


def add_all_iata_codes():
    """Adds all IATA codes to the Google Sheet, if its not already in there."""
    print("Checking IATA codes...")
    for row in sheets_data:
        iata_code = flight_finder.get_city_code(city_name=row['city'])
        sheets.add_iata_code(sheets_data, row['id'], iata_code=iata_code)
    print("All IATA codes up to date.")


def check_prices():
    from_date = dt.datetime.now()
    to_date = from_date + relativedelta(months=6)
    print("Checking prices.")
    for item in sheets_data:
        iata_code = flight_finder.get_city_code(city_name=item['city'])
        details = flight_finder.get_cheapest_flight(FLY_FROM_IATA, iata_code, from_date.strftime("%d/%m/%Y"), to_date.strftime("%d/%m/%Y"), 5)
        trigger = sheets.required_price_for_trigger(item["lowestPrice"], details['price'])
        if trigger:
            sms.send_sms(item['city'], details['price'])


if __name__ == "__main__":
    print("Flight deal finder started.")
    scheduler = BlockingScheduler()
    schedule = CronTrigger(day_of_week="mon-sun", hour=8, timezone="Canada/Mountain")
    scheduler.add_job(check_prices, schedule)
    scheduler.start()
    check_prices()

