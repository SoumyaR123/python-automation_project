from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
import os
from utilities.customLogger import LogGen

class test_0001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_account_reg(self,setup):
        self.logger.info("**** test_001_AccountRegistration started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Lunching application")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("clicking on Myaccount--> regidster")
        self.hp.ClickMyAccount()
        self.hp.ClickRegister()

        self.regpage=AccountRegistationPage(self.driver)

        self.regpage.setFirstname("soumya")
        self.regpage.SetLastName("ranjan")
        self.regpage.SetEmail(self.email)
        self.regpage.SetPassword(self.password)
        self.regpage.setPrivacyPolicy()
        self.regpage.ClickContinue()
        self.confmsg=self.regpage.getconfrimationmsg()
        self.driver.close()
        if self.confmsg=="Your Account Hasbeen Created":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.driver.close()
            assert False
