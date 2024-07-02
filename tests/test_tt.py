import allure
from pytest import mark

from pages.ActionsPage import ActionsPage
from pages.TransactionPage import TransactionsPage

from helpers.common import CalcFib

class TestMain:
    @allure.suite("Tests main suite")
    @allure.title("Test actions")
    @allure.description("This test check actions deposit and withdrawl")
    @allure.tag("CheckActions")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Zhanna Morozova")

    @mark.regress
    def test_actions(self):
        actions = ActionsPage(self.driver)

        actions.go_to_deposit()
        fibonacci_number = CalcFib.getFibonacciNumber()
        actions.deposit(fibonacci_number)

        actions.go_to_withdrawl()
        actions.withdrawl(fibonacci_number)

        assert actions.get_balance() == 0
        actions.go_to_transaction()

    @allure.suite("Tests main suite")
    @allure.title("Test transactions")
    @allure.description("This test check transactions after deposit and withdrawl")
    @allure.tag("CheckTransactions")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Zhanna Morozova")
    @mark.regress
    def test_transactions(self):
        transactions = TransactionsPage(self.driver)
        assert transactions.get_transactions_count() == 2

        transactions.write_to_csv('transaction_list.csv')
        transactions.back_to_action_page()

        allure.attach.file('transaction_list.csv', attachment_type=allure.attachment_type.CSV)

