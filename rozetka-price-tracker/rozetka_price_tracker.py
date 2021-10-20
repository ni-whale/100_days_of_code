import requests
from bs4 import BeautifulSoup

LINK = "https://rozetka.com.ua/samsung_sm_r180nzwasek/p238811953/"

headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Encoding': 'gzip, deflate',
}
# from requests_html import HTMLSession
#
# WEB_PAGE = "https://rozetka.com.ua/samsung_sm_r180nzwasek/p238811953/"
# WEB_FILE = "rozetka_page.html"
#
#
# # Using requests_html to render JavaScript
# def get_web_page():
#     # create an HTML Session object
#     session = HTMLSession()
#     # Use the object above to connect to needed webpage
#     response = session.get(WEB_PAGE)
#     # Run JavaScript code on webpage
#     response.html.render()
#
#     # Save web page to file
#     with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
#         fp.write(response.html.html)
#
#
# def read_web_file():
#     try:
#         open(WEB_FILE)
#     except FileNotFoundError:
#         get_web_page()
#     finally:
#         # Read the web page from file
#         with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
#             content = fp.read()
#         return BeautifulSoup(content, "html.parser")
#
#
# # Read web file if it exists, load from internet if it doesn't exist
# result = read_web_file()

with open("rozetka_page.html", "r") as data_file:
    rozetka_site = data_file.read()

soup = BeautifulSoup(rozetka_site, "html.parser")

price = soup.find(name="p", class_="product-prices__big")
price = price.text.split()
print(price[0]+price[1].split("₴")[0])
