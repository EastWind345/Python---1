import pytest
from api import YougileApi


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для создания клиента API."""
    # Данные для наставника: нужно заменить на реальные
    BASE_URL = "https://app.yougile.com"  # URL Yougile
    API_KEY = "your_api_key"  # API‑ключ из профиля Yougile

    client = YougileApi(BASE_URL, API_KEY)
    return client


@pytest.fixture
def test_project_data():
    """Данные для создания тестового проекта."""
    return {
        'name': 'Test 1',
        'description': 'Test description'
    }
