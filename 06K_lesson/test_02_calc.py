from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)


def test_slow_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow."
               "-calculator.html")

    element = driver.find_element(By.CSS_SELECTOR, "#delay")  # нашли элемент
    element.send_keys("45")  # отправляем текст

    driver.find_element(By.CSS_SELECTOR, "7", "+", "8", "=").click()

    assert element >= 15


driver.quit()
