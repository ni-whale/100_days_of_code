from dotenv import load_dotenv
import os
import requests

# ---------------------------- PATHs ------------------------------- #
load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')


class FlightSearch:
    def __init__(self):
        tequila_api = os.getenv('TEQUILA_FLY_API')
        self.tequila_endpoing_get = "https://tequila-api.kiwi.com/locations/query"
        self.body_request_get = {
            "term": "",
            "location_types": "city",
        }
        self.header ={"accept": "application/json", "apikey": tequila_api}


    def iata_search(self, town):
        self.body_request_get["term"] = town
        request = requests.get(url=self.tequila_endpoing_get, params=self.body_request_get, headers=self.header)
        request.raise_for_status()
        city_data = request.json()['locations']
        return city_data



