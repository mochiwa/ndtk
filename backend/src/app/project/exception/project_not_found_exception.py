from app.shared.exception.not_found_exception import NotFoundException


class ProjectNotFoundException(NotFoundException):

    def __init__(self, project_id: str):
        super().__init__(f"Project {project_id} not found.")
