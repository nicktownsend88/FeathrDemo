from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:

    driver = webdriver.Chrome()

    def goto_page(self, page_url):
        self.driver.get(page_url)
        self.driver.maximize_window()

    def get_browser_title(self):
        return self.driver.title

    def click_element(self, by_locator=None):
        self.get_web_element(by_locator).click()

    def get_web_element(self, by_locator, wait=10):
        try:
            el = WebDriverWait(self.driver, wait).until(ec.presence_of_element_located(by_locator))
        except TimeoutException:
            el = self.driver.find_element(*by_locator)
        return el

    def type_text_in_field(self, text_field, string_to_enter):
        self.get_web_element(text_field).send_keys(string_to_enter)

    def get_element_text(self, by_locator=None):
        return self.get_web_element(by_locator).text

    def get_element_attribute_value(self, element_attribute, by_locator=None):
        return self.get_web_element(by_locator).get_attribute(element_attribute)

    def get_browser_url(self):
        return self.driver.current_url
