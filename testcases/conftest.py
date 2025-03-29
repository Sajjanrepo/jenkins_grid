import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    binary_path = ReadConfig.getFirefoxPath()

    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.binary_path = binary_path
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    yield driver

    driver.quit()
