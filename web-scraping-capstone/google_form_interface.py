from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class GoogleFormInterface:

    def __init__(self):
        service = Service("/home/ni_whale/Documents/Working_space/projects/chromedriver_linux64/chromedriver")
        self.driver = webdriver.Chrome(service=service)
        # self.driver.get('https://forms.gle/QfoYgQN21fGhL6sn6')