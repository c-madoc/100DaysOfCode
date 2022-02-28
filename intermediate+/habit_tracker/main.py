import os
import dotenv
import requests
from datetime import datetime

dotenv.load_dotenv()

USERNAME = "madoc"
TOKEN = os.environ.get("USER_TOKEN")
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

now = datetime.now()


def create_new_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(f"Create new user: {response.text}")


def create_new_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    graph_config = {
        "id": GRAPH_ID,
        "name": "My Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(f"Create new graph: {response.text}")


def add_new_pixel(date: datetime, quantity: int):
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    add_pixel_config = {
        "date": str(date.strftime("%Y%m%d")),
        "quantity": str(quantity)
    }

    response = requests.post(url=pixel_endpoint, json=add_pixel_config, headers=headers)
    print(f"Add new pixel: {response.text}")


def update_pixel(date: datetime, quantity: int):
    update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"

    update_pixel_config = {
        "quantity": str(quantity)
    }

    response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
    print(f"Update pixel: {response.text}")


def delete_pixel(date: datetime):
    delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"

    response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    print(f"Delete pixel: {response.text}")


selected_date = datetime(year=2022, month=2, day=21)

# add new user
create_new_user()

# create new graph
create_new_graph()

# add new pixel
add_new_pixel(date=selected_date, quantity=100)

# update existing pixel (or make new if it doesnt exist)
update_pixel(date=selected_date, quantity=310)

# delete existing pixel
delete_pixel(date=selected_date)