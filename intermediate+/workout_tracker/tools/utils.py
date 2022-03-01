import os

import dotenv
import requests

dotenv.load_dotenv()


class NutritionAPI:
    def __init__(self, query, gender=None, weight_kg=None, height_cm=None, age=None):
        self.nutri_app_id = os.environ.get("NUTRI_APP_ID")
        self.nutri_api_key = os.environ.get("NUTRI_API_KEY")
        self.nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

        self.headers = {
            "x-app-id": self.nutri_app_id,
            "x-app-key": self.nutri_api_key
        }

        self.params = {
            "query": query,
            "gender": gender,
            "weight_kg": weight_kg,
            "height_cm": height_cm,
            "age": age
        }

    def get_exercises(self):
        response = requests.post(url=self.nutri_endpoint, json=self.params, headers=self.headers)
        return response.json()['exercises']


class SheetyAPI:
    def __init__(self):
        self.sheety_token = f'Bearer {os.environ.get("SHEETY_API_TOKEN")}'
        self.sheety_endpoint = "https://api.sheety.co/c63b8927f39edd0dc3fa69686cacf33e/myWorkouts/workouts"
        self.headers = {
            "Authorization": self.sheety_token
        }

    def get_data(self, object_id: int = None):
        if object_id is None:
            object_id = ""
        response = requests.get(url=f"{self.sheety_endpoint}/{object_id}", headers=self.headers)
        return response.json()

    def add_data(self, date, time, exercise, duration, calories):
        data = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
        }
        response = requests.post(url=self.sheety_endpoint, json=data, headers=self.headers)
        if response.status_code == 200:
            print(f"Added {duration} minutes of {exercise}")
        else:
            print(response.text)
