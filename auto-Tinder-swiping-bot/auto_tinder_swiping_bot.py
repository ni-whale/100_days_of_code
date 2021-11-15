from tinder_interface import TinderInterface
from dotenv import load_dotenv
import os

# ---------------------------- CONSTANTS ------------------------------- #
load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# ---------------------------- MAIN ------------------------------- #
tinder_interface = TinderInterface()

tinder_interface.login(EMAIL, PASSWORD)

for _ in range(10):
    tinder_interface.auto_like()






