from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv('/home/ni_whale/Documents/Working_space/projects/Python/storage.env')

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

date = "2021-01-02"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
hot100_web_page = response.text

soup = BeautifulSoup(hot100_web_page, "html.parser")

top100_songs = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song")]
print(top100_songs)

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

sp.user_playlist_create(
    user="ni-whale",
    name="Test",
    public=False,
    collaborative=False,
    description="Test attempt to create a playlist by the py_code"
)
