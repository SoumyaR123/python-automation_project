import configparser
import os

config = configparsher.RawConfigParsher()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")

class  ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo',"baseURL")
        return url

    @staticmethod
    def getuseremail():
        username=config.get("commonInfo","email")
        return username

    @staticmethod
    def getPassword():
        password=config.get("commonInfo","password")
        return password