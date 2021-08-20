from dotenv import load_dotenv
import os
import datetime as DT
import requests

# ---------------------------- PATHs ------------------------------- #

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint_adding_row = "https://api.sheety.co/6f646ab411f639652d7483808719cf20/workoutTracking/workouts"

# ---------------------------- CONSTANTS ------------------------------- #

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')

# ---------------------------- LOGIC ------------------------------- #

# Getting info about calories based on the exercise provided by the user. Natural language recognition done on the API side.
headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

user_input = input("What exercise you did: ")
exercise_params = {
    "query": user_input
}

response_nutritionix = requests.post(url=exercise_endpoint, headers=headers, json=exercise_params)
response_nutritionix.raise_for_status()
exercise_result = response_nutritionix.json()

# Adding the last workout to the google sheet by using Sheety API

current_date = DT.datetime.now().strftime('%d/%m/%Y')
current_time = DT.datetime.now().strftime("%X")
exercise = exercise_result['exercises'][0]['name']
duration = exercise_result['exercises'][0]['duration_min']
calories = exercise_result['exercises'][0]['nf_calories']

sheety_body_post = {
    'workout': {
        'date': current_date,
        'time': current_time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories
    }
}

response_sheety = requests.post(sheety_endpoint_adding_row, json=sheety_body_post)
response_sheety.raise_for_status()



