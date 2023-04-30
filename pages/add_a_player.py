import time

from pages.base_page import BasePage


class AddAPlayer(BasePage):

    page_title_xpath = "//header//h6"
    email_field_xpath = "//input[@name='email']"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    phone_field_xpath = "//input[@name='phone']"
    weight_field_xpath = "//input[@name='weight']"
    height_field_xpath = "//input[@name='height']"
    age_field_xpath = "//input[@name='age']"
    leg_field_xpath = "//input[@name='leg']"
    club_field_xpath = "//input[@name='club']"
    level_field_xpath = "//input[@name='level']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    second_position_field_xpath = "//input[@name='secondPosition']"
    district_field_xpath = "//*[contains(@id,'select-district')]"
    achievements_field_xpath = "//input[@name='achievements']"
    add_lang_button_xpath = "//button[@aria-label='Add language']"
    facebook_field_xpath = "//input[@name='webFB']"
    add_youtube_button_xpath = "//button[@aria-label='Add link to Youtube']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[@type='submit']//following-sibling::button"
    progress_bar_toaster_xpath = "//*[@role='alert']"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = 'Add player'
    expected_title_player_added = "Edit player Marian Kowalski"

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        test_title = self.get_page_title(self.add_a_player_url)
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert test_title == self.expected_title

    def player_added_title_of_the_page(self):
        self.wait_for_element_to_be_visible(self.progress_bar_toaster_xpath)
        assert self.driver.title == self.expected_title_player_added

