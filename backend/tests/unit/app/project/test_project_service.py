import pytest
from mockito import mock, when, verify, ANY

from app.project.exception.project_not_found_exception import ProjectNotFoundException
from app.project.project_repository import ProjectRepository
from app.shared.exception.not_found_exception import NotFoundException
from helper.arg_captor import ArgCaptor
from src.app.project.project_service import ProjectService
from unit.app.project.project_mother import ProjectMother


class TestProjectService:

    def setup(self):
        self.repository: ProjectRepository = mock()
        self.service = ProjectService(self.repository)

    def test_create_project_should_create_directory_projects_when_not_exist(self):
        uuid_captor = ArgCaptor()
        when(self.repository).save(ANY).thenAnswer(lambda x: x)

        self.service.create_project({
            'project_name': 'test',
            'nifi_uri': 'localhost:8080'
        })

        verify(self.repository).save(uuid_captor)
        assert uuid_captor.value is not None

    def test_create_project_should_return_project_created(self):
        when(self.repository).save(ANY).thenAnswer(lambda x: x)

        output = self.service.create_project({
            'project_name': 'test',
            'nifi_uri': 'localhost:8080'
        })

        assert output.project_id is not None
        assert output.project_name == 'test'
        assert output.nifi_uri == 'localhost:8080'

    def test_get_project_should_return_project_found(self):
        project = ProjectMother.create()
        when(self.repository).get(project.project_id).thenReturn(project)

        output = self.service.get_project(project.project_id)

        assert output is not None
        assert output.project_id == project.project_id

    def test_get_project_should_raise_project_not_found_exception_when_repository_not_contains_project(self):
        when(self.repository).get('').thenReturn(None)

        with pytest.raises(ProjectNotFoundException) as exception:
            self.service.get_project('')

        assert isinstance(exception.value, ProjectNotFoundException)
        assert isinstance(exception.value, NotFoundException)
