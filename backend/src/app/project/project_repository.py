import uuid

from app.project.project import Project


class ProjectRepository:

    def save(self, project: Project) -> Project:
        raise NotImplementedError()

    def get(self, project_id: uuid) -> Project | None:
        raise NotImplementedError()
