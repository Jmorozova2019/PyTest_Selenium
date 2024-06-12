from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import allure

from pages.Page import BasePage

from helpers import controls
from helpers.controls import Controls as controls

inputLocator = '//input[@placeholder]'

class ActionsPage(BasePage):

    """ Метод для перехода на форму пополнения баланса """
    def go_to_deposit(self):
        controls.get_button_by_contains_name(self.browser, 'Deposit').click()

    """ Метод для перехода на форму снятия с баланса """
    def go_to_withdrawl(self):
        controls.get_button_by_contains_name(self.browser, 'Withdrawl').click()

    """ Метод для перехода на форму транзакций """
    def go_to_transaction(self):
        controls.get_button_by_contains_name(self.browser, 'Transactions').click()


    """ Метод пополнения баланса """
    def deposit(self, amount):
        with allure.step("Top up the account"):
            self.browser.find_element(By.XPATH, inputLocator).click()    # Дополнительные действия для обхода shadow root
            elem = self.browser.switch_to.active_element

        elem.send_keys(amount)
        controls.get_submit_button(self.browser).click()

    """ Метод списания с баланса """
    def withdrawl(self, amount):
        with allure.step("Withdraw money from the account"):
            location = self.browser.find_element(By.XPATH, inputLocator).location
            actions = ActionChains(self.browser)                         # Дополнительные действия для обхода shadow root
            actions.move_by_offset(location['x'], location['y']).click().perform()
            elem = self.browser.switch_to.active_element

            elem.send_keys(amount)
            controls.get_submit_button(self.browser).click()

    """ Метод для получения значения суммы на балансе """
    def get_balance(self):
        balance = self.browser.find_element(By.XPATH,'//text()[contains(., "Balance ")]/following::strong[1]')
        return int(balance.text)
