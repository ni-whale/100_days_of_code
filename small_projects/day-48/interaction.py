from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("/home/ni_whale/Documents/Working_space/projects/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")

# articlescount = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
# articles_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# articles_count.click()
# print(articles_count.text)

# all_portals = driver.find_element(By.LINK_TEXT, "Society")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Hello World!")
# search.send_keys(Keys.ENTER)

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Dr.")
fname.send_keys(Keys.ENTER)
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Acula")
lname.send_keys(Keys.ENTER)
email = driver.find_element(By.NAME, "email")
email.send_keys("Dr.Acula@gmail.com")
email.send_keys(Keys.ENTER)

driver.quit()
