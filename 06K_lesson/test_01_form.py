from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()
driver.maximize_window()


def test_form_validation(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver."
                "-java/data-types.html")
    wait = WebDriverWait(browser, 10)

    first_name_field = wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )
    first_name_field.send_keys("Иван")

    last_name_field = browser.find_element(By.NAME, "last-name")
    last_name_field.send_keys("Петров")

    address_field = browser.find_element(By.NAME, "address")
    address_field.send_keys("Ленина, 55-3")

    email_field = browser.find_element(By.NAME, "e-mail")
    email_field.send_keys("test@skypro.com")

    phone_field = browser.find_element(By.NAME, "phone")
    phone_field.send_keys("+7985899998787")

    zip_code_field = browser.find_element(By.NAME, "zip-code")

    city_field = browser.find_element(By.NAME, "city")
    city_field.send_keys("Москва")

    country_field = browser.find_element(By.NAME, "country")
    country_field.send_keys("Россия")

    job_position_field = browser.find_element(By.NAME, "job-position")
    job_position_field.send_keys("QA")

    company_field = browser.find_element(By.NAME, "company")
    company_field.send_keys("SkyPro")

    submit_button = browser.find_element(By.CSS_SELECTOR,
                                         "button[type='submit']")
    submit_button.click()

    wait.until(
        lambda driver: any(
            "is-invalid" in elem.get_attribute("class") or
            "is-valid" in elem.get_attribute("class")
            for elem in driver.find_elements(By.CSS_SELECTOR, "[name]")
        )
    )

    zip_code_field = browser.find_element(By.NAME, "zip-code")
    zip_code_classes = zip_code_field.get_attribute("class")
    assert "is-invalid" in zip_code_classes, "Поле Zip code не подсвечено"
    "красным"

    valid_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_name in valid_fields:
        field = browser.find_element(By.NAME, field_name)
        field_classes = field.get_attribute("class")
        assert "is-valid" in field_classes, f"Поле {field_name} не подсвечено"
        "зелёным"
