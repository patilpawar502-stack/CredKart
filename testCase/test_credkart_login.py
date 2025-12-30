import allure
import pytest

from pageObjects.credKart_login_page import CredKart_Login_Class
from utillities.ReadConfig import ReadConfigClass
from utillities.logger import Log_Genrater_Class


@pytest.mark.usefixtures("driver_setup")
class Test_Credcart_Login_Page:
    driver = None
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_application_url()
    log = Log_Genrater_Class.loggen_method()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("CredKart")
    @allure.story("CredKart Login")
    @allure.description("This test case is to validate login functionality")
    @allure.testcase("https://apps.credence.in/login.html")
    @allure.title("test_credKart_login")
    def test_credkart_login(self):
        self.log.info("opening url")
        self.driver.get(self.login_url)
        self.log.info("Landed on url")
        self.lp = CredKart_Login_Class(self.driver)
        self.log.info("entering email")

        self.lp.enter_email(self.email)
        self.log.info("entering password")
        self.lp.enter_password(self.password)
        self.log.info("Checking login")
        self.lp.click_login_button1()

        if self.lp.verify_login() == "Pass":
            print("User login Successful")
            self.log.info("Taking Screenshort")
            self.driver.save_screenshot(r"D:\pro\CredKartFreamwork\ScreenShots\\loginSuccess.png")
            allure.attach.file(r"D:\pro\CredKartFreamwork\ScreenShots\\loginSuccess.png",name="User login Successful",attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.log.info("Tanking Screenshot")
            self.driver.save_screenshot(r"D:\pro\CredKartFreamwork\ScreenShots\\loginFail.png")
            allure.attach.file(r"D:\pro\CredKartFreamwork\ScreenShots\loginFail.png", name="User login Failed", attachment_type=allure.attachment_type.PNG)
            print("Login Failed")




