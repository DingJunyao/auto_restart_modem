import os
import time

import dotenv
from selenium import webdriver

from nopo import El, By, Pg

dotenv.load_dotenv()

ROUTER_ADDR = os.getenv("ROUTER_ADDR")
ROUTER_URL_PREFIX = f'http://{ROUTER_ADDR}'
USER_MANE = os.getenv("USER_MANE")
PASSWORD = os.getenv("PASSWORD")


class LoginPage(Pg):

    # Define like Selenium
    username_box = El(By.ID, 'login_username')
    password_box = El(By.ID, 'login_password')
    login_btn = El(By.CSS_SELECTOR, '#login_form > button')

    def login(self, username: str, password: str):
        self.username_box.send_keys(username)
        self.password_box.send_keys(password)
        self.login_btn.click()


class HomePage(Pg):
    # Define like Selenium
    restart_btn = El(By.ID,'menu_action_restart')
    confirm_btn = El(By.ID, 'confirm')

    def restart(self):
        self.restart_btn.click()
        self.confirm_btn.click()


def restart_modem():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(ROUTER_URL_PREFIX)
    login_page = LoginPage(driver)
    login_page.login(USER_MANE, PASSWORD)
    home_page = HomePage(driver)
    home_page.restart()
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    restart_modem()
