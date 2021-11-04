from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("/home/ni_whale/Documents/Working_space/projects/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

current_time = time.time()
estimated_time = current_time + 60.0
shopping_time = current_time + 5.0

cookie_button = driver.find_element(By.CSS_SELECTOR, "#cookie")

print(f"estimated time = {estimated_time} | shopping_time = {shopping_time}")

while time.time() < estimated_time:
    cookie_button.click()
    if time.time() > shopping_time:
        print("time to buy something")
        shopping_time = time.time() + 5.0
        print(f"new shopping time = {shopping_time}")

driver.quit()
