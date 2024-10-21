from steamtest.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SearchResultPage(BasePage):
    FILTER_BUTTON_LOCATOR_XPATH = (By.XPATH, "//a[@id='sort_by_trigger']")
    PRICE_FILTER_BUTTON_LOCATOR_XPATH = (By.XPATH, "//a[@id='Price_DESC']")
    FIRST_GAME_LOCATOR_XPATH = (By.XPATH, "//div[contains(@class, 'responsive_search_name_combined')][1]")
    GAMES_TITLE_LOCATOR_XPATH = (By.XPATH, "//span[contains(@class, 'title')]")
    PRICES_LOCATOR_XPATH = (By.XPATH, "//div[(contains(text(), '$') or contains(text(), 'руб')) and not(contains(@class, 'original_price'))]")
    def apply_filter(self):
        self.click_element(*SearchResultPage.FILTER_BUTTON_LOCATOR_XPATH)
        self.click_element(*SearchResultPage.PRICE_FILTER_BUTTON_LOCATOR_XPATH)
        first = self.find_element(*SearchResultPage.FIRST_GAME_LOCATOR_XPATH)
        WebDriverWait(self.driver, self.timeout).until(EC.staleness_of(first))
    def get_games_list(self, n):
       games = self.find_elements(*SearchResultPage.GAMES_TITLE_LOCATOR_XPATH)
       return [game.text for game in games[:n]]

    def get_prices(self, n):
        prices_raw = [price.text for price in self.find_elements(*SearchResultPage.PRICES_LOCATOR_XPATH)]
        prices = []
        for price in prices_raw[:n]:
            if 'руб' or ' руб.' in price:
                price = price.strip().replace(' руб.', '').replace(',', '.').replace('руб', '')
                prices.append(float(price))
            elif '$' in price:
                price = price.strip().replace('$', '').replace(',', '.')
                prices.append(float(price))
        return prices
