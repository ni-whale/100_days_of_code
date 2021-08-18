from dotenv import load_dotenv
import os
import datetime as DT
import requests

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

user_input = input("What exercise you did: ")

exercise_params = {
    "query": user_input
}

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_params)
response.raise_for_status()
print(response.text)




