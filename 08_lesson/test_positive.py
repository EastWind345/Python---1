import uuid
import pytest


class TestProjectsPositive:

    def test_create_project_success(self, api_client, test_project_data):
        """создание проекта."""
        unique_title = f"{test_project_data['title']} - {uuid.uuid4().hex[:8]}"
        payload = {**test_project_data, 'title': unique_title}

        response = api_client.create_project(**payload)

        assert response.status_code == 201, \
            f"Ожидался статус 201, получен {response.status_code}"
        data = response.json()
        assert 'id' in data

        project_id = data['id']
        get_response = api_client.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json()['title'] == unique_title

    def test_get_project_success(self, api_client, test_project_data):
        """получение проекта по ID."""
        unique_title = f"{test_project_data['title']} - {uuid.uuid4().hex[:8]}"
        create_response = api_client.create_project(title=unique_title)
        assert create_response.status_code == 201
        project_id = create_response.json()['id']

        get_response = api_client.get_project(project_id)
        assert get_response.status_code == 200
        data = get_response.json()
        assert data['id'] == project_id
        assert data['title'] == unique_title

    def test_update_project_success(self, api_client, test_project_data):
        """обновление проекта."""
        unique_title = f"{test_project_data['title']} - {uuid.uuid4().hex[:8]}"
        create_response = api_client.create_project(title=unique_title)
        assert create_response.status_code == 201
        project_id = create_response.json()['id']

        new_title = f"Updated - {unique_title}"
        update_response = api_client.update_project(project_id,
                                                    title=new_title)
        assert update_response.status_code == 200

        get_response = api_client.get_project(project_id)
        assert get_response.json()['title'] == new_title
