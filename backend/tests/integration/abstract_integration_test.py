import os.path
import shutil

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
    project: Project = None

    def setup(self):
        self.project = ProjectMother.create()
        self.container.project_repository.provided().save(self.project)

    def teardown(self):
        shutil.rmtree("./tmp")

    def test_should_create_projects_dir_when_application_start(self):
        assert os.path.exists("./tmp/projects") is True
