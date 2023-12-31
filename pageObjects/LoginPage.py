import time

from selenium .webdriver.common.by import By

class LoginPage:
    #locatore
    text_email_name="email"
    text_password_name="password"
    button_login_xpath="//button[normalize-space()='Login']"
    Msg_confirmation_xpath="//h2[normalize-space()='My Account']"

    # constructors
    def __init__(self,driver):
        self.driver=driver

    # Action method
    def setUsername(self,email):
        self.driver.find_element(By.NAME,self.text_email_name).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.text_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
        time.sleep(5)

    def MyAccountPage(self):
        try:
            return self.driver.find_element(By.XPATH,self.Msg_confirmation_xpath).is_displayed()

        except:
            return False

