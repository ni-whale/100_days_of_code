from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

# TODO Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air
#  Transport Association (IATA) codes for each city.Most of the cities in the sheet include multiple airports,
#  you want the city code (not the airport code see here).

# ---------------------------- GETTING IATA CODE FOR EACH CITY ------------------------------- #
list_of_cities = []
list_of_iata_codes = []
all_codes_presented = True
# adding city to the list in case if IATA code is not presented
for record in data_manager.getting_list_of_cities():
    if len(record['iataCode']) == 0:
        list_of_cities.append(record['city'])
        all_codes_presented = False
    else:
        if record not in list_of_iata_codes:
            list_of_iata_codes.append(record['iataCode'])
        continue
list_of_iata_codes = [code.upper() for code in list_of_iata_codes]  # for use in flights search
while not all_codes_presented:
    # Getting the whole info about each city from the list
    iata_search_data_collector = [flight_search.iata_search(city) for city in list_of_cities]
    getting_iata_code = []
    for town in iata_search_data_collector:
        getting_iata_code.append([record["code"] for record in town if record["name"] in list_of_cities
                                  and record["code"] is not None])
    data_manager.updating_sheet_by_iata_codes(getting_iata_code)  # Updating the spreadsheet by info we got
    all_codes_presented = True

print(flight_search.flights_seardh(*list_of_iata_codes))

# TODO Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities
#  in the Google Sheet.

# ---------------------------- CHECKING FLIGHTS ------------------------------- #


# TODO If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number
#  with the Twilio API.

# TODO The SMS should include the departure airport IATA code, destination airport IATA code, departure city,
#  destination city, flight price and flight dates.