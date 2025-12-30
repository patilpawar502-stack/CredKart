from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class CredKart_Login_Class():

    text_email_xpath = "//input[@id='email']"
    text_password_xpath = "//input[@id='password']"
    click_login_button = "//button[@type='submit']"
    click_on_menu_button = "//a[@role='button']"
    click_logout_button = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver
        self. wait = WebDriverWait(self.driver,5)


    def enter_email(self,email):
        self.driver.find_element(By.XPATH,self.text_email_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

    def click_login_button1(self):
        self.driver.find_element(By.XPATH,self.click_login_button).click()

    def verify_login(self):

        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.click_on_menu_button)))
            self.driver.find_element(By.XPATH,self.click_on_menu_button).click()
            self.driver.find_element(By.XPATH, self.click_logout_button).click()
            return "Login Pass"
        except:
            return "Login Fail"




