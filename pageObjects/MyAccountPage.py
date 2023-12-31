from selenium.webdriver.common.by import By


class MyAccountPage():
    #locator
    link_myaccount_xpath="//span[normalize-space()='My Account']"
    link_logout_xpath="//a[@class='dropdown-item'][normalize-space()='Logout']"

    #constructor
    def __init__(self,driver):
        self.driver=driver

    # Action method
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.link_myaccount_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()
