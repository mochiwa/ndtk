import uuid

from app.project.project import Project


class ProjectMother:
    @classmethod
    def create(cls) -> Project:
        return Project(str(uuid.uuid4()), 'my project', 'http://')
