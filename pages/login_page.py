from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class LoginPage(BasePage):

    FEATHR_URL = 'https://login.feathr.co/'
    EMAIL_FIELD = By.XPATH, "//div[1]/div/div/input"
    PASSWORD_FIELD = By.XPATH, "//div[2]/div/div/input"
    SIGN_IN_BUTTON = By.XPATH, "//button[contains(text(),'Sign in')]"
    ALERT_MESSAGE = By.XPATH, "//div[@role='alert']"
    FORGOT_YOUR_PASSWORD_LINK = By.XPATH, "//a[@href='/forgot-password']"
    SEND_ME_INSTRUCTIONS_BUTTON = By.XPATH, "//*[contains(text(), 'Send me instructions')]"
    RETURN_TO_LOGIN_LINK = By.XPATH, "//a[contains(text(), 'Return to log in')]"
    REQUEST_A_DEMO = By.XPATH, "//a[contains(text(), 'Request a demo!')]"

    def navigate_to_feathr(self):
        self.goto_page(self.FEATHR_URL)

    def is_page_title_correct(self):
        return self.get_browser_title() == "Feathr"

    def enter_email(self, email_address):
        self.type_text_in_field(self.EMAIL_FIELD, email_address)

    def enter_password(self, password):
        self.type_text_in_field(self.PASSWORD_FIELD, password)

    def click_sign_in_button(self):
        self.click_element(self.SIGN_IN_BUTTON)

    def get_alert_message_text(self):
        sleep(2)
        return self.get_element_text(self.ALERT_MESSAGE)

    def click_forgot_your_password_link(self):
        self.click_element(self.FORGOT_YOUR_PASSWORD_LINK)

    def click_return_to_login_link(self):
        self.click_element(self.RETURN_TO_LOGIN_LINK)

    def is_send_me_instructions_button_disabled(self):
        sleep(2)
        return self.get_element_attribute_value('aria-disabled', self.SEND_ME_INSTRUCTIONS_BUTTON)

    def is_sign_in_button_present(self):
        sleep(5)
        return self.get_web_element(self.SIGN_IN_BUTTON)

    def click_request_a_demo(self):
        self.click_element(self.REQUEST_A_DEMO)
