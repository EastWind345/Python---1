from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.ShopPage import ShopPage


def test_shop():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager()
                                               .install()))
    shop_page = ShopPage(browser)
    shop_page.open(browser)
    shop_page.products()
    shop_page.checkout()
    chek = shop_page.zakaz()

    assert chek == "Total: $58.29"
