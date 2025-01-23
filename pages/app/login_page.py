from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "normal_login_username")
        self.password_input = (By.ID, "normal_login_password")
        self.login_button = (By.CSS_SELECTOR, ".ant-btn")
        self.recover_password_link = (By.LINK_TEXT, "¿Olvidaste tu contraseña?")
        self.notification_message = (By.CLASS_NAME, "ant-notification-notice-message")
        
    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def get_notification_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.notification_message)
        ).text

    def is_login_button_enabled(self):
        return self.driver.find_element(*self.login_button).is_enabled()

    def clear_username(self):
        field = self.driver.find_element(*self.username_input)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)

    def clear_password(self):
        field = self.driver.find_element(*self.password_input)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)

    def click_recover_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.recover_password_link)
        ).click()