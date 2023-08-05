import os

import httpx

from integration.abstract_integration_test import TestAbstractIntegration


class TestItCRUDProject(TestAbstractIntegration):

    def test_create_should_return_code_200_when_success(self):
        response: httpx.Response = self.client.post('/projects', json={
            'project_name': 'my projects',
            'nifi_uri': 'localhost:8080'
        })

        assert response.status_code == 200

    def test_create_should_create_project_id_dir_when_not_exist(self):
        response = self.client.post('/projects', json={
            'project_name': 'my projects',
            'nifi_uri': 'localhost:8080'
        }).json()

        assert os.path.exists(f"./tmp/projects/{response['project_id']}")

    def test_create_should_return_the_project_created(self):
        response = self.client.post('/projects', json={
            'project_name': 'my projects',
            'nifi_uri': 'http://localhost:8080'
        }).json()

        assert response['project_id'] is not None
        assert response['project_name'] == 'my projects'
        assert response['nifi_uri'] == 'http://localhost:8080'