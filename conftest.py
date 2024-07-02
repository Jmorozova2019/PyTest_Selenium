# никогда не импортируется. Считется плагином
import pytest
from selenium import webdriver

from pages.AuthPage import AuthorisationPage

@pytest.fixture(autouse=True, scope="class")
def get_driver(request):
    # Setup
    base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    login = 'Harry Potter'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    driver.implicitly_wait(5)
    driver.get(base_url)

    auth_page = AuthorisationPage(driver)
    auth_page.authorization(login)

    yield

    #Teardown
    driver.quit()