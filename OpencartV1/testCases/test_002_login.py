import pytest

from pageObjects.HomePage import HomePage
from pageobjects.LoginPage import LoginPage
from utilities.readPraperties import ReadConfig
from utilities.customLogger import Loggen
import os

class Test_Login():
    baeURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()    #Logger

    user = ReadConfig.getuseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.lpsetEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshot\\" + "test_login")
            assert False

        self.driver.close()
        self.logger.info("*****End of test_002_login****")


