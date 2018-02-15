import os
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.search.directory import Directory


class FactoryAsset(object):

    def __init__(self):
        self._list_actual_directories_and_files = []
        self._first_root_path = ""

    def create_asset(self, path, is_sub_directory_search):
        result = []
        for root, directories, files in os.walk(path):
            if self._first_root_path == "":
                self._first_root_path = root
            if is_sub_directory_search:
                for directory in directories:
                    current_directory = Directory(os.path.join(root, directory), directory, False)
                    self._list_actual_directories_and_files.append(current_directory)
                for file in files:
                    sub_file = File(os.path.join(root, file), file, True)
                    self._list_actual_directories_and_files.append(sub_file)
            else:
                for directory in directories:
                    if self._first_root_path == root:
                        current_directory = Directory(os.path.join(root, directory), directory, False)
                        self._list_actual_directories_and_files.append(current_directory)
                for file in files:
                    if self._first_root_path == root:
                        current_file = File(os.path.join(root, file), file, True)
                        self._list_actual_directories_and_files.append(current_file)

    def get_list_actual_directories_and_files(self):
        return self._list_actual_directories_and_files

    def get_first_root_path(self):
        return self._first_root_path
