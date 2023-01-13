from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import secrets
import string


def find(driver, element, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located(element)
        )
    except:
        print('Element not found on the page!')
    return element


def get_random_string(length):
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 1):
            break
    return password


