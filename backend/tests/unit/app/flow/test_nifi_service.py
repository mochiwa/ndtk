import pytest
from mockito import mock, when, ANY

from app.flow.flow_not_found_exception import FlowNotFoundException
from app.flow.flow_provider import FlowProvider
from app.flow.nifi_service import NifiService
from app.project.exception.project_not_found_exception import ProjectNotFoundException
from app.project.project_repository import ProjectRepository
from unit.app.project.project_mother import ProjectMother


class TestNifiService:

    def setup(self):
        self.project_repository: ProjectRepository = mock()
        self.flow_provider: FlowProvider = mock()

        self.service = NifiService(
            project_repository=self.project_repository,
            flow_provider=self.flow_provider
        )

    def test_get_flow_should_raise_project_not_found_when_project_not_exist(self):
        when(self.project_repository).get(ANY).thenReturn(None)

        with pytest.raises(ProjectNotFoundException) as e:
            self.service.get_flow("", "")

    def test_get_flow_should_raise_flow_not_found_when_flow_provider_return_none(self):
        project = ProjectMother.create()
        when(self.project_repository).get(ANY).thenReturn(project)
        when(self.flow_provider).get_flow(ANY).thenReturn(None)

        with pytest.raises(FlowNotFoundException) as e:
            self.service.get_flow("", "")
