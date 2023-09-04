from app.flow.flow import Flow


class FlowProvider:

    def get_flow(self, nifi_host: str, flow_id: str) -> Flow:
        pass
