import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_email, valid_password

@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome('/home/alex/app/pycharm/chromedriver')
   # Устанавливаем неявное ожидание
   driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(valid_email)
   # Вводим пароль
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pass'))).send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
   # Нажимаем на ссылку "Мои питомцы"
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы'))).click()
   yield driver
   driver.quit()