from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class WebDriverSingleton:
    _driver = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    @staticmethod
    def get_driver(language):
        if WebDriverSingleton._driver is None:
            chrome_options = Options()
            chrome_options.add_argument(f'--lang={language}')
            WebDriverSingleton._driver = webdriver.Chrome(options=chrome_options)
            WebDriverSingleton._driver.maximize_window()
        return WebDriverSingleton._driver

    @staticmethod
    def quit_driver():
        if WebDriverSingleton._driver:
            WebDriverSingleton._driver.quit()
            WebDriverSingleton._driver = None