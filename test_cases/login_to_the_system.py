import os
import unittest
import time
from PIL import Image

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        #user_login.title_of_page()
        #user_login.check_header_of_box()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        self.driver.save_screenshot(
            "C:/Users/dziad/Documents/GitHub/Challenge_portfolio_paudzi/test_cases/screenshots/login_to_the_system/login_form_filled.png")
        Image.open(
            "C:/Users/dziad/Documents/GitHub/Challenge_portfolio_paudzi/test_cases/screenshots/login_to_the_system/login_form_filled.png").show()
        dashboard_page = Dashboard(self.driver)
        #dashboard_page.title_of_page()

    def test_log_in_with_invalid_data(self):
        user_login = LoginPage(self.driver)
        #user_login.title_of_page()
        #user_login.check_header_of_box()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234567')
        user_login.click_sign_in_button()
        #user_login.invalid_data()
        self.driver.save_screenshot(
            "C:/Users/dziad/Documents/GitHub/Challenge_portfolio_paudzi/test_cases/screenshots/login_to_the_system/invalid_data.png")
        Image.open(
            "C:/Users/dziad/Documents/GitHub/Challenge_portfolio_paudzi/test_cases/screenshots/login_to_the_system/invalid_data.png").show()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
