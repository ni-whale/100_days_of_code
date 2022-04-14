from bs4 import BeautifulSoup
import requests
import re

class ZillowInterface:
    def __init__(self):
        links_collection = {
            0: "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A"
               "-122.83501662207031%2C%22east%22%3A-122.03164137792969%2C%22south%22%3A37.54426829428638%2C%22north"
               "%22%3A37.9991021505461%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B"
               "%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C"
               "%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22"
               "%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn"
               "%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22"
               "%3Atrue%2C%22mapZoom%22%3A11%7D"}

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/95.0.4638.69 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

        self.links = []
        self.addresses = []
        self.prices = []

        self.response = requests.get(links_collection[0], headers=headers)
        zillow_web_page = self.response.text
        self.soup = BeautifulSoup(zillow_web_page, "html.parser")



    def find_elements(self):
        list_of_results = self.soup.find_all(name="ul", class_="photo-cards")
        for item in list_of_results:
            prices = self.soup.find_all(name="div", class_="list-card-price")
            addresses = self.soup.find_all(name="address", class_="list-card-addr")
            links = self.soup.find_all(name="a", class_="list-card-link")

        for address in addresses:
            self.addresses.append(address.text)

        for link in links:
            if re.match("/b/", link['href']):
                self.links.append(f"https://www.zillow.com{link['href']}")
            else:
                self.links.append(link['href'])
        self.links = set(self.links)
        self.links = list(self.links)

        for price in prices:
            self.prices.append(price.text)




