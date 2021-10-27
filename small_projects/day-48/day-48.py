from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/home/ni_whale/Documents/Working_space/projects/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(len(event_times))}

print(events)

driver.quit()
