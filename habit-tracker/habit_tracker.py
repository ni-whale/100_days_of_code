import requests
import os
from dotenv import load_dotenv

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.getenv("PIXELA_TOKEN"),
    "username": "nem0s",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)