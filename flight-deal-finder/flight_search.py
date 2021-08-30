from dotenv import load_dotenv
import os
import requests
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# ---------------------------- PATHs ------------------------------- #
load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')


class FlightSearch:
    def __init__(self):
        tequila_api = os.getenv('TEQUILA_FLY_API')
        self.tequila_endpoing_get = "https://tequila-api.kiwi.com/locations/query"
        self.tequila_enpoint_flights = "https://tequila-api.kiwi.com/v2/search"
        self.body_request_get_iata = {
            "term": "",
            "location_types": "city",
        }
        self.header = {"accept": "application/json", "apikey": tequila_api}
        # .strftime("%d/%m/%Y")
        day = datetime.today().day
        month = datetime.today().month
        year = datetime.today().year
        self.today = f"{day}/{month}/{year}"
        self.six_moth_later = (date(year, month, day) + relativedelta(months=+6)).strftime("%d/%m/%Y")


    def iata_search(self, town):
        self.body_request_get_iata["term"] = town
        request = requests.get(url=self.tequila_endpoing_get, params=self.body_request_get_iata, headers=self.header)
        request.raise_for_status()
        city_data = request.json()['locations']
        return city_data

    def flights_searh(self, iata_codes):
        body_request_get_flights = {
            "fly_from": "OZH",
            "fly_to": iata_codes[3],
            "date_from": self.today,
            "date_to": self.six_moth_later,
            "adults": 2,
            "adult_hold_bag": "1,0",
            "curr": "UAH",
        }
        request = requests.get(url=self.tequila_enpoint_flights, params=body_request_get_flights, headers=self.header)
        request.raise_for_status()
        flights_data = request.text
        return flights_data




