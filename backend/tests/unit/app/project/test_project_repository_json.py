import os
import shutil

from app.project.project_repository_json import ProjectRepositoryJson
from app.shared.file_manager import FileManager
from unit.app.project.project_mother import ProjectMother

tmp_path = os.path.join(os.path.dirname(__file__), 'tmp')


class TestProjectRepositoryJson:

    def setup(self):
        self.file = FileManager(tmp_path)
        self.repository = ProjectRepositoryJson(file_manager=self.file)

    def teardown(self):
        if os.path.exists(tmp_path):
            shutil.rmtree(tmp_path)

    def test_save_should_create_directory_with_project_id(self):
        project = ProjectMother.create()
        self.repository.save(project)

        assert os.path.exists(os.path.join(self.file.root_dir, project.project_id))

    def test_save_should_create_project_json_file_in_project_dir(self):
        project = ProjectMother.create()
        self.repository.save(project)

        assert os.path.exists(os.path.join(self.file.root_dir, project.project_id, 'project.json'))

    def test_save_should_return_the_project_saved(self):
        project = ProjectMother.create()
        output = self.repository.save(project)

        assert project == output

    def test_get_should_return_none_when_directory_not_exist(self):
        output = self.repository.get('')

        assert output is None

    def test_get_should_return_project_found(self):
        project = ProjectMother.create()
        self.repository.save(project)

        output = self.repository.get(project_id=project.project_id)

        assert output.project_id == project.project_id

    def test_get_all_should_return_empty_array_when_no_project(self):
        output = self.repository.get_all()

        assert len(output) == 0

    def test_get_all_should_return_array_of_all_project(self):
        project_1 = self.repository.save(ProjectMother.create())
        project_2 = self.repository.save(ProjectMother.create())

        output = [project.project_id for project in self.repository.get_all()]

        assert len(output) == 2
        assert project_1.project_id in output
        assert project_2.project_id in output

    def test_delete_should_delete_project_directory(self):
        project = ProjectMother.create()
        self.repository.save(project)

        self.repository.delete(project.project_id)

        assert os.path.exists(os.path.join(tmp_path, f"projects/{project.project_id}")) is False
