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
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_option_xpath = "//div[3]/ul/li[1]"
    left_leg_option_xpath = "//div[3]/ul/li[2]"
    club_field_xpath = "//input[@name='club']"
    level_field_xpath = "//input[@name='level']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    second_position_field_xpath = "//input[@name='secondPosition']"
    district_field_xpath = "//*[contains(@id,'select-district')]"
    lower_silesia_distr_xpath ="//li[1]"
    kuyavia_pomerania_distr_xpath = "//li[2]"
    lublin_distr_xpath = "//li[3]"
    lubusz_distr_xpath= "//li[4]"
    lodz_distr_xpath= "//li[5]"
    lesser_poland_distr_xpath= "//li[6]"
    masovia_distr_xpath= "//li[7]"
    opole_distr_xpath= "//li[8]"
    subcarpathia_distr_xpath= "//li[9]"
    podlaskie_distr_xpath= "//li[10]"
    pomerania_distr_xpath= "//li[11]"
    silesia_distr_xpath= "//li[12]"
    holy_cross_province_distr_xpath= "//li[13]"
    warmia_masuria_distr_xpath= "//li[14]"
    greater_poland_distr_xpath= "//li[15]"
    west_pomerania_distr_xpath= "//li[16]"
    district_xpath_map = {
        "Lower Silesia": "//li[1]",
        "Kuyavia-Pomerania": kuyavia_pomerania_distr_xpath,
        "Lublin": lublin_distr_xpath,
        "Lubusz": lubusz_distr_xpath,
        "Łódź": lodz_distr_xpath,
        "Lesser Poland": lesser_poland_distr_xpath,
        "Masovia": masovia_distr_xpath,
        "Opole": opole_distr_xpath,
        "Subcarpathia": subcarpathia_distr_xpath,
        "Podlaskie": podlaskie_distr_xpath,
        "Pomerania": pomerania_distr_xpath,
        "Silesia": silesia_distr_xpath,
        "Holy Cross Province": holy_cross_province_distr_xpath,
        "Warmia-Masuria": warmia_masuria_distr_xpath,
        "Greater Poland": greater_poland_distr_xpath,
        "West Pomerania": west_pomerania_distr_xpath

    }
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

    def select_leg(self, leg):
        self.wait_for_element_to_be_clickable(self.leg_dropdown_xpath)
        self.click_on_the_element(self.leg_dropdown_xpath)
        if leg == "left":
            self.wait_for_element_to_be_clickable(self.left_leg_option_xpath)
            self.click_on_the_element(self.left_leg_option_xpath)
        else:
            self.wait_for_element_to_be_clickable(self.right_leg_option_xpath)
            self.click_on_the_element(self.right_leg_option_xpath)

    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_field_xpath, second_position)

    def select_district(self, district):
        self.wait_for_element_to_be_clickable(self.district_field_xpath)
        self.click_on_the_element(self.district_field_xpath)
        xpath = self.district_xpath_map.get(district)
        if xpath:
            self.wait_for_element_to_be_clickable(xpath)
            self.click_on_the_element(xpath)

    def type_in_achievements(self,achievements):
        self.field_send_keys(self.achievements_field_xpath, achievements)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        test_title = self.get_page_title(self.add_a_player_url)
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert test_title == self.expected_title

    def player_added_title_of_the_page(self):
        self.wait_for_element_to_be_visible(self.progress_bar_toaster_xpath)
        assert self.driver.title == self.expected_title_player_added




'''
    def select_district(self,district):
        if district == "Lower Silesia":
            self.wait_for_element_to_be_clickable(self.lower_silesia_distr_xpath)
            self.click_on_the_element(self.lower_silesia_distr_xpath)
        elif district == "Kuyavia-Pomerania ":
            self.wait_for_element_to_be_clickable(self.kuyavia_pomerania_distr_xpath)
            self.click_on_the_element(self.kuyavia_pomerania_distr_xpath)
        elif district == "Lublin ":
            self.wait_for_element_to_be_clickable(self.lubusz_distr_xpath)
            self.click_on_the_element(self.lublin_distr_xpath)
'''