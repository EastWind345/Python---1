import uuid
import pytest


class TestProjectsNegative:

    def test_create_project_missing_title(self, api_client, test_project_data):
        """Создание проекта без обязательного поля title."""
        response = api_client.create_project(title="", users=test_project_data
                                             ['users'])
        assert response.status_code in [400, 422], \
            f"Ожидался статус 400/422, получен {response.status_code}"

    def test_get_project_not_found(self, api_client):
        """Получение несуществующего проекта."""
        response = api_client.get_project("nonexistent-project-id-123")
        assert response.status_code == 404, \
            f"Ожидался статус 404, получен {response.status_code}"

    def test_update_project_invalid_data(self, api_client, test_project_data):
        """Обновление с некорректными данными."""
        unique_title = f"{test_project_data['title']} - {uuid.uuid4().hex[:8]}"
        create_response = api_client.create_project(title=unique_title)
        assert create_response.status_code == 201
        project_id = create_response.json()['id']

        response = api_client.update_project(project_id, title='')
        assert response.status_code in [400, 422], \
            f"Ожидался статус 400/422, получен {response.status_code}"
