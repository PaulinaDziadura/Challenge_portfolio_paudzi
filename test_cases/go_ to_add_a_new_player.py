import os
import unittest
import time

from selenium import webdriver

from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestGoToAddNewPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_go_to_add_a_new_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        time.sleep(15)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player_button()
        time.sleep(15)
        add_player = AddAPlayer(self.driver)
        add_player.title_of_page()
        """
        add_player.type_in_email('test@test.pl')
        add_player.type_in_name('Marian')
        add_player.type_in_surname('Kowalski')
        add_player.type_in_age('01-01-1999')
        add_player.type_in_main_position('striker')
        add_player.click_submit_button()
        """

    @classmethod
    def tearDown(self):
        self.driver.quit()
