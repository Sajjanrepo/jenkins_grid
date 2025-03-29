import pytest
from selenium import webdriver

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def driver(browser):
    logger = LogGen.loggen()

    driver = get_driver(browser, logger)

    if driver:
        logger.info(f"Launching {browser} Browser")
    else:
        logger.error(f"Invalid browser name {browser} provided")

    yield driver

    # Close the driver after test session ends
    if driver:
        logger.info(f"Closing {browser} Browser")
        driver.quit()


BROWSERS = [
    "chrome",
    "firefox"
]


@pytest.mark.parametrize("browser", BROWSERS)
def get_driver(browser, logger):
    firefox_path = ReadConfig.getFirefoxPath()
    chrome_path = ReadConfig.getchromePath()
    browser_name = browser
    if browser_name == "chrome":
        # Initialize the ChromeDriver

        # options = webdriver.ChromeOptions()
        # return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        # For parallel run on Selenium Grid
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_path
        return webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

    elif browser_name == "firefox":
        # Initialize the FirefoxDriver

        # options = webdriver.FirefoxOptions()
        # options.binary_path = firefox_path
        # return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        # For parallel run on Selenium Grid
        options = webdriver.FirefoxOptions()
        options.binary_location = firefox_path
        return webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

    else:
        logger.error("Invalid browser name. Please provide 'chrome', 'firefox'")
        return None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
