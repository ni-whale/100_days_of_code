from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

# ---------------------------- GETTING IATA CODE FOR EACH CITY ------------------------------- #
list_of_cities = []
for record in data_manager.getting_list_of_cities():
    list_of_cities.append(record['city'])

iata_search_data_collector = [flight_search.iata_search(city) for city in list_of_cities]
getting_iata_code = []
for town in iata_search_data_collector:
    getting_iata_code.append([record["code"] for record in town if record["name"] in list_of_cities
                              and record["code"] is not None])



# city_and_iata_code = dict(zip(list_of_cities, getting_iata_code))
# print(city_and_iata_code)

print(data_manager.updating_sheet_by_iata_codes(getting_iata_code))



