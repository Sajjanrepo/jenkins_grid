from pageobjects.saucedemo import SaucedemoPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestSaucelab:

    baseURL = ReadConfig.getsaucedemoURL()
    username = ReadConfig.getsauceUseremail()
    password = ReadConfig.getsaucePassword()
    logger = LogGen.loggen()

    def test_saucelabLogin(self, driver):
        self.driver = driver
        self.saucedemo = SaucedemoPage(self.driver)

        self.logger.info("Enter the base url of Sauce Labs")
        self.saucedemo.open_sauceLabs(self.baseURL)
        self.logger.debug(f"Entered the base url: {self.baseURL}")

        self.logger.info("Enter the username of Sauce Labs")
        self.saucedemo.enterusername(self.username)
        self.logger.debug(f"Entered the username: {self.username}")

        self.logger.info("Enter the password of Sauce Labs")
        self.saucedemo.enterpassword(self.password)
        self.logger.debug(f"Entered the password: {self.password}")

        self.logger.info("Click the login button")
        self.saucedemo.clickLoginBtn()
        self.logger.info("Clicked the login button")

        self.logger.info("Verify the login")
        result= self.saucedemo.verify()
        if result:
            self.logger.info("Login is succesfull")
            self.driver.close()
            assert True

        else:
            self.logger.error("Login is Unsuccessfull")
            self.driver.close()
            assert False






