from dependency_injector import containers, providers

from app.project.project_repository_json import ProjectRepositoryJson
from app.project.project_service import ProjectService
from app.shared.file_manager import FileManager


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=['./src/config.ini'])
    wiring_config = containers.WiringConfiguration(modules=["app.rest.projects_router"])

    file_manager = providers.Factory(
        FileManager,
        config.provided['APP']['projects_directory']
    )
    project_repository = providers.Factory(
        ProjectRepositoryJson,
        file_manager
    )
    project_service = providers.Factory(
        ProjectService,
        project_repository
    )
