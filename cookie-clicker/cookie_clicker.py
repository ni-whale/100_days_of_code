from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from threading import Timer

service = Service("/home/ni_whale/Documents/Working_space/projects/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.CSS_SELECTOR, "#cookie")

store = driver.find_elements(By.CSS_SELECTOR, "#store b")
money = driver.find_element(By.CSS_SELECTOR, "#money").text

for thing in store[:-1:]:  # added slice because split return additional element ['']
    print(thing.text.split(" - "))



# driver.quit()