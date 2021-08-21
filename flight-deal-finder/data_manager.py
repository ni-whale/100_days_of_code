from dotenv import load_dotenv


# ---------------------------- PATHs ------------------------------- #
load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')

sheety_endpoint_get = "https://api.sheety.co/6f646ab411f639652d7483808719cf20/flightDeals/prices"
sheety_endpoint_put = "https://api.sheety.co/6f646ab411f639652d7483808719cf20/flightDeals/prices/[Object ID]"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass