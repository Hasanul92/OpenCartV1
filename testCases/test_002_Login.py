import os.path

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProrperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggGenaration()

    user=ReadConfig.getUserEmail()
    password=ReadConfig.getUserPassword()

    @pytest.mark.sanity
    def test_Login(self,setup):
        self.logger.info("***** Starting Test_002_Login ******")
        self.driver=setup               # Launching the browser
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    # creating object for HomePage class (from pageObject package)
        self.logger.info("***** Creating object for HomePage *****")
        self.hp=HomePage(self.driver)           # passing the driver(self.driver) in argument
        self.logger.info("***** Clicking on my account *****")
        self.hp.clickMyAccount()
        self.hp.clickLogin()

    # creating object for LoginPage class (from pageObject package)
        self.logger.info("***** Creating object for LoginPage *****")
        self.lp=LoginPage(self.driver)          # passing the driver(self.driver) in argument

        self.lp.setUsername(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.targetPage=self.lp.MyAccountPage()
        if self.targetPage==True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_Login.png")
            # self.driver.save_screenshot(os.getcwd()+"\\screenshots\\"+"test_accountReg.png")
            self.driver.close()
            assert False


        self.logger.info("******* End of the Test_002_Login ***********")
