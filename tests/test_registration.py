from locators.locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import NewEmail


new_email = NewEmail.new_email()

class TestRegistration:
    def test_reg_new_user_and_check_redirect_to_mainpage(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRAION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((MainPageLocators.HAVENT_AN_ACCOUNT_BUTTON)))
        driver.find_element(*MainPageLocators.HAVENT_AN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((MainPageLocators.REGISTRATION_EMAIL_FIELD)))
        driver.find_element(*MainPageLocators.REGISTRATION_EMAIL_FIELD).send_keys(new_email)
        driver.find_element(*MainPageLocators.REGISTRATION_PASSWORD_FIELD).send_keys('Qwerty!@') 
        driver.find_element(*MainPageLocators.SUBMIT_PASSWORD_FIELD).send_keys('Qwerty!@')
        driver.find_element(*MainPageLocators.CREATE_AN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(((MainPageLocators.CREATE_NEW_AD))))
        create_an_ad_txt = driver.find_element(*MainPageLocators.CREATE_NEW_AD).text
        assert create_an_ad_txt == 'Разместить объявление', f'create_an_ad is ---->>>> {create_an_ad_txt}'

    def test_registration_w_wrong_email_isnt_allowed(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRAION_BUTTON).click()       
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((MainPageLocators.HAVENT_AN_ACCOUNT_BUTTON)))
        driver.find_element(*MainPageLocators.HAVENT_AN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((MainPageLocators.REGISTRATION_EMAIL_FIELD)))
        driver.find_element(*MainPageLocators.REGISTRATION_EMAIL_FIELD).send_keys("test@wrongemail")
        driver.find_element(*MainPageLocators.CREATE_AN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((MainPageLocators.ERROR_MESSAGE_TEXT)))
        error_message = driver.find_element(*MainPageLocators.ERROR_MESSAGE_TEXT).text
        error_message_frame_color = driver.find_element(*MainPageLocators.FRAME_COLOR).value_of_css_property("border-color")
        assert "Ошибка" == error_message and 'rgb(255, 105, 114)' in error_message_frame_color, f'error_message is ---->>>> {error_message} ||||||| error_message_frame_color ---->>>> {error_message_frame_color} '

    def test_rereg_new_user_and_check_for_errors(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRAION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((MainPageLocators.HAVENT_AN_ACCOUNT_BUTTON)))
        driver.find_element(*MainPageLocators.HAVENT_AN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((MainPageLocators.REGISTRATION_EMAIL_FIELD)))
        driver.find_element(*MainPageLocators.REGISTRATION_EMAIL_FIELD).send_keys(new_email)
        driver.find_element(*MainPageLocators.REGISTRATION_PASSWORD_FIELD).send_keys('Qwerty!@') 
        driver.find_element(*MainPageLocators.SUBMIT_PASSWORD_FIELD).send_keys('Qwerty!@')
        driver.find_element(*MainPageLocators.CREATE_AN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((MainPageLocators.ERROR_MESSAGE_TEXT)))
        error_message = driver.find_element(*MainPageLocators.ERROR_MESSAGE_TEXT).text
        error_message_frame_color = driver.find_element(*MainPageLocators.FRAME_COLOR).value_of_css_property("border-color")    
        assert "Ошибка" == error_message and 'rgb(255, 105, 114)' in error_message_frame_color, f'error_message is ---->>>> {error_message} ||||||| \n error_message_frame_color ---->>>> {error_message_frame_color} ||||||| \n new_email ---->>>> {new_email} '
