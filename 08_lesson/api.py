import requests


class YougileApi:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

    def create_project(self, name, **kwargs):
        """Создать проект (POST /api-v2/projects)"""
        url = f"{self.base_url}/api-v2/projects"
        payload = {'name': name, **kwargs}
        response = requests.post(
            url,
            json=payload,
            headers=self.headers
        )
        return response

    def get_project(self, project_id):
        """Получить проект по ID (GET /api-v2/projects/{id})"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id, **updates):
        """Обновить проект (PUT /api-v2/projects/{id})"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.put(
            url,
            json=updates,
            headers=self.headers
        )
        return response
