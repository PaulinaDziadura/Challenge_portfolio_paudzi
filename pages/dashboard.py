from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    scouts_panel_logo_background_image_xpath = "//*[@title='Logo Scouts Panel']"
    dev_team_contact_button_xpath = "//*[text()='Dev team contact']"
    shortcuts_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/h2"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    activity_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h2"
    last_created_player_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h6[1]"
    last_created_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h6[2]"
    last_updated_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
    last_created_match_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h6[3]"
    last_created_match_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
    last_updated_match_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h6[4]"
    last_updated_match_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[4]/button/span[1]"
    last_updated_report_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h6[5]"
    last_updated_report_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"


pass