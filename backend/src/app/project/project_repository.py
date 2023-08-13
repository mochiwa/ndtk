import uuid

from app.project.project import Project


class ProjectRepository:

    def save(self, project: Project) -> Project:
        raise NotImplementedError()

    def get(self, project_id: uuid) -> Project | None:
        raise NotImplementedError()

    def get_all(self) -> [Project]:
        raise NotImplementedError()

    def delete(self, project_id: str):
        raise NotImplementedError()
