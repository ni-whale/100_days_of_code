from selenium import webdriver

chrome_driver_path = "/home/ni_whale/Documents/Working_space/projects/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.google.com")

