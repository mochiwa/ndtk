from mockito import mock, when, verify, ANY

from helper.arg_captor import ArgCaptor
from src.app.shared.file_manager import FileManager

from src.app.project.project_service import ProjectService


class TestProjectService:

    def setup(self):
        self.file_manager: FileManager = mock()
        self.service = ProjectService(self.file_manager)

    def test_create_project_should_create_directory_projects_when_not_exist(self):
        uuid_captor = ArgCaptor()
        when(self.file_manager).create_dir(ANY).thenReturn("filePath")

        self.service.create_project({
            'project_name': 'test',
            'nifi_uri': 'localhost:8080'
        })

        verify(self.file_manager).create_dir(uuid_captor)
        assert uuid_captor.value is not None

    def test_create_project_should_return_project_created(self):
        when(self.file_manager).create_dir(ANY).thenReturn("filePath")

        output = self.service.create_project({
            'project_name': 'test',
            'nifi_uri': 'localhost:8080'
        })

        assert output.project_id is not None
        assert output.project_name == 'test'
        assert output.nifi_uri == 'localhost:8080'

