from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from steamtest.config_reader import ConfigReader


class WebDriverSingleton:
    _driver = None

    def __new__(cls, language):
        if not cls._driver:
            chrome_options = Options()
            for option in ConfigReader().get_value("chrome_options").keys():
                if option == "language":
                    chrome_options.add_argument(f"--lang={language}")
            cls._driver = webdriver.Chrome(options=chrome_options)
            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def get_driver(cls):
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
