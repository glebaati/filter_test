from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from steamtest.config_reader import ConfigReader


class BasePage:
    TIMEOUT = ConfigReader().get_value("timeout")

    def __init__(self, driver):
        self.driver = driver
        self.timeout = self.TIMEOUT

    def click_element(self, by, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, locator))).click()

    def submit_search(self, by, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, locator))).submit()

    def enter_text(self, by, locator, text):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, locator))).send_keys(text)
