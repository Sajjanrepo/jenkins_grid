from pageobjects.basepage import BasePage


class DemostorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.demousername = "username"
        self.demopassword = "password"
        self.demologin = "login"
        self.demologout = "//a[normalize-space()='Log out']"
        self.myaccount = "//ul[@class='nav-menu']//a[normalize-space()='My account']"

    def open_demostore(self, url):
        self.open_url(url)

    def clickmyaccount(self):
        self.clickMyaccount(self.myaccount)

    def enterusername(self, query):
        self.username(self.demousername, query)

    def enterpassword(self, query):
        self.password(self.demopassword, query)

    def clickLoginBtn(self):
        self.login(self.demologin)

    def verify(self):
        return self.isLoginsuccess(self.demologout)
