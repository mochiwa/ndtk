import os
import shutil


class FileManager:
    PROJECT_DIR = "projects"

    def __init__(self, root_path: str):
        self._root_path = os.path.join(root_path, FileManager.PROJECT_DIR)
        os.makedirs(self._root_path, exist_ok=True)

    @property
    def root_dir(self) -> str:
        return self._root_path

    def create_dir(self, path: str, ok_exist: bool = True):
        full_path = f"{self._root_path}/{path}"
        os.makedirs(full_path, exist_ok=ok_exist)
        return full_path

    def write_file(self, path: str, filename: str, content: str):
        with open(os.path.join(self._root_path, path, filename), 'w') as file:
            file.write(content)

    def read_file(self, path: str, filename: str) -> str:
        with open(os.path.join(self._root_path, path, filename), 'r') as file:
            return file.read()

    def exist(self, path: str) -> bool:
        return os.path.exists(os.path.join(self._root_path, path))

    def list_dir(self) -> [str]:
        return os.listdir(self._root_path)

    def delete_directory(self, dir_name: str):
        shutil.rmtree(os.path.join(self._root_path, dir_name), ignore_errors=True)
