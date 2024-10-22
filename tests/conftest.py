import pytest
from steamtest.singleton import WebDriverSingleton
from steamtest.config_reader import ConfigReader


@pytest.fixture()
def driver(request):
    URL = ConfigReader()["URL"]
    driver = WebDriverSingleton(language=request.param)
    driver.get(URL)
    yield driver
    WebDriverSingleton.quit_driver()
