from dotenv import load_dotenv
import requests
import os

#This class is responsible for talking to the Google Sheet.

# ---------------------------- PATHs ------------------------------- #
load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')
sheety_endpoint_get = "https://api.sheety.co/6f646ab411f639652d7483808719cf20/flightDeals/prices"
sheety_endpoint_put = "https://api.sheety.co/6f646ab411f639652d7483808719cf20/flightDeals/prices/[Object ID]"

token = os.getenv("SHEETY_BEARER_TOKEN")



class DataManager:
    def __init__(self):
        self.headers_sheety = {f"Authorization": f"Bearer {token}"}

    def getting_list_of_cities(self):
        sheety_get_response = requests.get(url=sheety_endpoint_get, headers=self.headers_sheety)
        sheety_get_response.raise_for_status()
        print(sheety_get_response.json())

