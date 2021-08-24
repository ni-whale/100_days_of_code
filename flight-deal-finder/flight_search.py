from dotenv import load_dotenv
import os



# ---------------------------- PATHs ------------------------------- #
load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')
tequila_api = os.getenv('TEQUILA_FLY_API')
tequila_endpoing_get = "https://tequila-api.kiwi.com/locations/query"

class FlightSearch:
    pass