import os
from pprint import pprint

import dotenv
import pandas
import requests
from twilio.rest import Client

dotenv.load_dotenv()


class StockData:
    def __init__(self, ticker: str, threshold: int):
        self.ticker = ticker
        self.threshold = threshold

        self.params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.ticker,
            "apikey": os.environ.get("STOCK_API")
        }
        self.URL = "https://www.alphavantage.co/query"

    def __get_data(self) -> dict:
        response = requests.get(url=self.URL, params=self.params)
        response.raise_for_status()
        return response.json()['Time Series (Daily)']

    def get_latest_data(self) -> (float, float):
        data = self.__get_data()
        data = {k: data[k] for k in list(data)[:3]}

        most_recent_close = None
        next_recent_close = None

        for date, stock_data in data.items():
            if stock_data['4. close'] != "":
                if most_recent_close is None:
                    most_recent_close = float(stock_data['4. close'])
                elif next_recent_close is None:
                    next_recent_close = float(stock_data['4. close'])
        return most_recent_close, next_recent_close

    def get_latest_changes(self) -> float:
        most_recent, next_recent = self.get_latest_data()
        return ((most_recent - next_recent) / next_recent) * 100

    def stock_past_threshold(self) -> bool:
        change = self.get_latest_changes()
        if change >= self.threshold:
            return True
        elif change <= -abs(self.threshold):
            return True
        else:
            return False

    def build_string(self):
        change = self.get_latest_changes()
        arrow = ""
        if change >= self.threshold:
            arrow = "?"
        elif change <= -abs(self.threshold):
            arrow = "?"
        return f"{self.ticker}: {arrow}\n"


class StockNews:
    def __init__(self, company_name: str, news_pieces: int):
        self.news_pieces = news_pieces
        self.params = {
            "q": company_name,
            "apiKey": os.environ.get("NEWS_API"),
            "sortBy": "publishedAt"
        }
        self.URL = "https://newsapi.org/v2/everything"

    def get_data(self):
        response = requests.get(url=self.URL, params=self.params)
        response.raise_for_status()
        return response.json()['articles']

    def get_recent_news(self):
        data = self.get_data()
        return data[:self.news_pieces]

    def build_string(self):
        string = ""
        for news_piece in self.get_recent_news():
            string += f"Headline: {news_piece['title']}\nBrief: {news_piece['description']}\nLink: {news_piece['url']}\n\n"
        return string

class SMS:
    def __init__(self):
        self.sid = os.environ.get("TWILIO_SID")
        self.token = os.environ.get("TWILIO_TOKEN")
        self.client = Client(self.sid, self.token)
        self.phone_number = "+19035688571"

    def send_sms(self, text: str):
        df = pandas.read_csv("./data/.recipients.csv")

        for i, person in df.iterrows():
            try:
                message = self.client.messages.create(
                    body=text,
                    from_=self.phone_number,
                    to=person['phone']
                )
            except Exception as e:
                print(f"Error delivering to {person['name']}: {e}")
            else:
                print(f"To: {person['name']} Status: {message.status}")

