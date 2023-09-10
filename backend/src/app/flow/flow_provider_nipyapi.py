import nipyapi
from nipyapi.nifi import ProcessGroupFlowEntity, ApiClient
from urllib3.exceptions import MaxRetryError

from app.flow.flow import Flow
from app.flow.flow_mapper import mapping_flow
from app.flow.flow_provider import FlowProvider


class FlowProviderNipyApi(FlowProvider):

    def get_flow(self, nifi_host: str, flow_id: str) -> Flow:
        nipyapi.utils.set_endpoint(nifi_host)
        entity: ProcessGroupFlowEntity = nipyapi.canvas.get_flow(flow_id)
        return mapping_flow(entity)
