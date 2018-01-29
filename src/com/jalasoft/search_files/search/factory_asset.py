#import File
import os
from src.com.jalasoft.search_files.search.asset import Asset, File, Directory


class FactoryAsset (object):

    def __init__(self):
        self._list_actual_directories_and_files = []

    def create_asset(self, path):
        result = []
        for root, directories, files in os.walk(path):
            for dir in directories:
                directory = Directory(os.path.join(root, dir),dir, False)
                self._list_actual_directories_and_files.append(directory)

            for file in files:
                sub_file = File(os.path.join(root, file),file, True)
                self._list_actual_directories_and_files.append(sub_file)

    def get_list_actual_directories_and_files(self):
        return self._list_actual_directories_and_files


