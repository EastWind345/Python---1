import pytest
from api import YougileApi

BASE_URL = "https://app.yougile.com"
API_KEY = ""  # API‑ключ из профиля Yougile


@pytest.fixture(scope="session")
def api_client():
    return YougileApi(BASE_URL, API_KEY)


@pytest.fixture(scope="session")
def current_user_id(api_client):
    """Получить ID текущего пользователя для создания проектов."""
    response = api_client.get_users()
    assert response.status_code == 200, "Не удалось получить список"
    users = response.json().get('content', [])
    assert users, "Список пользователей пуст"
    return users[0]['id']


@pytest.fixture
def test_project_data(current_user_id):
    return {
        'name': 'Test 1',
        'user': {current_user_id: 'admin'}
    }
