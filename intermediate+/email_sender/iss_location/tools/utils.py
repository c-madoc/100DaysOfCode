import os
from datetime import datetime

from dateutil import tz
import requests, json
import pandas


def __get_line(path: str) -> str:
    if os.path.exists(path):
        with open(path, "r") as file:
            return file.readline().replace("\n", "")
    else:
        print(f"Missing required '{path}' file.")


def smtp_login() -> str:
    return __get_line("./data/.email.txt")


def smtp_password() -> str:
    return __get_line("./data/.pass.txt")


def get_emails() -> list:
    df = pandas.read_csv("./data/.recipients.csv")
    emails = []
    for i, person in df.iterrows():
        emails.append(person['email'])
    return emails


def get_recipients() -> list:
    df = pandas.read_csv("./data/.recipients.csv")

    users = []
    for i, user in df.iterrows():
        users.append(user)
    return users


def __get_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()['iss_position']
    return float(iss_data['longitude']), float(iss_data['latitude'])


def __get_sunrise_sunset_local(timezone, latitude, longitude):
    parameters = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()['results']
    sunrise_time = data['sunrise']
    sunset_time = data['sunset']

    sunrise_dt = __date_str_to_datetime(sunrise_time)
    sunset_dt = __date_str_to_datetime(sunset_time)

    sunrise = __convert_utc_to_local(timezone, sunrise_dt)
    sunset = __convert_utc_to_local(timezone, sunset_dt)

    return sunrise, sunset


def __date_str_to_datetime(date_string: str):
    ymd = date_string.split("T")[0]
    time = date_string.split("T")[1]
    hms = time.split("+")[0]

    date_string = f"{ymd} {hms}"
    return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')


def __convert_utc_to_local(timezone: str, datetime: datetime):
    from_utc = tz.tzutc()
    to_local = tz.gettz(timezone)

    # Tell the datetime object that it's in UTC time zone since
    # datetime objects are 'naive' by default
    utc = datetime.replace(tzinfo=from_utc)

    # Convert time zone
    central = utc.astimezone(to_local)

    return central


def dark_outside(user) -> bool:
    sunrise, sunset = __get_sunrise_sunset_local(user['timezone'], user['latitude'], user['longitude'])
    current_time = __convert_utc_to_local(user['timezone'], datetime.utcnow())

    ct_hour = current_time.hour
    sr_hour = sunrise.hour
    ss_hour = sunset.hour

    if ct_hour < sr_hour or ct_hour > ss_hour:
        return True
    return False


def iss_above(user):
    iss_lat, iss_long = __get_iss_location()
    print(iss_lat, iss_long)
    user_lat = user['latitude']
    user_long = user['longitude']

    if iss_lat > user_lat + 5 or iss_lat < user_lat - 5:
        return False
    if iss_long > user_long + 5 or iss_long < user_long - 5:
        return False
    return True

