# from selenium.webdriver.common.by import By
#
# class HomePage():
#     #Locators
#     link_myaccount_xpath="//*[@id='top']/div[2]/div[2]/ul/li[2]/div/a/span"
#     link_register_linktext="Register"
#     link_login_linktext="Login"
#
#
#     #Constructors
#     def __init__(self,driver):
#         self.driver=driver
#
#     #Action methods
#     def clickMyAccount(self):
#         self.driver.find_element(By.XPATH,self.link_myaccount_xpath).click()
#
#     def clickRegister(self):
#         self.driver.find_element(By.LINK_TEXT,self.link_register_linktext).click()
#
#     def clickLogin(self):
#         self.driver.find_element(By.LINK_TEXT,self.link_login_linktext).click()
#
#



from selenium.webdriver.common.by import By

class HomePage():

    # Locator
    link_MyAcount_xpath="//span[normalize-space()='My Account']"
    link_Register_link_text="Register"
    link_login_link_text="Login"

    # Constructor
    def __init__(self,driver):                     # This is the constructor which will initiate the driver
        self.driver=driver

    # Action Methods

    def clickMyAcount(self):
        self.driver.find_element(By.XPATH,self.link_MyAcount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.link_Register_link_text).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.link_login_link_text).click()


