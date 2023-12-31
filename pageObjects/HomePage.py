from selenium.webdriver.common.by import By

class HomePage():
    #Locators
    link_myaccount_xpath="//span[normalize-space()='My Account']"
    link_register_linktext="Register"
    link_login_linktext="Login"


    #Constructors
    def __init__(self,driver):
        self.driver=driver

    #Action methods
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.link_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.link_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.link_login_linktext).click()


