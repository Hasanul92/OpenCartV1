import os.path
import time

from pageObjects.MyAccountPage import   MyAccountPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProrperties import ReadConfig
from utilities import XLUtils
from utilities.customLogger import LogGen


class Test_Login_DDT():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggGenaration()

    file=os.path.abspath(os.curdir)+"\\testData\\OpenCart_LoginData.xlsx"



    def test_Login_ddt(self,setup):
        self.logger.info("******** Starting test_003_DataDriven ********")
        self.rows=XLUtils.getRowCount(self.file,'Sheet1')
        list_status=[]

        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)       # Creating object for HomePage object class
        self.lp=LoginPage(self.driver)      # Creating object for LoginPage object class
        self.ma=MyAccountPage(self.driver)  # Creating object for MyAccountPage object class

        # Performing actions on HomePage
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        for r in range(2,self.rows+1):
            self.email=XLUtils.readData(self.file,'Sheet1',r,1)
            self.password=XLUtils.readData(self.file,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.file,'Sheet1',r,3)

            # Performing actions on LoginPage
            self.lp.setUsername(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.target=self.lp.MyAccountPage()
            print(self.target)

            if self.exp=='Valid':
                if self.target==True:
                    list_status.append('Pass')
                    # self.ma.clickMyAccount()
                    self.ma.clickLogout()
                else:
                    list_status.append('Fail')
                    # self.driver.save_screenshot(os.getcwd()+"\\screenshots\\"+"test_003_Login_ddt.png")

            elif self.exp=='Invalid':
                if self.target==True:
                    list_status.append('Fail')
                    self.ma.clickMyAccount()
                    self.ma.clickLogout()
                else:
                    list_status.append('Pass')
        self.driver.close()

        # Final validation
        if 'Fail' not in list_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of the test_003_LoginPage_DataDriven ********")

