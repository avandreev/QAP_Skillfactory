from page.registration_form import RegistrationFormPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page.rostelecom_authorization import RostelecomAuthorizationPage
from page.email_confirmation import SubmitEmail
from page.redirect_uri import RedirectURI
from test import functions
from page.policy_privacy import PolicyPrivacy
from page.vk_ru import VK
from page.mail_ru import MailRu
from page.gmail_com import GmailCom
from page.odnoklassniki_ru import Odnoklassniki
from page.yandex_ru import YandexRu
from fixtures.fixtures import open_rostelecom_page


# 1. Позитивный тест формы регистрации с валидными значениями (имя 2 символа)
def test_registration_valid_name_2(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Ал")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()
    # При ручном вводе выпадающий список работает некорректно, заведён баг-репорт - BR-06

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# 2. Позитивный тест формы регистрации с валидными значениями (имя 16 символов)
def test_registration_valid_name_16(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексеееееееееей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# 3. Позитивный тест формы регистрации с валидными значениями (имя 30 символов)
def test_registration_valid_name_30(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексеееееееееееееееееееееееей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# 4. Позитивный тест формы регистрации с валидными значениями (фамилия 2 символа)
def test_registration_valid_surname_2(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Ан')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# 5. Позитивный тест формы регистрации с валидными значениями (фамилия 16 символа)
def test_registration_valid_surname_16(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андрееееееееееев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# 6. Позитивный тест формы регистрации с валидными значениями (фамилия 30 символа)
def test_registration_valid_surname_30(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андрееееееееееееееееееееееееев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# 7. Позитивный тест формы регистрации с валидными значениями (пароль 8 символов)
def test_user_registration_valid_password_8(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# 8. Позитивный тест формы регистрации с валидными значениями (пароль 14 символов)
def test_registration_valid_password_14(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Але")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Анд')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(14)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# 9. Позитивный тест формы регистрации с валидными значениями (пароль 20 символов)
def test_registration_valid_password_20(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(20)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# 10. Негативный тест формы регистрации с невалидным значением (имя 1 символ)
def test_user_registration_name_1_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("А")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    check_error_message = functions.find(driver, RegistrationFormPage.NAME_ERROR_MESSAGE)
    assert check_error_message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# 11. Негативный тест формы регистрации с невалидным значением (имя 31 символ)
def test_user_registration_name_31_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексееееееееееееееееееееееееей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    check_error_message = functions.find(driver, RegistrationFormPage.NAME_ERROR_MESSAGE)
    assert check_error_message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# 12. Негативный тест формы регистрации с невалидным значением (фамилия 1 символ)
def test_user_registration_surname_1_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('А')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    check_error_message = functions.find(driver, RegistrationFormPage.SURNAME_ERROR_MESSAGE)
    assert check_error_message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# 13. Негативный тест формы регистрации с невалидным значением (фамилия 31 символ)
def test_user_registration_surname_31_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреееееееееееееееееееееееееев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    check_error_message = functions.find(driver, RegistrationFormPage.SURNAME_ERROR_MESSAGE)
    assert check_error_message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# 14. Негативный тест формы регистрации с невалидным значением (пароль 7 символов)
def test_registration_password_7_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(7)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)
    check_error_message = functions.find(driver, RegistrationFormPage.INVALID_ACCAUNT_NUMBER_ERROR_MESSAGE)
    assert check_error_message.text == "Длина пароля должна быть не менее 8 символов"


# 15. Негативный тест формы регистрации с невалидным значением (пароль 21 символ)
def test_registration_password_21_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Алтайский край")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    email = functions.get_random_string(5) + '@mail.ru'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(21)
    password.send_keys(password_generation)

    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)
    check_error_message = functions.find(driver, RegistrationFormPage.INVALID_ACCAUNT_NUMBER_ERROR_MESSAGE)
    assert check_error_message.text == "Длина пароля должна быть не более 20 символов"


# 16. Позитивный тест формы авторизации с валидными значениями
def test_authorization_using_mail(open_rostelecom_page):
    driver = open_rostelecom_page

    email_tab = functions.find(driver, RostelecomAuthorizationPage.EMAIL_TAB)
    email_tab.click()

    email_input = functions.find(driver, RostelecomAuthorizationPage.EMAIL)
    email_input.send_keys('inzine@mail.ru')

    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('a12345678AA')

    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    assert "https://b2c.passport.rt.ru/account_b2c/page?state=" in driver.current_url


# 17. Негативный тест формы авторизации с невалидными значениями
def test_authorization_using_personal_account_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    personal_account_tab = functions.find(driver, RostelecomAuthorizationPage.PERSONAL_ACCOUNT_TAB)

    personal_account = functions.find(driver, RostelecomAuthorizationPage.PERSONAL_ACCOUNT)
    personal_account.send_keys("test@mail.ru")

    password = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password.send_keys('Passw0rd')

    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    check_error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert check_error_message.text == "Неверный логин или пароль"


# 18. Негативный тест формы авторизации с невалидным значением (номер телефона)
def test_user_authorization_using_invalid_telephone_number_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    telephone_tab = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER_TAB)
    telephone_tab.click()

    telephone_number = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER)
    telephone_number.send_keys('+77777777777')

    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('a12345678AA')

    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# 19. Негативный тест формы авторизации с невалидным значением (пароль)
def test_user_authorization_with_invalid_password_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    email_tab = functions.find(driver, RostelecomAuthorizationPage.EMAIL_TAB)
    email_tab.click()

    email = functions.find(driver, RostelecomAuthorizationPage.EMAIL)
    email.send_keys('inzine@mail.ru')

    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('b12345678BB')

    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# 20. Позитивный тест открытия страницы пользовательского соглашения
def test_redirect_policy_privacy(open_rostelecom_page):
    driver = open_rostelecom_page

    policy_privacy_link = functions.find(driver, RostelecomAuthorizationPage.POLICY_PRIVACY)
    policy_privacy_link.click()
    current_url = driver.switch_to.window(driver.window_handles[1])
    check_redirect_to_policy_privacy = functions.find(driver, PolicyPrivacy.POLICY_PRIVACY)
    assert driver.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"


# 21. Позитивный тест переадресации для единой авторизации через ВКонтакте (проверка только переадресации)
def test_VK_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    vk_icon = functions.find(driver, RostelecomAuthorizationPage.VK_ICON)
    vk_icon.click()
    check_redirect_vk_page = functions.find(driver, VK.VK)
    assert check_redirect_vk_page.text == 'Для продолжения вам необходимо войти ВКонтакте.'


# 22. Позитивный тест переадресации для единой авторизации через Одноклассники (проверка только переадресации)
def test_odnoklassniki_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    odnoklassniki_icon = functions.find(driver, RostelecomAuthorizationPage.ODNOKLASSNIKI_ICON)
    odnoklassniki_icon.click()
    check_redirect_odnoklassniki_page = functions.find(driver, Odnoklassniki.odnoklassniki)
    assert check_redirect_odnoklassniki_page.text == 'Одноклассники'


# 23. Позитивный тест переадресации для единой авторизации через Мой Мир (проверка только переадресации)
def test_mail_ru_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    mail_ru_icon = functions.find(driver, RostelecomAuthorizationPage.MAIL_RU_ICON)
    mail_ru_icon.click()
    check_redirect_mail_ru_page = functions.find(driver, MailRu.MAIL_RU)
    assert check_redirect_mail_ru_page.text == 'Мой Мир@Mail.Ru'


# 24. Позитивный тест переадресации для единой авторизации через Google (проверка только переадресации)
def test_gmail_com_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    gmail_ru_icon = functions.find(driver, RostelecomAuthorizationPage.GMAIL_COM_ICON)
    gmail_ru_icon.click()
    check_redirect_gmail_com_page = functions.find(driver, GmailCom.GMAIL_COM)
    assert check_redirect_gmail_com_page.text == "Войдите в аккаунт Google"


# 25. Позитивный тест переадресации для единой авторизации через Яндекс ID (проверка только переадресации)
def test_yandex_ru_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    yandex_ru_icon = functions.find(driver, RostelecomAuthorizationPage.YANDEX_RU_ICON)
    yandex_ru_icon.click()
    check_redirect_yandex_ru_page = functions.find(driver, YandexRu.YANDEX_RU)
    assert check_redirect_yandex_ru_page.text == "Войдите с Яндекс ID"
