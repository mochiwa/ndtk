import os.path
import shutil

import httpx
from starlette.testclient import TestClient

from app.project.project import Project
from container import Container
from main import create_app
from unit.app.project.project_mother import ProjectMother


class TestAbstractIntegration:
    container = Container()
    container.config.from_ini(os.path.join(os.path.dirname(__file__), 'config.ini'))
    app = create_app(container)
    client = TestClient(app)
    project_repository = container.project_repository.provided()
    project: Project = None

    def setup(self):
        self.project = self.project_repository.save(ProjectMother.create())

    def teardown(self):
        shutil.rmtree("./tmp")

    def test_should_create_projects_dir_when_application_start(self):
        assert os.path.exists("./tmp/projects") is True

    def _assert_error(self, response: httpx.Response, code: int, title: str, message: str):
        assert response.status_code == code
        assert response.json()['status'] == code
        assert response.json()['title'] == title
        assert response.json()['detail'] == message
