from cookie_interface import CookieInterface
import time

cookie_interface = CookieInterface()

estimated_time = time.time() + 60.0
shopping_time = time.time() + 5.0

# print(f"estimated time = {estimated_time} | shopping_time = {shopping_time}")

while time.time() < estimated_time:
    cookie_interface.cookie_button_click()
    if time.time() > shopping_time:
        for menu_item in cookie_interface.get_cookie_menu():
            if int(cookie_interface.get_money()) >= int(menu_item[1]):
                print(f"You should buy: {menu_item}")
        shopping_time = time.time() + 5.0
        # print(f"new shopping time = {shopping_time}")

cookie_interface.quit()

