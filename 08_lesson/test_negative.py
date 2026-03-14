import uuid


class TestProjectsNegative:

    def test_create_project_missing_name(self, api_client):
        """Негативный тест: создание проекта без обязательного поля name."""
        response = api_client.create_project(name="")

        assert response.status_code in [400, 422], \
            f"Ожидался статус 400/422, получен {response.status_code}"

    def test_get_project_not_found(self, api_client):
        """Негативный тест: получение несуществующего проекта."""
        non_existent_id = "nonexistent-project-id-123"
        response = api_client.get_project(non_existent_id)

        assert response.status_code == 404, \
            f"Ожидался статус 404, получен {response.status_code}"

    def test_update_project_invalid_data(self, api_client, test_project_data):
        """Негативный тест: обновление с некорректными данными."""
        unique_name = f"{test_project_data['name']} - {uuid.uuid4().hex[:8]}"
        create_response = api_client.create_project(name=unique_name)
        assert create_response.status_code == 201
        project_id = create_response.json()['id']

        invalid_updates = {'name': ''}
        response = api_client.update_project(project_id, **invalid_updates)

        assert response.status_code in [400, 422], \
            f"Ожидался статус 400/422, получен {response.status_code}"
