import time

from selenium.webdriver.common.by import By


class JustAmomentPage():
    #Locators
    checkbox_vrfyhumn_xpath="//input[@type='checkbox']"

    #Constructors
    def __init__(self,driver):     # This is a constructors which will initiate the driver
        self.driver=driver

    #Action methods
    def checkHumn(self):
        self.driver.find_element(By.XPATH,self.checkbox_vrfyhumn_xpath).click()

