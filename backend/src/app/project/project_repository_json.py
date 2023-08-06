import json
import uuid

from app.project.project import Project
from app.project.project_repository import ProjectRepository
from app.shared.file_manager import FileManager


class ProjectRepositoryJson(ProjectRepository):

    def __init__(self, file_manager: FileManager):
        self._file = file_manager

    def save(self, project: Project) -> Project:
        self._file.create_dir(project.project_id)
        self._file.write_file(project.project_id, 'project.json', json.dumps(project.__dict__))
        return project

    def get(self, project_id: uuid) -> Project | None:
        if self._file.exist(project_id) is False:
            return None
        stream = self._file.read_file(project_id, 'project.json')
        return Project(**json.loads(stream))
