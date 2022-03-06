import os

import dotenv
import requests

dotenv.load_dotenv()


class Sheety:
    def __init__(self):
        self.sheety_token = f'Bearer {os.environ.get("SHEETY_API_TOKEN")}'
        self.sheety_endpoint = "https://api.sheety.co/c63b8927f39edd0dc3fa69686cacf33e/flightDeals/prices"
        self.headers = {
            "Authorization": self.sheety_token
        }

    def get_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.headers)
        return response.json()['prices']

    def add_iata_code(self, data, object_id: int, iata_code: str):
        for item in data:
            if item['id'] == object_id:
                if item['iataCode'].lower() != iata_code.lower():
                    data = {
                        "price": {
                            "iataCode": iata_code
                        }
                    }
                    response = requests.put(url=f"{self.sheety_endpoint}/{object_id}", json=data)
                    response.raise_for_status()
                    print(f"Added IATA code for {item['city']} {iata_code}")

    def required_price_for_trigger(self, max_flight_price: int, current_price: int) -> bool:
        """Check if Sheets minimum is the same or less than flight_price"""
        if current_price < max_flight_price:
            return True
        return False
