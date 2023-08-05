from dataclasses import dataclass

from app.project.project import Project


@dataclass
class ProjectResponse:
    project_id: str
    project_name: str
    nifi_uri: str

    @classmethod
    def from_project(cls, project: Project):
        return ProjectResponse(
            project_id=project.project_id,
            project_name=project.project_name,
            nifi_uri=project.nifi_uri)
