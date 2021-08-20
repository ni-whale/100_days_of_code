from dotenv import load_dotenv
import os
import datetime as DT
import requests

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint_adding_row = "https://api.sheety.co/6f646ab411f639652d7483808719cf20/workoutTracking/workouts"

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



# sheety_body_post = {
#     'workout': {
#         'date': DT.datetime.now().strftime('%d/%m/%Y'),
#         'time': DT.datetime.now().strftime("%X")
#     }
# }
#
# response = requests.post(sheety_endpoint_adding_row, json=sheety_body_post)
# response.raise_for_status()
# print(response.text)


