from selenium.webdriver.common.by import By


class RegistrationFormPage:
    NAME = (By.XPATH, "//input[@name='firstName']")
    SURNAME = (By.XPATH, "//input[@name='lastName']")
    REGION_INPUT = (By.XPATH, "//input[@autocomplete='new-password']")
    REGION_SELECT = (By.XPATH, "//div[@class='rt-select__list-item']")
    EMAIL_MOB_PHONE = (By.XPATH, "//input[@id='address']")
    PASSWORD = (By.ID, "password")
    PASSWORD_CONFIRM = (By.XPATH, "//input[@id='password-confirm']")
    REGISTER_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")
    NAME_ERROR_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
    SURNAME_ERROR_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    INVALID_ACCAUNT_NUMBER_ERROR_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]')
