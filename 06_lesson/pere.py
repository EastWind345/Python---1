from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

try:
    driver.get("http://uitestingplayground.com/textinput")

    input_field = driver.find_element(By.CSS_SELECTOR, 'input#newButtonName')
    input_field.send_keys("SkyPro")
    print("Введён текст: SkyPro")

    button = driver.find_element(By.CSS_SELECTOR, 'button#updatingButton')
    button.click()
    print("Кнопка нажата")

    updated_button_text = button.text.strip()

    print("Текст кнопки после клика:")
    print(updated_button_text)

    expected_text = "SkyPro"
    if updated_button_text == expected_text:
        print("Текст кнопки совпадает с ожидаемым")
    else:
        print("Текст кнопки не совпадает")
        print(f"Ожидалось: {expected_text}")
        print(f"Получено: {updated_button_text}")

finally:
    driver.quit()
    print("Браузер закрыт")
