from selenium.webdriver.common.by import By


class RostelecomAuthorizationPage:
    REGISTRATION_LINK = (By.XPATH, '//a[@id="kc-register"]')
    EMAIL_TAB = (By.XPATH, '// div[ @ id = "t-btn-tab-mail"]')
    EMAIL = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    ENTER_BUTTON = (By.XPATH, "// button[ @ id = 'kc-login']")
    PERSONAL_ACCOUNT_TAB = (By.XPATH, "// div[ @ id = 't-btn-tab-ls']")
    PERSONAL_ACCOUNT = (By.XPATH, "//input[@id='username']")
    POLICY_PRIVACY = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    VK_ICON = (By.XPATH, '//*[@alt="ВКонтакте"]')
    ODNOKLASSNIKI_ICON = (By.XPATH, '//*[@id="oidc_ok"]')
    MAIL_RU_ICON = (By.CSS_SELECTOR, "a#oidc_mail > svg")
    GMAIL_COM_ICON = (By.XPATH, '//*[@id="oidc_google"]')
    YANDEX_RU_ICON = (By.XPATH, '//*[@id="oidc_ya"]')
    TELEPHONE_NUMBER_TAB = (By.XPATH, '//*[@id="t-btn-tab-phone"]')
    TELEPHONE_NUMBER = (By.XPATH, '//input[@id="username"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="form-error-message"]')
    LOGIN_TAB = (By.XPATH, '//*[@id="t-btn-tab-login"]')

