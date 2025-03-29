import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def driver(request):
    binary_path = ReadConfig.getFirefoxPath()
    browser = request.param
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.binary_path = binary_path
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    else:
        raise ValueError("Unsupported browser: " + browser)

    driver.maximize_window()
    yield driver

    driver.quit()
