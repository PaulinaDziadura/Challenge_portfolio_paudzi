from pages.base_page import BasePage


class AddMatchForm(BasePage):
    my_team_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    enemy_team_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    my_team_score_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    enemy_team_score_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    t_shirt_color_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    league_input_xpath =  "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[8]/div/div/input"
    time_played_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    number_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    web_match_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    general_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    rating_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"
    clear_button_xpath =  "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"



pass