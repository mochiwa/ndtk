import os
import uuid

import httpx

from integration.abstract_integration_test import TestAbstractIntegration
from unit.app.project.project_mother import ProjectMother


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

    def test_get_project_by_id_should_return_the_project_found(self):
        response = self.client.get(f'/projects/{self.project.project_id}').json()

        assert response is not None
        assert response['project_id'] == self.project.project_id

    def test_get_should_return_error_project_not_found_when_project_id_not_exist(self):
        project_id = str(uuid.uuid4())
        response = self.client.get(f'/projects/{project_id}')

        assert response.status_code == 404
        assert response.json()['title'] == 'NOT_FOUND'
        assert response.json()['status'] == 404
        assert response.json()['detail'] == f'Project {project_id} not found.'

    def test_get_all_should_return_all_projects(self):
        response = self.client.get(f'/projects')

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]['project_id'] == self.project.project_id

    def test_delete_should_delete_project_from_repository(self):
        project = self.project_repository.save(ProjectMother.create())
        response = self.client.delete(f'/projects/{project.project_id}')

        assert response.status_code == 200
        assert self.project_repository.get(project.project_id) is None

    def test_delete_should_return_200_when_not_project_found_to_delete(self):
        project_id = uuid.uuid4()
        response = self.client.delete(f'/projects/{project_id}')

        assert response.status_code == 200
        assert self.project_repository.get(project_id) is None
