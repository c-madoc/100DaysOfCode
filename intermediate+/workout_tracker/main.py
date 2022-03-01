from datetime import datetime
from pprint import pprint

from tools import utils

query = input("What workout did you do today?: ")

nutri = utils.NutritionAPI(query=query)
exercises = nutri.get_exercises()

sheety = utils.SheetyAPI()

for exercise in exercises:
    sheety.add_data(
        date=datetime.now().strftime("%d/%m/%Y"),
        time=datetime.now().strftime("%H:%M:%S"),
        exercise=exercise["name"].title(),
        duration=exercise["duration_min"],
        calories=exercise["nf_calories"]
    )

