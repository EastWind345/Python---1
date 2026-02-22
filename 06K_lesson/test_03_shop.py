from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()


def test_shopping_process(browser):
    wait = WebDriverWait(browser, 10)

    browser.get("https://www.saucedemo.com/")

    wait.until(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product_name in products_to_add:
        add_button = browser.find_element(
            By.XPATH, f"//div[text()='{product_name}']/following::button"
        )
        add_button.click()

    wait.until(By.CLASS_NAME, "shopping_cart_badge").click()
    wait.until(By.ID, "checkout").click()

    browser.find_element(By.ID, "first-name").send_keys("Иван")
    browser.find_element(By.ID, "last-name").send_keys("Иванов")
    browser.find_element(By.ID, "postal-code").send_keys("123456")

    browser.find_element(By.ID, "continue").click()

    total_element = wait.until(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text

    total_amount = float(total_text.split("$")[1])

    assert round(total_amount, 2) == 58.29, \
        f"Ошибка: ожидалось $58.29, получено ${total_amount}"
