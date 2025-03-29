from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def clickMyaccount(self, locator):
        my_account = self.driver.find_element(By.XPATH, locator)
        my_account.click()

    def username(self, locator, query):
        username_box = self.driver.find_element(By.NAME, locator)
        username_box.clear()
        username_box.send_keys(query)

    def password(self, locator, query):
        password_box = self.driver.find_element(By.NAME, locator)
        password_box.clear()
        password_box.send_keys(query)

    def login(self, locator):
        login_btn = self.driver.find_element(By.NAME, locator)
        login_btn.click()

    def isLoginsuccess(self, locator):
        try:
            result_text = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, locator))).text
        except TimeoutException:
            return False

        if result_text == "Log out":
            return True
        else:
            return False

    def isLoginSuccess_saucelab(self, locator):
        try:
            result_text = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, locator))).text
        except TimeoutException:
            return False

        if result_text == "Products":
            return True
        else:
            return False
