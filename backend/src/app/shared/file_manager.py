import os


class FileManager:
    PROJECT_DIR = "projects"

    def __init__(self, root_path: str):
        self._root_path = os.path.join(root_path, FileManager.PROJECT_DIR)

    def create_dir(self, path: str, ok_exist: bool = True):
        full_path = f"{self._root_path}/{path}"
        os.makedirs(full_path, exist_ok=ok_exist)
        return full_path
