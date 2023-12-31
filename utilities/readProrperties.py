import configparser
import os

config=configparser.RawConfigParser()
# config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")
config.read(os.getcwd()+"\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo','baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username=config.get('commonInfo','email')
        return username

    @staticmethod
    def getUserPassword():
        password=config.get('commonInfo','password')
        return password
