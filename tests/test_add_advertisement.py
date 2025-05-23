from locators.locators import MainPageLocators
from locators.locators import CreateAnAD
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddAnAd:
    def test_add_advertisement_by_unautorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*MainPageLocators.CREATE_NEW_AD).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.MODAL_WINDOW))
        modal_window = driver.find_element(*MainPageLocators.MODAL_WINDOW).text
        assert modal_window == 'Чтобы разместить объявление, авторизуйтесь', f'modal_window is ---->>>> {modal_window}'

    def test_add_advertisement_by_autorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRAION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.LOGON_ENTER_EMAIL_FIELD))
        driver.find_element(*MainPageLocators.LOGON_ENTER_EMAIL_FIELD).send_keys('test_user_logon@henry.ok')
        driver.find_element(*MainPageLocators.LOGON_ENTER_PASS_FIELD).send_keys('1') 
        driver.find_element(*MainPageLocators.LOGON_LOGIN_BUTTON).click()
        create_new_ad_button_refresh = driver.find_element(*MainPageLocators.CREATE_NEW_AD)
        WebDriverWait(driver, 10).until(expected_conditions.staleness_of(create_new_ad_button_refresh))
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MainPageLocators.CREATE_NEW_AD))
        driver.find_element(*MainPageLocators.CREATE_NEW_AD).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(CreateAnAD.NAME_FIELD))
        driver.find_element(*CreateAnAD.NAME_FIELD).send_keys('TEST_NAME_FOR_AN_AD') 
        driver.find_element(*CreateAnAD.DESCRIPTION_FIELD).send_keys('TEST_DESCRIPTION_FOR_AN_AD') 
        driver.find_element(*CreateAnAD.PRICE_FIELD).send_keys(int(99999)) 
        driver.find_element(*CreateAnAD.TYPE_DROPDOWN).click()
        driver.find_element(*CreateAnAD.TYPE_DROPDOWN_SET_SADOVODSTVO).click()      
        driver.find_element(*CreateAnAD.CITY_DROPDOWN).click()
        driver.find_element(*CreateAnAD.CITY_DROPDOWN_SET_NN).click()
        driver.find_element(*CreateAnAD.SET_CONDITION_RADIOBUTTON).click()
        driver.find_element(*CreateAnAD.SUBMIT_BUTTON).click()
        profile_button_refresh = driver.find_element(*CreateAnAD.OPEN_PROFILE)
        WebDriverWait(driver, 10).until(expected_conditions.staleness_of(profile_button_refresh))
        driver.find_element(*CreateAnAD.OPEN_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(CreateAnAD.FIND_AD))
        ad_env = driver.find_element(*CreateAnAD.FIND_AD).text
        assert 'TEST_NAME_FOR_AN_AD' == ad_env, f'ad_env is ---->>>> {ad_env}'
