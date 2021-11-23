from zillow_interface import ZillowInterface
from google_form_interface import GoogleFormInterface

zillow_interface = ZillowInterface()
google_form_interface = GoogleFormInterface()

zillow_interface.find_elements()

# print(zillow_interface.links)
# print(zillow_interface.prices)
print(zillow_interface.addresses)
