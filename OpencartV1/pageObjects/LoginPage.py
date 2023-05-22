from selenium.webdriver.common.by import By

class LoginPage():
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//button[@type='submit']"
    msg_myaccount_xpath = "//h2[txt()='My Account']"

    #Action methods
    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).sendkeys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).click()

    def isMyAccountPage(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False


