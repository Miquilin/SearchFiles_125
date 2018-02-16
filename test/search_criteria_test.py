import unittest
import os
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.search.directory import Directory


PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
PATH_SEARCH_BY_CONTENT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_by_content")

class SearchTest(unittest.TestCase):
    """ Test to verify that can list all directories"""

    def test_get_all_directories_and_files_with_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(True)
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

    def test_get_all_directories_and_files_with_non_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(False)
        search_test = Search().start_a_search(search_criteria)
        directories = ['dir1', 'dir2', 'files']
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

    def test_basic_search_by_contain_common_name_that_returns_coincidences_and_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("file")
        search_criteria.set_is_include_sub_folders(True)

        search_test = Search().start_a_search(search_criteria)
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

    def test_basic_search_by_contain_common_name_that_does_not_return_coincidences_and_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("non_considences")
        search_criteria.set_is_include_sub_folders(True)
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

    def test_basic_search_by_contain_common_name_that_returns_coincidences_and_non_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("file")
        search_criteria.set_is_include_sub_folders(False)

        search_test = Search().start_a_search(search_criteria)
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

    def test_basic_search_by_contain_common_extension_that_returns_coincidences_and_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("")
        search_criteria.set_extension("txt")
        search_criteria.set_is_include_sub_folders(True)

        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = ['file1.txt', 'file3.txt', 'dir_file.txt', 'file1_1.txt', 'diledir2.txt']
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

    def test_basic_search_by_asterisk_common_extension_that_returns_coincidences_and_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("")
        search_criteria.set_extension("*.txt")
        search_criteria.set_is_include_sub_folders(True)

        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = ['file1.txt', 'file3.txt', 'dir_file.txt', 'file1_1.txt', 'diledir2.txt']
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

    def test_basic_search_by_contain_common_extension_that_returns_coincidences_and_non_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(False)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("")
        search_criteria.set_extension("txt")
        search_criteria.set_is_include_sub_folders(False)

        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = ['file1.txt', 'file3.txt']
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

    def test_advance_search_by_contain_common_name_and_extension(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("sr")
        search_criteria.set_extension("bat")
        search_criteria.set_is_include_sub_folders(True)

        search_test = Search().start_a_search(search_criteria)
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

    def test_advance_search_by_contain_exact_common_name_and_extension(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("sr")
        search_criteria.set_extension("bat")
        search_criteria.set_is_exact_common_name(True)
        search_criteria.set_is_include_sub_folders(True)

        search_test = Search().start_a_search(search_criteria)
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

    def test_advance_search_by_contain_common_name_and_extension_and_non_include_sub_folders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_common_name("2")
        search_criteria.set_extension("dat")
        search_criteria.set_is_exact_common_name(False)
        search_criteria.set_is_include_sub_folders(False)

        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = ["file2.dat"]
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

    def test_advance_search_by_less_than_a_size_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_less_size(1)
        search_criteria.set_is_include_sub_folders(True)

        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = ['file1.txt', 'file2.dat', 'dir_file.txt', 'file1_1.txt', 'diledir2.txt', 'sr.bat']
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

    def test_advance_search_by_bigger_than_a_size_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_bigger_size(1)
        search_criteria.set_is_include_sub_folders(True)

        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = ['file3.txt', 'none']
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

    def test_advance_search_by_bigger_than_a_size_and_less_than_a_size_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_bigger_size(1)
        search_criteria.set_less_size(5)
        search_criteria.set_is_include_sub_folders(True)
        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = ['file3.txt', 'none']
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

    def test_advance_search_by_content_that_returns_a_coincidency_without_sub_forlders(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(False)
        search_criteria.set_content_word("qe")
        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = ['file1.txt']
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

    def test_advance_search_by_content_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH_SEARCH_BY_CONTENT)
        search_criteria.set_is_include_sub_folders(True)
        search_criteria.set_content_word("Ninoshka")
        search_test = Search().start_a_search(search_criteria)
        directories = []
        files = ['file1 - copia.log', "file1.txt", "example.xml", "install.log", "search_criteria_test.py", "The Complete List Blog.html", "style.css"]
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

    def test_advance_search_by_content_that_does_not_return_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH_SEARCH_BY_CONTENT)
        search_criteria.set_is_include_sub_folders(True)
        search_criteria.set_content_word("NOexist")
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

