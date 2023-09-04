from app.shared.exception.not_found_exception import NotFoundException


class FlowNotFoundException(NotFoundException):

    def __init__(self, flow_id:str):
        super().__init__(f"Flow '{flow_id}' not found.")
