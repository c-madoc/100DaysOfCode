import os

import dotenv
import pandas
from twilio.rest import Client

dotenv.load_dotenv()


class SMS:
    def __init__(self):
        self.sid = os.environ.get("TWILIO_SID")
        self.token = os.environ.get("TWILIO_TOKEN")
        self.client = Client(self.sid, self.token)
        self.phone_number = "+19035688571"

    def send_sms(self, city: str, price: int):
        phone = os.environ.get("MY_PHONE_NUMBER")
        try:
            message = self.client.messages.create(
                body=(
                    f"New cheap flight found:\n"
                    f"To: {city}\n"
                    f"Price: {price}"
                ),
                from_=self.phone_number,
                to=phone
            )
        except Exception as e:
            print(f"Error delivering to {phone}: {e}")
        else:
            print(f"To: {phone} Status: {message.status}")

