from zillow_interface import ZillowInterface
from google_form_interface import GoogleFormInterface

zillow_interface = ZillowInterface()
zillow_interface.find_elements()

# print(zillow_interface.links)
# print(zillow_interface.prices)
# print(zillow_interface.addresses)

google_form_interface = GoogleFormInterface()

for item in range(len(zillow_interface.prices)):
    google_form_interface.fill_up_form(zillow_interface.addresses[item], zillow_interface.prices[item], zillow_interface.links[item])
