from pageobjects.demostore import DemostorePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestDemostore:

    baseURL = ReadConfig.getdemostoreURL()
    username = ReadConfig.getdemostoreUseremail()
    password = ReadConfig.getdemostorePassword()
    logger = LogGen.loggen()

    def test_demostoreLogin(self, driver):
        self.driver = driver
        self.demostore = DemostorePage(self.driver)

        self.logger.info("Enter the base url of Demostore")
        self.demostore.open_demostore(self.baseURL)
        self.logger.debug(f"Entered the base url: {self.baseURL}")

        self.logger.info("Click Myaccount in homepage")
        self.demostore.clickmyaccount()
        self.logger.debug(f"Clicked the My Account link on homepage")

        self.logger.info("Enter the username of Demostore")
        self.demostore.enterusername(self.username)
        self.logger.debug(f"Entered the username: {self.username}")

        self.logger.info("Enter the password of Demostore")
        self.demostore.enterpassword(self.password)
        self.logger.debug(f"Entered the password: {self.password}")

        self.logger.info("Click the login button")
        self.demostore.clickLoginBtn()
        self.logger.info("Clicked the login button")

        self.logger.info("Verify the login")
        result = self.demostore.verify()
        if result:
            self.logger.info("Login is succesfull")
            assert True

        else:
            self.logger.error("Login is Unsuccessfull")
            assert False






