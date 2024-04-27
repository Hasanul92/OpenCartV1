# import os
# import time
#
# import pytest
#
# from pageObjects.HomePage import HomePage
# from pageObjects.AccountRegistration import AccountRegistrationPage
# from utilities import randomString
# from utilities.readProrperties import ReadConfig
# from utilities.customLogger import LogGen
#
#
# class Test_001_AccountReg():
#     baseURL=ReadConfig.getApplicationURL()
#     logger=LogGen.loggGenaration()       # for logging
#
#     @pytest.mark.sanity
#     def test_accountReg(self,setup):
#         self.logger.info("***test_001_AccountRegistration started***")
#         self.driver=setup
#         self.logger.info("Launching application")
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         # creating object for HomePage class (from pageObject package)
#         self.hp=HomePage(self.driver)
#         self.logger.info("Clicking on my account")
#         self.hp.clickMyAcount()
#         self.logger.info("Clicking on my account")
#         self.hp.clickRegister()
#
#         # creating object for HomePage class (from pageObject package)
#         self.logger.info("***Registration page started***")
#         self.regPage=AccountRegistrationPage(self.driver)
#         self.logger.info("Providing customer details for registration")
#         self.regPage.setFirstName("Hasan")
#         self.regPage.setLastName("Haque")
#         self.email=randomString.random_string_generator()+'@gmail.com'
#         self.regPage.setEmail(self.email)
#         self.regPage.setPassword("abcxyz")
#         self.regPage.clickPrivacyPolicy()
#         self.regPage.clickContinue()
#         self.confmsg=self.regPage.getConfirmationMsg()
#         # print(self.confmsg)
#
#         if self.confmsg=="Your Account Has Been Created!":
#             self.logger.info("***Account registration is passed***")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(os.getcwd()+"\\screenshots\\"+"test_accountReg.png")
#             # self.driver.save_screenshot(os.getcwd()+"\\screenshots\\test_accountReg.png")
#             self.logger.error("***Account registration is passed***")
#             self.driver.close()
#             assert False
#         self.logger.info("***test_001_AccountRegistration finished***")

import os
import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistration import AccountRegistrationPage
# from utilities import randomString
from utilities.randomString import random_string_generator
from utilities.readProrperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_AccountRegistration:
    baseurl=ReadConfig.getApplicationUrl()
    logger=LogGen.loggGenaration()

    @pytest.mark.sanity
    def test_AccountReg(self,setup):
        self.logger.info("***test_AccountReg started****")
        self.driver=setup
        self.logger.info("*****launching application url****")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(5)

        # Creating object of Home Page class (from pageObjects package)
        self.logger.info("****creating object of home page class****")
        self.hp=HomePage(self.driver)
        self.logger.info("****clicking on my acount*****")
        self.hp.clickMyAcount()
        self.logger.info("****clicking on register****")
        self.hp.clickRegister()

        # Creating object of Account Registration Page class (from pageObjects package)
        self.logger.info("****creating object of Accoun t registration page****")
        self.ar=AccountRegistrationPage(self.driver)
        self.logger.info("****providing customer details****")
        self.ar.setFname("Hasan")
        self.ar.setLname("Haque")
        self.email=random_string_generator()+"@gmail.com"
        self.ar.setEmail(self.email)
        self.ar.setPassword("Hasan@1234")
        self.ar.ClickPrivacy()
        self.ar.ClickContinue()
        self.ar.ConfMsg()
        self.confirmmsg=self.ar.ConfMsg()
        # print(self.confirmmsg)


        if self.confirmmsg=="Your Account Has Been Created!":
            self.logger.info("****test case passed****")
            self.driver.close()
            assert True
        else:
            # self.driver.save_screenshot(os.getcwd()+"\\screenshots\\"+"test_AccountReg.png")
            self.driver.save_screenshot(os.getcwd()+"\\screenshots\\test_accountReg.png")
            self.logger.info("****test case failed****")
            self.driver.close()
            assert False
        self.logger.info("****test_AccountReg finished****")










