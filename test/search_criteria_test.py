import unittest
import os
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria
from src.com.jalasoft.search_files.search.asset import File, Directory

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


class SearchTest(unittest.TestCase):
    """ Test to verify that can list all directories"""

    def test_search_by_contain_common_name_that_returns_coincidences_and_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("file")
        search_criteria.set_is_include_sub_folders(True)

        search_test = Search().get_search(search_criteria)
        directories = ['files']
        files = ['file1.txt', 'file2.dat', 'file3.txt', 'dir_file.txt', 'file1_1.txt']
        directories_result = []
        files_result = []
        for item in search_test:
            if isinstance(item, File):
                if item.get_extension() != "":
                    files_result.append(item.get_file_name() + item.get_separator() + item.get_extension())
                else:
                    files_result.append(item.get_file_name())
            elif isinstance(item, Directory):
                directories_result.append(item.get_dir_name())
        self.assertEqual(directories, directories_result)
        files.sort(key=str)
        files_result.sort(key=str)
        self.assertEqual(files, files_result)

    def test_search_by_contain_common_name_that_returns_coincidences_and_non_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("file")
        search_criteria.set_is_include_sub_folders(False)

        search_test = Search().get_search(search_criteria)
        directories = ['files']
        files = ['file1.txt', 'file2.dat', 'file3.txt']
        directories_result = []
        files_result = []
        for item in search_test:
            if isinstance(item, File):
                if item.get_extension() != "":
                    files_result.append(item.get_file_name() + item.get_separator() + item.get_extension())
                else:
                    files_result.append(item.get_file_name())
            elif isinstance(item, Directory):
                directories_result.append(item.get_dir_name())
        self.assertEqual(directories, directories_result)
        files.sort(key=str)
        files_result.sort(key=str)
        self.assertEqual(files, files_result)

    def test_search_by_contain_common_name_that_returns_coincidences_and_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("sr")
        search_criteria.set_extension("bat")
        search_criteria.set_is_include_sub_folders(True)

        search_test = Search().get_search(search_criteria)
        directories = []
        files = ['sr.bat']
        directories_result = []
        files_result = []
        for item in search_test:
            if isinstance(item, File):
                if item.get_extension() != "":
                    files_result.append(item.get_file_name() + item.get_separator() + item.get_extension())
                else:
                    files_result.append(item.get_file_name())
            elif isinstance(item, Directory):
                directories_result.append(item.get_dir_name())
        self.assertEqual(directories, directories_result)
        files.sort(key=str)
        files_result.sort(key=str)
        self.assertEqual(files, files_result)


if __name__ == "__main__":
    unittest.main()
