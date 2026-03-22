from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculPage:
    """Страница калькулятора для тестирования."""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver — экземпляр драйвера браузера.
        """
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def set_delay(self, delay_value: str = "50") -> None:
        """
        Устанавливает задержку в калькуляторе.

        Args:
            delay_value: str — значение задержки в секундах (по умолчанию "50"
            ).
        """
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(delay_value)

    def perform_calculation(self) -> None:
        """
        Выполняет расчёт: 7 + 8 =.
        """
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self) -> str:
        """
        Получает результат расчёта с ожиданием.

        Returns:
            str — текст результата из экрана калькулятора.
        """
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"
                                              ), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
