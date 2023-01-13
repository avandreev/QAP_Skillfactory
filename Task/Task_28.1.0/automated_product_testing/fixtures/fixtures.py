import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def open_rostelecom_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=ef7559df-68f7-4eba-8fb2-75c418c77937&theme&auth_type")
    return driver
