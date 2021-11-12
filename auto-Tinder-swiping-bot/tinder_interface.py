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
            "login_front_page": '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a',
            "login_via_google": '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button',
            "next_button": '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button',
            "allow_button": '/html/body/div[2]/div/div/div/div/div[3]/button[1]',
            "not_interested_button": '/html/body/div[2]/div/div/div/div/div[3]/button[2]',
            "accept_cookie_button": '/html/body/div[1]/div/div[2]/div/div/div[1]/button',

        }


    def login(self, email, password):
        self.driver.find_element(By.XPATH, self.buttons_collection["login_front_page"]).click()
        sleep(2)
        window_before = self.driver.window_handles[0]
        self.driver.find_element(By.XPATH, self.buttons_collection["login_via_google"]).click()
        window_after = self.driver.window_handles[1]
        sleep(2)
        self.driver.switch_to.window(window_after)
        self.driver.find_element(By.NAME, "identifier").send_keys(email)
        self.driver.find_element(By.XPATH, self.buttons_collection["next_button"]).click()
        sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, self.buttons_collection["next_button"]).click()
        sleep(7)
        self.driver.switch_to.window(window_before)
        self.driver.find_element(By.XPATH, self.buttons_collection["allow_button"]).click()
        sleep(2)
        self.driver.find_element(By.XPATH, self.buttons_collection["not_interested_button"]).click()
        sleep(2)
        self.driver.find_element(By.XPATH, self.buttons_collection["accept_cookie_button"]).click()

