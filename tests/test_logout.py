from locators.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    def test_logout_and_check_for_login_and_reg_button(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRAION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.LOGON_ENTER_EMAIL_FIELD))
        driver.find_element(*MainPageLocators.LOGON_ENTER_EMAIL_FIELD).send_keys('test_user_logon@henry.ok')
        driver.find_element(*MainPageLocators.LOGON_ENTER_PASS_FIELD).send_keys('1') 
        driver.find_element(*MainPageLocators.LOGON_LOGIN_BUTTON).click() 
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.USER_NAME))
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.LOGIN_AND_REGISTRAION_BUTTON))
        logon_button = driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRAION_BUTTON).text       
        assert logon_button == 'Вход и регистрация', f'logon_button is ------> {logon_button}'
