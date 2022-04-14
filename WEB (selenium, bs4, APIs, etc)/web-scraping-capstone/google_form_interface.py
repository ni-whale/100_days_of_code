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
        self.driver.get('https://forms.gle/QfoYgQN21fGhL6sn6')

        self.fields_collection = {
            "address_field": "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > "
                             "div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div > "
                             "div.freebirdFormviewerComponentsQuestionTextRoot > div > "
                             "div.quantumWizTextinputPaperinputMainContent.exportContent > div > "
                             "div.quantumWizTextinputPaperinputInputArea > input",
            "price_field": "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > "
                           "div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div > "
                           "div.freebirdFormviewerComponentsQuestionTextRoot > div > "
                           "div.quantumWizTextinputPaperinputMainContent.exportContent > div > "
                           "div.quantumWizTextinputPaperinputInputArea > input",
            "link_field": "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > "
                          "div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > "
                          "div.freebirdFormviewerComponentsQuestionTextRoot > div > "
                          "div.quantumWizTextinputPaperinputMainContent.exportContent > div > "
                          "div.quantumWizTextinputPaperinputInputArea > input",
            "submit_button": "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > "
                             "div.freebirdFormviewerViewNavigationNavControls > "
                             "div.freebirdFormviewerViewNavigationButtonsAndProgress.hasClearButton > "
                             "div.freebirdFormviewerViewNavigationLeftButtons > div > span > span ",
            "submit_another_reply_button": "body > div.freebirdFormviewerViewFormContentWrapper > div:nth-child(2) > "
                                           "div.freebirdFormviewerViewFormCard.exportFormCard > div > "
                                           "div.freebirdFormviewerViewResponseLinksContainer > a "
        }

    def fill_up_form(self, address, price, link):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.fields_collection["address_field"]).send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, self.fields_collection["price_field"]).send_keys(price)
        self.driver.find_element(By.CSS_SELECTOR, self.fields_collection["link_field"]).send_keys(link)
        self.driver.find_element(By.CSS_SELECTOR, self.fields_collection["submit_button"]).click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, self.fields_collection["submit_another_reply_button"]).click()
