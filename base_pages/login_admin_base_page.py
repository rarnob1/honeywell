from selenium.webdriver.common.by import By

class login_admin_page:

    text_box_user_name = "user-name"
    text_box_password = "password"
    xpath_login_button = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.text_box_user_name).clear()
        self.driver.find_element(By.ID, self.text_box_user_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_box_password).clear()
        self.driver.find_element(By.ID, self.text_box_password).send_keys(password)

    def click_button(self):
        self.driver.find_element(By.ID, self.xpath_login_button).click()
