from dotenv import load_dotenv
import requests
import os

#This class is responsible for talking to the Google Sheet.

# ---------------------------- PATHs ------------------------------- #
load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')


class DataManager:
    def __init__(self):
        self.sheety_endpoint_get = "https://api.sheety.co/6f646ab411f639652d7483808719cf20/flightDeals/prices"
        self.sheety_endpoint_put = "https://api.sheety.co/6f646ab411f639652d7483808719cf20/flightDeals/prices/"
        token = os.getenv("SHEETY_BEARER_TOKEN")
        self.headers_sheety = {f"Authorization": f"Bearer {token}"}
        self.row_id = 1

    def getting_list_of_cities(self):
        sheety_get_response = requests.get(url=self.sheety_endpoint_get, headers=self.headers_sheety)
        sheety_get_response.raise_for_status()
        return sheety_get_response.json()['prices']

    def updating_sheet_by_iata_codes(self, codes):
        for code in codes:
            self.row_id += 1
            sheety_body = {"price": {"iataCode": code[0].lower()}}
            self.sheety_endpoint_put = f"https://api.sheety.co/6f646ab411f639652d7483808719cf20/flightDeals/prices/{self.row_id}"
            print(f"{sheety_body}\n{self.sheety_endpoint_put}")
            sheety_put_response = requests.put(url=self.sheety_endpoint_put, headers=self.headers_sheety,
                                               json=sheety_body)
            sheety_put_response.raise_for_status()


