import os
from pprint import pprint

import dotenv
import requests

dotenv.load_dotenv()


class FlightFinder:
    def __init__(self):

        self.api_key = os.environ.get("KIWI_API_KEY")
        self.header = {
            "apikey": self.api_key
        }

    def get_city_code(self, city_name: str):
        flight_search_endpoint = "http://tequila-api.kiwi.com/locations/query"
        params = {
            "term": city_name,
            "locale": "en-US",
            "location_type": "airport",
            "limit": "10"
        }

        data = requests.get(url=flight_search_endpoint,
                            params=params,
                            headers=self.header).json()

        for item in data['locations']:
            if item['name'].lower() == city_name.lower():
                return item['code']

    def get_cheapest_flight(self, from_city: str, to_city: str, from_date: str, to_date: str, limit: int = 3):
        flight_search_endpoint = "http://tequila-api.kiwi.com/v2/search"
        params = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from ": from_date,
            "date_to ": to_date,
            "limit": limit
        }
        cheapest_price = None
        r = requests.get(url=flight_search_endpoint,
                         params=params,
                         headers=self.header).json()

        for flight in r['data']:
            if cheapest_price is None:
                print(f"Set cheapest flight from {cheapest_price} to {flight['price']}")
                cheapest_price = flight['price']
            elif cheapest_price > flight['price']:
                print(f"Updating cheapest flight from {cheapest_price} to {flight['price']}")
                cheapest_price = flight['price']

        return {"to": to_city, "price": cheapest_price}

    def get_flight_cost(self, data):
        currency = data['currency']
        found_flights = data['data']

        condensed_prices = []

        for flight in found_flights:
            condensed_prices.append({
                'currency': currency,
                'price': flight['price']
            })
