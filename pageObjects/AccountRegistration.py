import time

from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    #Locators
    txt_firstname_name="firstname"
    txt_last_name="lastname"
    txt_password_name="password"
    txt_email_name="email"
    check_privacypolicy_name = "agree"
    button_continue_xpath = "//button[normalize-space()='Continue']"
    textMsg_confirmation_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    #Constructors
    def __init__(self,driver):     # This is a constructors which will initiate the driver
        self.driver=driver

    #Action methods
    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_last_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)
        time.sleep(3)


    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(password)

        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(5)

    def clickPrivacyPolicy(self):
        self.driver.find_element(By.NAME,self.check_privacypolicy_name).click()
        time.sleep(3)

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.button_continue_xpath).click()
        time.sleep(3)

    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.textMsg_confirmation_xpath).text
        except:
            None
