from selenium.webdriver.common.by import By
from pages.Page import BasePage


class Controls(BasePage):
    @staticmethod
    def get_button_by_name(browser, name):
        return browser.find_element(By.XPATH, '//button[text()="' + name + '"]')

    @staticmethod
    def get_button_by_contains_name(browser, name):
        return browser.find_element(By.XPATH, '//button[contains(text(),"' + name + '")]')

    @staticmethod
    def get_submit_button(browser):
        return browser.find_element(By.XPATH, '//button[@type="submit"]')

    @staticmethod
    def select_item_in_dropdown_by_name(browser, name):
        browser.find_element(By.XPATH, '//select').click()
        browser.find_element(By.XPATH, '//option[text()="' + name + '"]').click()