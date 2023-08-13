import uuid

from app.project.exception.project_not_found_exception import ProjectNotFoundException
from app.project.project import Project
from app.project.project_repository import ProjectRepository


class ProjectService:

    def __init__(self, project_repository: ProjectRepository):
        self._repository = project_repository

    def create_project(self, request: {}) -> Project:
        project = Project(str(uuid.uuid4()), request['project_name'], request['nifi_uri'])
        return self._repository.save(project)

    def get_project(self, project_id: str) -> Project:
        project = self._repository.get(project_id)
        if project is None:
            raise ProjectNotFoundException(project_id)
        return project

    def get_all_project(self) -> [Project]:
        return self._repository.get_all()

    def delete_project(self, project_id: str) -> None:
        self._repository.delete(project_id)
