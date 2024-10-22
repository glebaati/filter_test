from steamtest.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    SEARCH_FIELD_LOCATOR_XPATH = (By.ID, 'store_nav_search_term')
    SEARCH_BUTTON_LOCATOR_XPATH = (By.ID, 'store_search_link')
    LOAD_ELEMENT_LOCATOR_ID = (By.ID, "home_maincap_v7")

    def search_game(self, game_name):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.SEARCH_FIELD_LOCATOR_XPATH)).send_keys(game_name)
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON_LOCATOR_XPATH)).submit()

    def wait_loaded_page(self):
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(self.LOAD_ELEMENT_LOCATOR_ID))
