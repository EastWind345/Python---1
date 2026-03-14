import uuid


class TestProjectsPositive:

    def test_create_project_success(self, api_client, test_project_data):
        """Позитивный тест: создание проекта."""
        unique_name = f"{test_project_data['name']} - {uuid.uuid4().hex[:8]}"
        payload = {**test_project_data, 'name': unique_name}

        response = api_client.create_project(**payload)

        assert response.status_code == 201, \
            f"Ожидался статус 201, получен {response.status_code}"

        data = response.json()
        assert 'id' in data, "В ответе отсутствует ID проекта"
        assert data['name'] == unique_name, "Имя проекта не совпадает"

    def test_get_project_success(self, api_client, test_project_data):
        """Позитивный тест: получение проекта по ID."""
        unique_name = f"{test_project_data['name']} - {uuid.uuid4().hex[:8]}"
        create_response = api_client.create_project(name=unique_name)
        assert create_response.status_code == 201
        project_id = create_response.json()['id']

        get_response = api_client.get_project(project_id)
        assert get_response.status_code == 200, \
            f"Ожидался статус 200, получен {get_response.status_code}"

        data = get_response.json()
        assert data['id'] == project_id, "ID проекта не совпадает"
        assert data['name'] == unique_name, "Имя проекта не совпадает"

    def test_update_project_success(self, api_client, test_project_data):
        """Позитивный тест: обновление проекта."""
        unique_name = f"{test_project_data['name']} - {uuid.uuid4().hex[:8]}"
        create_response = api_client.create_project(name=unique_name)
        assert create_response.status_code == 201
        project_id = create_response.json()['id']

        new_name = f"Updated - {unique_name}"
        update_response = api_client.update_project(
            project_id,
            name=new_name,
            description="Updated description"
        )
        assert update_response.status_code == 200, \
            f"Ожидался статус 200, получен {update_response.status_code}"

        get_response = api_client.get_project(project_id)
        data = get_response.json()
        assert data['name'] == new_name, "Имя проекта не обновилось"
