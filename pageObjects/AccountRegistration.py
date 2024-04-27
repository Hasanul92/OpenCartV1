# import time
#
# from selenium.webdriver.common.by import By
#
#
# class AccountRegistrationPage():
#     #Locators
#     txt_firstname_name="firstname"
#     txt_lastname_name="lastname"
#     txt_password_name="password"
#     txt_email_name="email"
#     check_privacypolicy_name = "agree"
#     button_continue_xpath = "//button[normalize-space()='Continue']"
#     textMsg_confirmation_xpath="//h1[normalize-space()='Your Account Has Been Created!']"
#
#     #Constructors
#     def __init__(self,driver):     # This is a constructors which will initiate the driver
#         self.driver=driver
#
#     #Action methods
#     def setFirstName(self,fname):
#         self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)
#
#     def setLastName(self,lname):
#         self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)
#
#     def setEmail(self,email):
#         self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)
#         time.sleep(3)
#
#
#     def setPassword(self,password):
#         self.driver.find_element(By.NAME,self.txt_password_name).send_keys(password)
#
#         self.driver.execute_script("window.scrollBy(0, 300);")
#         time.sleep(5)
#
#     def clickPrivacyPolicy(self):
#         self.driver.find_element(By.NAME,self.check_privacypolicy_name).click()
#         time.sleep(3)
#
#     def clickContinue(self):
#         self.driver.find_element(By.XPATH,self.button_continue_xpath).click()
#         time.sleep(5)
#
#     def getConfirmationMsg(self):
#         try:
#             return self.driver.find_element(By.XPATH,self.textMsg_confirmation_xpath).text
#         except:
#             None



import time

from selenium.webdriver.common.by import By
class AccountRegistrationPage():

    #Locators
    txt_FirstName_ID="input-firstname"
    txt_LastName_ID="input-lastname"
    txt_Email_ID="input-email"
    txt_Password_ID="input-password"
    check_PrivacyPolacy_name="agree"
    button_Continue_Xpath="//button[@type='submit']"
    txt_ConfMsg_Xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    #Constructor
    def __init__(self,driver):               # This is the constructor which will initiate the driver
        self.driver=driver

    #Action Method
    def setFname(self,Fname):
        self.driver.find_element(By.ID,self.txt_FirstName_ID).send_keys(Fname)
        time.sleep(3)

    def setLname(self,Lname):
        self.driver.find_element(By.ID,self.txt_LastName_ID).send_keys(Lname)
        time.sleep(3)

    def setEmail(self,Email):
        self.driver.find_element(By.ID,self.txt_Email_ID).send_keys(Email)
        time.sleep(3)

    def setPassword(self,Password):
        self.driver.find_element(By.ID,self.txt_Password_ID).send_keys(Password)
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(5)

    def ClickPrivacy(self):
        self.driver.find_element(By.NAME,self.check_PrivacyPolacy_name).click()
        time.sleep(3)

    def ClickContinue(self):
        self.driver.find_element(By.XPATH,self.button_Continue_Xpath).click()
        time.sleep(3)

    def ConfMsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_ConfMsg_Xpath).text

        except:
            None
