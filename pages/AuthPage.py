from selenium.webdriver.common.by import By

from pages.Page import BasePage
from helpers.controls import Controls as controls

class AuthorisationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def authorization(self, login):
        controls.get_button_by_name(self.browser, 'Customer Login').click()
        self.browser.find_element(By.XPATH, '//select').click()
        self.browser.find_element(By.XPATH, '//option[text()="' + login + '"]').click()
        controls.get_button_by_name(self.browser, 'Login').click()