import unittest
import os
import datetime
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.search.directory import Directory


PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


class SearchByDateTest(unittest.TestCase):

    def test_advance_search_by_less_creation_date_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(True)
        search_criteria.set_less_creation_date(datetime.datetime.now())
        search_test = Search().start_a_search(search_criteria)
        directories = ['dir1', 'dir2', 'files']
        files = ['file1.txt', 'file2.dat', 'file3.txt', 'dir_file.txt', 'file1_1.txt', 'diledir2.txt', 'none', 'sr.bat']
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

    def test_advance_search_by_bigger_creation_date_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(True)
        search_criteria.set_bigger_creation_date(datetime.datetime.now())
        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = []
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

    def test_advance_search_by_bigger_creation_date_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(True)
        search_criteria.set_bigger_creation_date(datetime.datetime.fromtimestamp(1518526276))
        search_test = Search().start_a_search(search_criteria)
        directories = ['dir1', 'dir2', 'files']
        files = ['file1.txt', 'file2.dat', 'file3.txt', 'dir_file.txt', 'file1_1.txt', 'diledir2.txt', 'none', 'sr.bat']
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


    def test_advance_search_by_less_modification_date_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(True)
        search_criteria.set_less_modification_date(datetime.datetime.now())
        search_test = Search().start_a_search(search_criteria)
        directories = ['dir1', 'dir2', 'files']
        files = ['file1.txt', 'file2.dat', 'file3.txt', 'dir_file.txt', 'file1_1.txt', 'diledir2.txt', 'none', 'sr.bat']
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

    def test_advance_search_by_bigger_modification_date_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(True)
        search_criteria.set_bigger_modification_date(datetime.datetime.now())
        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = []
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

    def test_advance_search_by_bigger_modification_date_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(True)
        search_criteria.set_bigger_modification_date(datetime.datetime.fromtimestamp(1518526276))
        search_test = Search().start_a_search(search_criteria)
        directories = ['dir1', 'dir2', 'files']
        files = ['file1.txt', 'file2.dat', 'file3.txt', 'dir_file.txt', 'file1_1.txt', 'diledir2.txt', 'none', 'sr.bat']
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
