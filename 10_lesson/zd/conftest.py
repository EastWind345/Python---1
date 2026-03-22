import pytest
from selenium import webdriver
import allure


@pytest.fixture
def driver():
    """Фикстура для инициализации браузера."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
