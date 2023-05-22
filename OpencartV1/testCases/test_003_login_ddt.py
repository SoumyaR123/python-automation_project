import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.Loginpage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    path = os.path.abspath(os.curdir)+"\\testdata\\Opencart_LoginData.xlsa"

    # @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("**** Starting test_003_login_Datadriven****")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAcccountPage(self.driver)

        for r in range(2,elf.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email=XLUtiles.readData(self.path,"Sheet1",r,1)
            self.pasword = XLUtils.readDatareadData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readDatareadData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self,email)
            self.lp.SetPassword(self.password)
            self.lp.clockLogin()
            time.sleep(3 )
            self.targetpage=self.lp.isMyAccountPageExists()

            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_sttus.append('pass')
                    self.ma.clickLogout()
                else:
                    lst_ststus.append('Fail')
            elif self.exp=='Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.ma.clcikLogout()
                else:
                    lst_ststus.append('Pass')
            self.driver.close()
            #final validation
            if "Fail" not in lst_status:
                assert True
            else:
                assert False
            self.logger.info("**** end of test_003)login_Datadriven")








