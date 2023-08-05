import os.path
import shutil

from starlette.testclient import TestClient

from container import Container
from main import create_app


class TestAbstractIntegration:
    container = Container()
    container.config.from_ini(os.path.join(os.path.dirname(__file__),'config.ini'))
    t = container.config.provided()['APP']
    app = create_app(container)
    client = TestClient(app)
    def teardown(self):
        shutil.rmtree("./tmp")
    def test_should_create_projects_dir_when_application_start(self):
        assert os.path.exists("./tmp/projects") is True
