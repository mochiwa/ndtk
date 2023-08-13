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
        try:
            stream = self._file.read_file(project_id, 'project.json')
            return Project(**json.loads(stream))
        except:
            return None

    def get_all(self) -> [Project]:
        if self._file.exist('/') is False:
            return []
        return [self.get(project_id) for project_id in self._file.list_dir()]

    def delete(self, project_id: str):
        self._file.delete_directory(project_id)
