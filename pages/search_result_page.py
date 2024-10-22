from steamtest.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from steamtest.config_reader import ConfigReader


class SearchResultPage(BasePage):
    FILTER_BUTTON_LOCATOR_XPATH = (By.ID, 'sort_by_trigger')
    PRICE_FILTER_BUTTON_LOCATOR_XPATH = (By.ID, 'Price_DESC')
    FIRST_GAME_LOCATOR_XPATH = (By.XPATH, "//div[contains(@class, 'responsive_search_name_combined')][1]")
    GAMES_TITLE_LOCATOR_XPATH = (By.XPATH, "//span[contains(@class, 'title')]")
    PRICES_LOCATOR_XPATH = (
        By.XPATH,
        "//div[contains(@class, 'discount_prices')]//div[contains(text(), '') and not(contains(@class, 'original_price') or contains(@class, 'your_price'))]")
    LOAD_ELEMENT_LOCATOR_XPATH = (By.XPATH, "//div[contains(@id, 'searchtag')]")
    BACKGROUND_OPACITY_LOCATOR_XPATH = (
        By.XPATH, "//div[contains(@id, 'search_result_container') and contains(@style, 'opacity: 0.5;')]")

    def wait_loaded_page(self):
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(self.LOAD_ELEMENT_LOCATOR_XPATH))

    def apply_filter(self):
        self.driver.set_network_conditions(**ConfigReader()["network_options"])
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.FILTER_BUTTON_LOCATOR_XPATH)).click()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.PRICE_FILTER_BUTTON_LOCATOR_XPATH)).click()
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.BACKGROUND_OPACITY_LOCATOR_XPATH))
        WebDriverWait(self.driver, self.timeout).until_not(
            EC.presence_of_element_located(self.BACKGROUND_OPACITY_LOCATOR_XPATH))

    def get_games_list(self, n):
        games = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(self.GAMES_TITLE_LOCATOR_XPATH))
        return [game.text for game in games[:n]]

    def get_prices(self, n):
        prices_raw = [price.text for price in WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(self.PRICES_LOCATOR_XPATH))]
        prices = []
        for price in prices_raw[:n]:
            match = re.search(r'\d+[\.,]?\d*', price)
            if match:
                price = float(match.group().replace(',', '.'))
                prices.append(price)
        return prices
