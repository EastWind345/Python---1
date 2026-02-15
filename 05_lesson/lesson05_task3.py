from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))


try:
    driver.get('http://the-internet.herokuapp.com/inputs')

    wait = ChromeDriverManager(driver, 10)
    input_field = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="number"]'))
    )

    input_field.send_keys('Sky')
    print('Введено "Sky"')

    input_field.clear()
    print('Поле очищено')

    input_field.send_keys('Pro')
    print('Введено "Pro"')

finally:
    driver.quit()
    print('Браузер закрыт')
sleep(10)
