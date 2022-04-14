from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
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
            "like_button": '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button',
            "like_button_alt": '//*[@id="u1186853273"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button',
            "back_to_tinder": '/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/button',
            "not_interested": '/html/body/div[2]/div/div/div[2]/button[2]'
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

    def auto_like(self):
        try:
            sleep(2)
            self.driver.find_element(By.XPATH, self.buttons_collection["like_button"]).click()
        except NoSuchElementException:
            sleep(2)
            try:
                add_home_dismiss = self.driver.find_element(By.CSS_SELECTOR,
                    "#u1408193709 > div > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\).Px\(24px\)--s > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\)")
                add_home_dismiss.click()
                sleep(2)
            except:
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_RIGHT)
        except ElementClickInterceptedException:
            try:
                self.driver.find_element(By.XPATH, self.buttons_collection["back_to_tinder"]).click()
                sleep(2)
            except:
                print("Take a rest.")
                self.driver.quit()


    def quit(self):
        self.driver.quit()
