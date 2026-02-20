from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, 'input#newButtonName')
input_field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, 'button#updatingButton')
button.click()

updated_button_text = button.text.strip()

print("SkyPro")

driver.quit()
