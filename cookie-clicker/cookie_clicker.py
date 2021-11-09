from cookie_interface import CookieInterface
import time

cookie_interface = CookieInterface()

estimated_time = time.time() + 60.0 * 5
shopping_time = time.time() + 5.0

while time.time() < estimated_time:
    cookie_interface.cookie_button_click()
    if time.time() > shopping_time:
        available_items = []
        for menu_item in cookie_interface.get_cookie_menu():
            if int(cookie_interface.get_money()) >= int(menu_item[1]):
                available_items.append(int(menu_item[1]))
        cookie_interface.buy_item(cookie_interface.get_cookie_menu(), available_items)
        shopping_time = time.time() + 5.0

cookie_interface.get_cps()

cookie_interface.quit()

