from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading."
           "-images.html")

# Ждём появления текста "Done!" — это сигнал, что все картинки загружены
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

# Теперь ищем все картинки
images = driver.find_elements(By.TAG_NAME, 'img')

# Выводим src третьей картинки (индекс 2)
print(images[2].get_attribute('src'))

driver.quit()
