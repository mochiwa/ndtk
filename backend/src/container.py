from dependency_injector import containers, providers

from app.flow.flow_provider import FlowProvider
from app.flow.flow_provider_nipyapi import FlowProviderNipyApi
from app.flow.nifi_service import NifiService
from app.project.project_repository_json import ProjectRepositoryJson
from app.project.project_service import ProjectService
from app.shared.file_manager import FileManager


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=['./src/config.ini'])
    wiring_config = containers.WiringConfiguration(modules=["app.rest.projects_router", "app.rest.flow_router"])

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
    flow_provider = providers.Factory(
        FlowProviderNipyApi
    )
    nifi_service = providers.Factory(
        NifiService,
        project_repository, flow_provider
    )
