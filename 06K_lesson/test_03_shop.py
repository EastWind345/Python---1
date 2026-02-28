import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shopping_process(browser):

    browser.get("https://www.saucedemo.com/")

    user_name_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "user-name")))
    user_name_field.send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product_name in products_to_add:
        add_button = browser.find_element(By.XPATH,
                                          f"//div[contains(@class,"
                                          f"'inventory_item') and .//div"
                                          f"[contains(text(),"
                                          f"'{product_name}'"
                                          f")]]//button")
        add_button.click()

    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    browser.find_element(By.ID, "checkout").click()

    browser.find_element(By.ID, "first-name").send_keys("Иван")
    browser.find_element(By.ID, "last-name").send_keys("Иванов")
    browser.find_element(By.ID, "postal-code").send_keys("123456")

    browser.find_element(By.ID, "continue").click()

    total_element = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text

    assert total_text == "Total: $58.29"
