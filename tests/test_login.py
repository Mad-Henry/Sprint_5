from locators.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_reg_new_user_and_check_redirect_to_mainpage(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRAION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.LOGON_ENTER_EMAIL_FIELD))
        driver.find_element(*MainPageLocators.LOGON_ENTER_EMAIL_FIELD).send_keys('test_user_logon@henry.ok')
        driver.find_element(*MainPageLocators.LOGON_ENTER_PASS_FIELD).send_keys('1') 
        driver.find_element(*MainPageLocators.LOGON_LOGIN_BUTTON).click() 
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.USER_NAME))
        avatar = driver.find_element(*MainPageLocators.USER_AVATAR).get_attribute('xmlns')   
        user_name = driver.find_element(*MainPageLocators.USER_NAME).text
        assert user_name == 'User.' and 'http://www.w3.org/2000/svg' in avatar, f'user_name is ---->>>> {user_name} |||| \n avatar is  ---->>>> {avatar}'
