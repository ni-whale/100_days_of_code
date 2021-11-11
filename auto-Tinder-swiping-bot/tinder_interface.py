from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class TinderInterface:
    def __init__(self):
        service = Service("/home/ni_whale/Documents/Working_space/projects/chromedriver_linux64/chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://tinder.com/")

        self.buttons_collection = {
            "login_front_page": "'//*[@id=\"q-274726726\"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'",
            "login_via_google": '//*[@id="q-53386290"]/div/div/div[1]/div/div[3]/span/div[1]/div/button'
        }

    def login(self, email, password):
        print(self.buttons_collection["login_front_page"])
        print(self.buttons_collection["login_via_google"])
        self.driver.find_element(By.XPATH, self.buttons_collection["login_front_page"])
        # sleep(2)
        # self.driver.find_element(By.XPATH, self.buttons_collection["login_via_google"])
