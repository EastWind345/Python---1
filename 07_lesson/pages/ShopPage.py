from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window

    def open(self, browser):
        user_name_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "user-name")))
        user_name_field.send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def products(self):
        products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt",
                           "Sauce Labs Onesie"]

        for product_name in products_to_add:
            add_button = self.driver.find_element(By.XPATH, f"//div[contains("
                                                  f"@class, 'inventory_item')"
                                                  f"and.//div[contains(text(),"
                                                  f"'{product_name}')]]//"
                                                  f"button")
        add_button.click()

    def checkout(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()

    def zakaz(self):
        self.driver.find_element(By.ID, "first-name").send_keys("Иван")
        self.driver.find_element(By.ID, "last-name").send_keys("Иванов")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")

        self.driver.find_element(By.ID, "continue").click()

        self.driver.find_element(By.CLASS_NAME, "summary_total_label")
