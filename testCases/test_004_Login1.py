import os.path

from utilities.readProrperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.Login1Page import LoginPage
from utilities.customLogger import LogGen

class Test_LoginPage:
    baseUrl=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUserName()
    pswd=ReadConfig.getPassword()
    logger=LogGen.loggGenaration()



    def test_Login(self,setup):
        self.logger.info("test_004_Login1 is Started .....")
        self.driver=setup
        self.logger.info("Launching application url....")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
      # creating object of home page class
        self.logger.info("Creating object of Home page class....")
        self.hp=HomePage(self.driver)
        self.hp.clickMyAcount()
        self.hp.clickLogin()
      # creating object of login page class
        self.logger.info("Creating object of login page class")
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.pswd)
        self.lp.ClickLogin()
        self.targetPage=self.lp.MyAccountPage()

        if self.targetPage==True:
            print("test case is passed...")
            self.driver.close()
            assert True
        else:
            # self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\test_Login.png")
            self.driver.save_screenshot(os.getcwd()+"\\screenshots\\test_Login.png")
            print("test case is failed...")
            self.driver.close()
            assert False

        self.logger.info("test_004_Login1 is finished....")


