from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CookieInterface():
    def __init__(self):
        service = Service("/home/ni_whale/Documents/Working_space/projects/chromedriver_linux64/chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://orteil.dashnet.org/experiments/cookie/")

    def cookie_button_click(self):
        cookie_button = self.driver.find_element(By.CSS_SELECTOR, "#cookie")
        cookie_button.click()

    def get_cookie_menu(self):
        cookie_store = self.driver.find_elements(By.CSS_SELECTOR, "#store b")
        cookie_store_menu_list = []
        for position in cookie_store[:-1:]:  # To avoid empty "[]" element in the list
            cookie_store_menu_list.append(position.text.split(" - "))

        for price in cookie_store_menu_list:
            price[1] = price[1].replace(",", "")  # removing comas in the price for each element of the menu

        return cookie_store_menu_list

    def get_money(self):
        money = self.driver.find_element(By.CSS_SELECTOR, "#money").text.replace(",", "")
        return money



    def quit(self):
        self.driver.quit()
