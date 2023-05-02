import os
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddAPlayer
from PIL import Image


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_to_database(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_add_a_player_button()
        add_a_player = AddAPlayer(self.driver)
        add_a_player.title_of_page()
        add_a_player.type_in_email('test@test.pl')
        add_a_player.type_in_name("Marian")
        add_a_player.type_in_surname("Kowalski")
        add_a_player.type_in_phone("555555555")
        add_a_player.type_in_weight('87')
        add_a_player.type_in_height('187')
        add_a_player.type_in_age('01-01-1999')
        add_a_player.select_leg("left")
        add_a_player.type_in_main_position('striker')
        add_a_player.type_in_second_position('Winger')
        add_a_player.select_district("Lower Silesia")
        add_a_player.type_in_achievements("Bestfromthebest")
        add_a_player.click_submit_button()
        add_a_player.player_added_title_of_the_page()
        self.driver.save_screenshot(
            "C:/Users/dziad/Documents/GitHub/Challenge_portfolio_paudzi/test_cases/screenshots/add_a_new_player/added_player.png")
        Image.open(
            "C:/Users/dziad/Documents/GitHub/Challenge_portfolio_paudzi/test_cases/screenshots/add_a_new_player/added_player.png").show()


    @classmethod
    def tearDown(self):
        self.driver.quit()

