import time
from datetime import datetime

import pytest
from selenium import webdriver
import os
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

# @pytest.fixture()
# def setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
#     driver = webdriver.Chrome(service=serv_obj)
#     # driver=webdriver.Chrome(ChromeDriverManager().install())
#     return driver

# -----if we want to run Test Cases on desired browser-----
@pytest.fixture()
def setup(browser):
    if browser == "edge":
        from selenium.webdriver.edge.service import Service
        serv_obj = Service("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)

        # driver=webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching edge browser....")
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("C:\\Drivers\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)

        # driver= webdriver.Firefox(GeckoDriverManager().install())
        print("Launching firefox browser...")
    else:
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        # driver=webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser...")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")                      # This will get the value from CLI/hooks

@pytest.fixture()
def browser(request):                                  # This will return the browser value to setup method
    return request.config.getoption("--browser")


############# Pytest HTML Report #####################

# #------If we want to do customization/modification in Html report-----
#
# # It is hook for adding environment info to Html report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Orange HRM'
#     config._metadata['Module Name'] = 'Login Module'
#     config._metadata['Tester Name'] = 'Hasan'
#
#
#
# # It is hook for delete/remove environment info to Html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Plugins", None)
#     metadata.pop("Packages", None)


# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


