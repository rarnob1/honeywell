import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.login_admin_base_page import login_admin_page
import os
from utility.custom_logger import logclass

from utility.read_properties import Read_config

class TestAdminLogin:

    admin_page_url = Read_config.admin_page_url()
    username = Read_config.valid_user_name()
    password = Read_config.valid_password()
    invalid_username = Read_config.invalid_user_name()
    logger=logclass.log_gen()



    # If you don't need to keep the browser open, re-enable teardown:
    # def teardown_method(self, method):
    #     self.driver.quit()

    def test_title_verification(self,setup):
        self.driver=setup
        self.logger.info("***************** 1st *******************")
        self.driver.get(self.admin_page_url)
        exp_title = "Swag Labs"
        act_title = self.driver.title
        assert act_title == exp_title

    def test_valid_login(self,setup):
        self.logger.info("***************** 2nd *******************")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.loginObject = login_admin_page(self.driver)  # Pass driver to login page
        self.loginObject.enter_username(self.username)
        self.loginObject.enter_password(self.password)
        self.loginObject.click_button()

        login_check = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product_label']"))
        ).text
        assert login_check == "Products"

    def test_invalid_login(self, setup):
        self.logger.info("***************** 3rd *******************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.loginObject = login_admin_page(self.driver)
        self.loginObject.enter_username(self.invalid_username)
        self.loginObject.enter_password(self.password)
        self.loginObject.click_button()

        exp_error = "Epic sadface: Username and password do not match any user in this service"

        try:
            login_check = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/h3"))
            ).text

            assert login_check == exp_error

        except AssertionError:
            # Specify absolute path for 'screenshot' folder
            screenshot_dir = r"C:\Users\Rafi Ornob\PycharmProjects\honeywell\screenshot"

            # Create 'screenshot' folder if it doesn't exist
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)  # Create the directory

            # Save the screenshot in the 'screenshot' folder
            screenshot_path = os.path.join(screenshot_dir, "test_invalid_login_failed.png")
            self.driver.save_screenshot(screenshot_path)

            raise  # Re-raise to mark the test as failed

        finally:
            self.driver.close()

