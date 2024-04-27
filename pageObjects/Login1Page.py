import time

from selenium.webdriver.common.by import By


class LoginPage:

    # Locators
    text_username_ID="input-email"
    text_password_ID="input-password"
    button_login_Xpath="//button[@type='submit']"
    msg_MyAccount_Xpath="//h2[normalize-space()='My Account']"

    # Constructor
    def __init__(self,driver):
        self.driver=driver

    # Action Methods
    def setUsername(self,username):
        self.driver.find_element(By.ID,self.text_username_ID).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.text_password_ID).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_Xpath).click()
        time.sleep(5)

    def MyAccountPage(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_MyAccount_Xpath).is_displayed()
        except:
            return False
