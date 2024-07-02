
pip install allure-pytest
# ------------ Запуск не на гриде------------
# python -m pytest --alluredir allure-results   Запуск теста с аллюром
# allure serve allure-results                   Отображение  отчета

# -------------- Запуск на гриде ----
# в отдельных процессах cmd
# netstat -a занятые порты - проверить, не занят ли порт перед запуском ноды


# java -jar selenium-server-standalone-3.9.0.jar запустить сервер
# java -jar selenium-server-standalone-3.9.0.jar -role webdriver -hub http://172.18.103.81:4444/grid/register -port 5255

# pytest --alluredir allure-results     запуск с аллюром
# allure serve allure-results           генерация и отображение  отчета