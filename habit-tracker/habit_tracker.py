import requests
import os
from dotenv import load_dotenv
import datetime as DT

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')

username = "nem0s"
token = os.getenv("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_id = "graph1"

graph_config = {
    'id': graph_id,
    'name': 'coding-time-tracker',
    'unit': 'hour',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_id}"

pixel_config = {
    'date': DT.datetime.today().strftime('%Y%m%d'),
    'quantity': "1"
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)