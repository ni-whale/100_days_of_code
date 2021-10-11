from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import spotipy

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

date = "2021-01-02"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
hot100_web_page = response.text

soup = BeautifulSoup(hot100_web_page, "html.parser")

top100_songs = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song")]
print(top100_songs)





