from dotenv import load_dotenv


# ---------------------------- PATHs ------------------------------- #
load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')
#This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self):
        self.flights_data_for_all_locations = []
    def structuring_flight_data(self):
        pass