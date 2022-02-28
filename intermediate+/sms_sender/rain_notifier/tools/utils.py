import os

from dotenv import load_dotenv

import pandas
from twilio.rest import Client

import requests

ROOT_URL = "https://api.openweathermap.org/data/2.5/onecall"

load_dotenv()

def get_phone_numbers() -> list:
    df = pandas.read_csv("./data/.recipients.csv")
    emails = []
    for i, person in df.iterrows():
        emails.append(person['phone'])
    return emails


class Data:
    def __init__(self):
        self.params = {
            "lat": 32.514252,
            "lon": -93.747772,
            "appid": os.environ.get("OWM_API_KEY"),
            "exclude": "current,minutely,daily"
        }

    def __get_data(self):
        response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=self.params)
        response.raise_for_status()
        data = response.json()
        return data

    def __get_hourly_data(self):
        return self.__get_data()['hourly'][:12]

    def will_rain(self):
        """
        Checks the 12 hour list of weather data
        If there is going to be rain today, returns true
        :return:
        """
        rain = False
        for item in self.__get_hourly_data():
            if item['weather'][0]['id'] < 700:
                rain = True
        return rain

class SMS:
    def __init__(self):
        self.sid = os.environ.get("TWILIO_SID")
        self.token = os.environ.get("TWILIO_TOKEN")
        self.client = Client(self.sid, self.token)
        self.phone_number = "+19035688571"

    def send_sms(self):
        df = pandas.read_csv("./data/.recipients.csv")

        for i, person in df.iterrows():
            try:
                message = self.client.messages.create(
                    body=f"Good morning, {person['name']}. It's going to rain today.",
                    from_=self.phone_number,
                    to=person['phone']
                )
            except Exception as e:
                print(f"Error delivering to {person['name']}: {e}")
            else:
                print(f"To: {person['name']} Status: {message.status}")



