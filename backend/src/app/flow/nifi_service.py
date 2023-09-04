from app.flow.flow import Flow
from app.flow.flow_not_found_exception import FlowNotFoundException
from app.flow.flow_provider import FlowProvider
from app.project.exception.project_not_found_exception import ProjectNotFoundException
from app.project.project_repository import ProjectRepository


class NifiService:
    def __init__(self, project_repository: ProjectRepository,
                 flow_provider: FlowProvider):
        self._project_repository = project_repository
        self._flow_provider = flow_provider

    def get_flow(self, project_id: str, flow_id: str) -> Flow:
        project = self._project_repository.get(project_id)
        if project is None:
            raise ProjectNotFoundException(project_id)
        flow = self._flow_provider.get_flow(project.nifi_uri, flow_id)
        if flow is None:
            raise FlowNotFoundException(flow_id)
        return flow
