from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("/home/ni_whale/Documents/Working_space/projects/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com/")

login_button = driver.find_element(By.CSS_SELECTOR, "#Pos(r) Z(1)").click()
