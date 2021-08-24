#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager

data_manager = DataManager()

json_data = data_manager.getting_list_of_cities()['prices']

for record in json_data:
    print(record['city'])

