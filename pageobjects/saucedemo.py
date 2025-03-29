from pageobjects.basepage import BasePage


class SaucedemoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sauceusername = "user-name"
        self.saucepassword = "password"
        self.saucelogin = "login-button"
        self.sauceproduct = "//span[@class='title']"

    def open_sauceLabs(self, url):
        self.open_url(url)

    def enterusername(self, query):
        self.username(self.sauceusername, query)

    def enterpassword(self, query):
        self.password(self.saucepassword, query)

    def clickLoginBtn(self):
        self.login(self.saucelogin)

    def verify(self):
        return self.isLoginSuccess_saucelab(self.sauceproduct)
