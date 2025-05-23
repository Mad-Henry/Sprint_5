from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_AND_REGISTRAION_BUTTON = (By.XPATH, ".//button[text()[contains(., 'Вход и регистрация')]]")
    HAVENT_AN_ACCOUNT_BUTTON= (By.XPATH,  ".//button[text()[contains(., 'Нет аккаунта')]]")
    CREATE_AN_ACCOUNT_BUTTON = (By.XPATH,  ".//button[text()[contains(., 'Создать аккаунт')]]")
    REGISTRATION_EMAIL_FIELD = (By.XPATH, ".//input[@name='email']")
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, ".//input[@name='password']")
    SUBMIT_PASSWORD_FIELD = (By.XPATH, ".//input[@name='submitPassword']")
    ERROR_MESSAGE_TEXT = (By.XPATH, ".//span[text()[contains(., 'Ошибка')]]")
    FRAME_COLOR = (By.CSS_SELECTOR, ".input_inputError__fLUP9")
    LOGON_ENTER_EMAIL_FIELD = (By.XPATH,  ".//*[@Placeholder='Введите Email']")
    LOGON_ENTER_PASS_FIELD = (By.XPATH,  ".//*[@Placeholder='Пароль']")
    LOGON_LOGIN_BUTTON = (By.XPATH,  ".//button[text()[contains(., 'Войти')]]")
    USER_NAME = (By.XPATH, ".//*[@class='profileText name']")
    USER_AVATAR = (By.XPATH, ".//*[@class='svgSmall']")
    LOGON_ADD_AN_AD_BUTTON = (By.XPATH,  ".//button[text()[contains(., 'Войти')]]")
    CREATE_NEW_AD = (By.XPATH,  ".//button[text()[contains(., 'Разместить объявление')]]")
    MODAL_WINDOW = (By.XPATH,  ".//h1[text()[contains(., 'Чтобы разместить объявление, авторизуйтесь')]]")
    EXIT_BUTTON = (By.XPATH,  ".//button[text()[contains(., 'Выйти')]]")  


class CreateAnAD():
    NAME_FIELD = (By.XPATH,  ".//div/input[@placeholder='Название']")
    DESCRIPTION_FIELD = (By.XPATH,  ".//div/textarea[@name='description']")
    PRICE_FIELD = (By.XPATH,  ".//div/input[@placeholder='Стоимость']")
    TYPE_DROPDOWN = (By.XPATH,  "//div[2]/div[1]/button")
    TYPE_DROPDOWN_SET_SADOVODSTVO = (By.XPATH,  "//span[text()[contains(., 'Садоводство')]]/parent::*")
    CITY_DROPDOWN = (By.XPATH,  "//div[3]/div[1]/button")
    CITY_DROPDOWN_SET_NN = (By.XPATH,  "//span[text()[contains(., 'Нижний Новгород')]]/parent::*")
    SET_CONDITION_RADIOBUTTON = (By.XPATH,  "//label[text()[contains(., 'Б/У')]]/parent::*/div")
    SUBMIT_BUTTON = (By.XPATH,  "//button[text()[contains(., 'Опубликовать')]]")
    OPEN_PROFILE = (By.XPATH,  "//button[@class='circleSmall']/*")
    FIND_AD = (By.XPATH,  "//div[@class='card']/div//div/h2")
    