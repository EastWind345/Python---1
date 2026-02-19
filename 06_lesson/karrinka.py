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
    driver.get("https://bonigarcia.dev/selenium-webdriver."
               "-java/loading-images.html")

    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))

    images = driver.find_elements(By.TAG_NAME, 'img')

    if len(images) < 3:
        raise IndexError('На странице меньше 3 изображений')

    third_image_src = images[2].get_attribute('src')

    print('Значение атрибута src у 3-й картинки:')
    print(third_image_src)

finally:
    driver.quit()
    print('Браузер закрыт')
