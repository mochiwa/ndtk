from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.project.project_service import ProjectService
from container import Container

router = APIRouter(
    prefix="/projects",
)


@router.post("/", status_code=200)
@inject
def create_project(
        payload: dict,
        service: ProjectService = Depends(Provide[Container.project_service])):
    return service.create_project(payload)


@router.get('/{project_id}')
@inject
def get_project(
        project_id: str,
        service: ProjectService = Depends(Provide[Container.project_service])):
    return service.get_project(project_id)


@router.get('/')
@inject
def get_all_project(
        service: ProjectService = Depends(Provide[Container.project_service])):
    return service.get_all_project()


@router.delete('/{project_id}', status_code=200)
@inject
def delete_project(
        project_id: str,
        service: ProjectService = Depends(Provide[Container.project_service])):
    service.delete_project(project_id)
