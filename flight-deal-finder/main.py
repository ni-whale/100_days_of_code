from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

iata_search_data_collector = []
list_of_cities = data_manager.getting_list_of_cities()['prices']
# for record in list_of_cities:
#     iata_search_data_collector.append(flight_search.iata_search(record['city']))
for city in list_of_cities:
    for record in flight_search.iata_search(city['city']):
        print(f"{record['locations']['name']}/{record['locations']['code']}")
# print(iata_search_data_collector)
# for record in iata_search_data_collector:
#     print(f"{record['locations']['name']}/{record['locations']['code']}")



