import uuid

from app.project.project import Project
from app.shared.file_manager import FileManager
from app.project.project_response import ProjectResponse


class ProjectService:

    def __init__(self, file_manager: FileManager):
        self._file_manager = file_manager

    def create_project(self, request: {}) -> ProjectResponse:
        project_id = uuid.uuid4()
        project = Project(str(project_id),
                          request['project_name'],
                          request['nifi_uri'])

        self._file_manager.create_dir(str(project_id))
        return ProjectResponse.from_project(project)
