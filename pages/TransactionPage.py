import csv
import time

from selenium.webdriver.common.by import By
import allure

from pages.Page import BasePage
from helpers.controls import Controls as controls


rowsLocator = 'tbody>tr'

class TransactionsPage(BasePage):

    """ Метод возвращает количество записей в таблице транзакций.
    Процесс записи занимает некоторое время, поэтому было добавлено ожидание не более 60 с.
    Подсчет количества транзакций, если их много, и проверка времени найденных транзакций не реализована """
    def get_transactions_count(self):
        with allure.step("Check transaction count"):
            max_time_wait = 60
            step_wait = 0.5
            time_wait = 0
            self.browser.find_element(By.CSS_SELECTOR,'#start').click()
            self.browser.find_element(By.CSS_SELECTOR,'#start').clear()

            while ((not self.browser.find_elements(By.CSS_SELECTOR, rowsLocator)) and (time_wait < max_time_wait)):
                time.sleep(step_wait)
                time_wait += step_wait
                self.browser.refresh()
            rows_transaction = self.browser.find_elements(By.CSS_SELECTOR, rowsLocator)

            return len(rows_transaction)

    """ Метод, в котором реализована запись транзакций в файл .csv """
    def write_to_csv(self, file_name):
        with allure.step("Write transaction to .csv"):
            rows = self.browser.find_elements(By.CSS_SELECTOR, rowsLocator)
            with open(file_name, 'w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['Дата - времяТранзакции', 'Сумма', 'ТипТранзакции'])

            with open('transaction_list.csv', 'a', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                for row in rows:
                    columns = row.find_elements(By.CSS_SELECTOR, 'td')
                    transaction_dt = columns[0].text
                    transaction_amount = columns[1].text
                    transaction_type = columns[2].text

                    writer.writerow([transaction_dt, transaction_amount, transaction_type])

    """ Метод для возврата со страницы транзакций на форму действий со счетом """
    def back_to_action_page(self):
        controls.get_button_by_name(self.browser, 'Back').click()