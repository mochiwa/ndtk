from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.flow.nifi_service import NifiService
from container import Container

router = APIRouter(
    prefix="/nifi",
)


@router.get("/{project_id}/flow/{flow_id}")
@inject
def get_flow(
        project_id: str,
        flow_id: str,
        service: NifiService = Depends(Provide[Container.nifi_service])):
    return service.get_flow(project_id, flow_id)
