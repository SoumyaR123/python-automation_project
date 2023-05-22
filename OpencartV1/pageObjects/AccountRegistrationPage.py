from selenium.webdriver.common.by import By

class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_password_name = "password"
    chk_policy_name = "agree"
    btn_cont_xpath = "//button[normalize-space()='Continue']"
    txt_mag_conf_xpath="//h1[normalize-space()='your account has been Cedited!']"

    def __init__(self):
        self.driver = driver

    def SetfiFstname(self,fname):
        self.driver.find_element(By.NAME,self.txt_first_name).send_keys(fname)

    def SetlastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_last_name).send_keys(lname)

    def SetEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def SetPassword(self,pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def SetPrivacyPolicy(self):
        self.driver.find_element(By.NAME,self.chk_policy_name).click()

    def ClickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_cont_xpath).click()

    def getconfrimationmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_mag_conf_xpath).text()
        except:
            None




