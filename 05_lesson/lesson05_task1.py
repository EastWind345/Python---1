from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get('http://uitestingplayground.com/classattr')

    button = driver.find_element(By.XPATH, "//button[contains(text(),"
                                 "'Button')]")

    button.click()

    print("Кнопка нажата успешно.")

finally:
    driver.quit()
sleep(10)
