from steamtest.config_reader import ConfigReader


class BasePage:
    TIMEOUT = ConfigReader()["timeout"]

    def __init__(self, driver):
        self.driver = driver
        self.timeout = self.TIMEOUT
