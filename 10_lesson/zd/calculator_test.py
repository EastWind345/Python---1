from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalculPage import CalculPage


def test_calculator():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager()
                                               .install()))
    calcul_page = CalculPage(browser)
    calcul_page.delay()
    calcul_page.knopka()
    itog = calcul_page.result()

    assert itog == "15"
