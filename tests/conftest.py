import pytest
from steamtest.Singleton import WebDriverSingleton
from steamtest.config_reader import ConfigReader

@pytest.fixture()
def driver(request):
    URL = ConfigReader().get_url()
    driver = WebDriverSingleton.get_driver(language=request.param)
    driver.get(URL)
    yield driver
    WebDriverSingleton.quit_driver()
