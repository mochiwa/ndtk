import json
import os
import shutil

import pytest

from app.shared.file_manager import FileManager

tmp_path = os.path.join(os.path.dirname(__file__), 'tmp')


class TestFileManager():

    def setup(self):
        self.service = FileManager(tmp_path)

    def teardown(self):
        shutil.rmtree(tmp_path, ignore_errors=True)

    def test_constructor_should_create_directory_projects_root_path(self):
        assert os.path.exists(os.path.join(tmp_path, 'projects'))
        assert os.path.exists(self.service.root_dir)
        assert self.service.root_dir == os.path.join(tmp_path, 'projects')

    def test_create_dir_should_create_directory_from_root_dir(self):
        output = self.service.create_dir("dir-1")
        assert os.path.exists(output)
        assert output == os.path.join(tmp_path, 'projects', 'dir-1')

    def test_create_dir_should_create_directory_nested_from_root_dir(self):
        output = self.service.create_dir("dir-1/dir-2/dir-3")
        assert os.path.exists(output)
        assert output == os.path.join(tmp_path, 'projects', 'dir-1', 'dir-2', 'dir-3')

    def test_write_file_should_create_file_at_path_with_content(self):
        self.service.write_file("", 'hello.js', "{'test': 'data'}")

        assert os.path.exists(os.path.join(self.service.root_dir, 'hello.js'))

    def test_write_file_should_raise_error_when_path_not_exist(self):
        with pytest.raises(FileNotFoundError) as e:
            self.service.write_file("test", 'hello.js', "{'test': 'data'}")

    def test_read_file_should_return_the_content_of_the_file(self):
        self.service.write_file("", 'hello.js', '{"test": "data"}')

        output = self.service.read_file("", "hello.js")

        assert json.loads(output)['test'] == 'data'

    def test_exist_should_return_boolean_when_file_exist_or_not(self):
        output = self.service.create_dir("dir_1")

        assert self.service.exist(output) is True
        assert self.service.exist('dir_1') is True
        assert self.service.exist('dir_2') is False

    def test_list_dir_should_return_all_directory_name_in_path(self):
        assert self.service.list_dir() == []

        self.service.create_dir("dir")
        assert self.service.list_dir() == ['dir']

    def test_delete_dir_should_delete_directory_and_content_of_dir_from_root(self):
        self.service.create_dir("dir")
        self.service.write_file("dir", "file", "hello")
        assert self.service.exist('dir/file')

        self.service.delete_directory('dir')
        assert self.service.exist('dir/file') is False
