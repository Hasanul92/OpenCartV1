from selenium.webdriver.common.by import By


class MyAccountPage:

    # Locators
    link_MyAccount_Xpath="//span[normalize-space()='My Account']"
    link_logout_Link_Text="Logout"

    # Constructors
    def __init__(self,driver):
        self.driver=driver

    # Action Methods
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.link_MyAccount_Xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_Link_Text).click()
