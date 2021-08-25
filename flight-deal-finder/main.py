from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()


list_of_cities = data_manager.getting_list_of_cities()['prices']

# for record in list_of_cities:
#     print(record["city"])

iata_search_data_collector = [flight_search.iata_search(list_of_cities['city']) for city, index in list_of_cities]
# print(iata_search_data_collector[0])

# for city in list_of_cities:
#     for record in flight_search.iata_search(city['city']):
#         print(f"{record['locations']['name']}/{record['locations']['code']}")



# for record in iata_search_data_collector:
#     print(f"{record['locations']['name']}/{record['locations']['code']}")



