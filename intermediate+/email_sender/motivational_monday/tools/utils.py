import os
import random
import requests, json
import pandas


def __get_line(path: str) -> str:
    if os.path.exists(path):
        with open(path, "r") as file:
            return file.readline().replace("\n", "")
    else:
        print(f"Missing required '{path}' file.")


def __get_random_quote() -> str:
    with open(f"./data/quotes.txt", "r") as f:
        return f.read()


def smtp_login() -> str:
    return __get_line("./data/.email.txt")


def smtp_password() -> str:
    return __get_line("./data/.pass.txt")


def get_random_quote() -> str:
    if os.path.exists("./data/quotes.txt"):
        with open("./data/quotes.txt", "r") as file:
            return random.choice(file.readlines())


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


def calculate_to_celsius(kelvin):
    return round(kelvin - 273.15)


def get_weather(person):
    city = person["city"]
    api_key = __get_line('./data/.weather_api.txt')
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = f"{BASE_URL}q={city},CA&appid={api_key}"
    print(URL)

    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']

        details = {
            "city": city,
            "curr_temp": calculate_to_celsius(main['temp']),
            "feels_like": calculate_to_celsius(main['feels_like']),
            "temp_max": calculate_to_celsius(main['temp_max']),
            "temp_min": calculate_to_celsius(main['temp_min']),
            "humidity": main['humidity'],
            "pressure": main['pressure'],
            "report": data['weather'],

        }

        return report_weather(details)

    else:
        print("HTTP Request Error")
        return None


def report_weather(weather_data) -> str:
    return (
        f"Weather report in {weather_data['city']}:\n\n"
        f"Temperature: {weather_data['curr_temp']}C (Feels like {weather_data['feels_like']}C)\n"
        f"High of {weather_data['temp_max']}C with a low of {weather_data['temp_min']}C\n"
        f"Humidity: {weather_data['humidity']}%\n"
    )
