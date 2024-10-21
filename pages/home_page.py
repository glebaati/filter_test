from selenium.webdriver.common.by import By
from steamtest.pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_FIELD_LOCATOR_XPATH = (By.XPATH, "//input[@id='store_nav_search_term']")
    SEARCH_BUTTON_LOCATOR_XPATH = (By.XPATH, "//a[@id='store_search_link']")
    def search_game(self, game_name):
        self.enter_text(*HomePage.SEARCH_FIELD_LOCATOR_XPATH, game_name)
        self.submit_search(*HomePage.SEARCH_BUTTON_LOCATOR_XPATH)



