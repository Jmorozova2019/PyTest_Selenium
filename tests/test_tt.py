from selenium import webdriver
import allure
from pytest import mark

from pages.AuthPage import AuthorisationPage
from pages.ActionsPage import ActionsPage
from pages.TransactionPage import TransactionsPage

from helpers.common import CalcFib

class TestMain():
    @allure.suite("Tests main suite")
    @allure.title("Test transactions")
    @allure.description("This test check transactions after deposit and withdrawl")
    @allure.tag("CheckTransactions")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Zhanna Morozova")

    @mark.regress
    def test_transactions(self):
        base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        login = 'Harry Potter'
        remote_url = 'http://127.0.0.1:4444/wd/hub'

        fibonacci_number = CalcFib.getFibonacciNumber()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        with (webdriver.Remote(command_executor = remote_url, options=chrome_options,) as browser):
            browser.implicitly_wait(5)
            browser.get(base_url)

            auth_page = AuthorisationPage(browser)
            auth_page.authorization(login)

            actions = ActionsPage(browser)
            actions.go_to_deposit()
            actions.deposit(fibonacci_number)

            actions.go_to_withdrawl()
            actions.withdrawl(fibonacci_number)

            assert actions.get_balance() == 0

            actions.go_to_transaction()

            transactions = TransactionsPage(browser)
            assert transactions.get_transactions_count() == 2

            transactions.write_to_csv('transaction_list.csv')
            transactions.back_to_action_page()

            allure.attach.file('transaction_list.csv', attachment_type=allure.attachment_type.CSV)

