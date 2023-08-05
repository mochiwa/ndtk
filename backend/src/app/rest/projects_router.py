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
