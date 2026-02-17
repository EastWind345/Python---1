from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

try:
    driver.get('http://the-internet.herokuapp.com/login')

    wait = WebDriverWait(driver, 10)

    username_field = wait.until(
        EC.element_to_be_clickable((By.ID, 'username'))
    )
    username_field.send_keys('tomsmith')
    print('Введён логин: tomsmith')

    password_field = wait.until(
        EC.element_to_be_clickable((By.ID, 'password'))
    )
    password_field.send_keys('SuperSecretPassword!')
    print('Введён пароль: SuperSecretPassword!')

    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    login_button.click()
    print('Нажата кнопка Login')

    success_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '.flash.flash-success'))
    )

    message_text = success_message.text.strip()
    print('Текст с зелёной плашки:')
    print(message_text)

finally:
    driver.quit()
    print('Браузер закрыт')
