from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")


try:
    driver.get("http://uitestingplayground.com/ajax")

    button = driver.find_element(By.CSS_SELECTOR, 'button#ajaxButton')
    button.click()
    print("Кнопка нажата")

    wait = WebDriverWait(driver, 15)
    success_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '#content .bg-success'))
    )

    message_text = success_message.text.strip()

    print("Текст из зелёной плашки:")
    print(message_text)

    expected_text = "Data loaded with AJAX get request."
    if message_text == expected_text:
        print("Текст совпадает")
    else:
        print("Текст не совпадает")
        print(f"Ожидалось: {expected_text}")
        print(f"Получено: {message_text}")

finally:
    driver.quit()
    print("Браузер закрыт")
