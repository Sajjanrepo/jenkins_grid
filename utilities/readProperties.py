import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + '\\configurations\\config.ini')


class ReadConfig:

    @staticmethod
    def getsaucedemoURL():
        saudemourl = config.get('url', 'saucedemo_baseURL')
        return saudemourl

    @staticmethod
    def getdemostoreURL():
        demostoreurl = config.get('url', 'demostorebaseURL')
        return demostoreurl

    @staticmethod
    def getdemostoreUseremail():
        demousername = config.get('credentials', 'demostore_email')
        return demousername

    @staticmethod
    def getdemostorePassword():
        password = config.get('credentials', 'demostore_password')
        return password

    @staticmethod
    def getsauceUseremail():
        sauceusername = config.get('credentials', 'saucedemo_username')
        return sauceusername

    @staticmethod
    def getsaucePassword():
        saucepassword = config.get('credentials', 'saucedemo_password')
        return saucepassword

    @staticmethod
    def getFirefoxPath():
        firefox_path = config.get('drivers', 'firefox_path')
        return firefox_path

    @staticmethod
    def getchromePath():
        chrome_path = config.get('drivers', 'chrome_path')
        return chrome_path
