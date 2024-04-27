import time

from utilities.readProrperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils

class Test_Login_DDT:
    baseurl=ReadConfig.getApplicationUrl()
    logger=LogGen.loggGenaration()
    file_path=r"C:\Users\Me\PycharmProjects\OpenCartV1\testData\OpenCart_LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.logger.info("******Starting test_005_Login_ddt1******")
        self.driver=setup
        self.logger.info("*****Launching application url*****")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("****Creating object of HomePage,LoginPage,MyAccountPage")
        self.hp=HomePage(self.driver)             # Creating object of Home page class
        self.lp=LoginPage(self.driver)            # Creating object of Login page class
        self.ma=MyAccountPage(self.driver)        # Creating object of MyAccount page

        # Performing actions on Home page
        self.logger.info("****Performing actions on Home Page*****")
        self.hp.clickMyAcount()
        self.hp.clickLogin()

        # Reading data from excel file
        self.logger.info('*****Counting total no. of rows from excel sheet******')
        self.rows=XLUtils.getRowCount(self.file_path,'Sheet1')
        list_status=[]

        self.logger.info('****Reading data from excel sheet****')
        for r in range(2,self.rows+1):
            self.email=XLUtils.readData(self.file_path,'Sheet1',r,1)
            self.pswd=XLUtils.readData(self.file_path,'Sheet1',r,2)
            self.exp_result=XLUtils.readData(self.file_path,'Sheet1',r,3)

            # Performing actions on Login page
            self.logger.info('*****Performiong actions on LoginPage*****')
            self.lp.setUsername(self.email)
            self.lp.setPassword(self.pswd)
            self.lp.clickLogin()
            time.sleep(5)
            self.targetPage=self.lp.MyAccountPage()

            self.logger.info('*****Validating test cases****')
            if self.exp_result=='Valid':
                if self.targetPage==True:
                    list_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    list_status.append('Fail')

            elif self.exp_result=='Invalid':
                if self.targetPage==True:
                    list_status.append('Fail')
                    self.ma.clickMyAccount()
                    self.ma.clickLogout()
                else:
                    list_status.append('Pass')
            self.driver.close()

            if 'Fail' in list_status:
                assert True
            else:
                assert False

        self.logger.info('****end of the test_005_Login_ddt1******')




