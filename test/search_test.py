import unittest
import os
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.search.asset import File, Directory

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


class SearchTest(unittest.TestCase):
    """ Test to verify that can list all directories"""

    def test_get_all_directories_and_files(self):
        directories = ['dir1', 'dir2', 'files']
        files = ['file1.txt', 'file2.dat', 'file3.txt', 'dir_file.txt', 'file1_1.txt', 'diledir2.txt', 'none', 'sr.bat']
        search_test = Search().get_all_directories_and_files(PATH)
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

    def test_search_by_contain_common_name_that_returns_coincidences(self):
        search_test = Search().search_by_contain_common_name(PATH, "file")
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

    def test_search_by_contain_common_name_that_does_not_return_coincidences(self):
        search_test = Search().search_by_contain_common_name(PATH, "non_conicidences")
        # Count 0 files and directories
        cont = 0
        result_count = len(search_test)
        self.assertEqual(cont, result_count)

    def test_search_by_exact_common_name__without_extension_file_that_returns_coincidences(self):
        search_test = Search().search_by_exact_common_name(PATH, "none")
        directories = []
        files = ['none']
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

    def test_search_by_exact_common_name__without_extension_that_returns_coincidences(self):
        search_test = Search().search_by_exact_common_name(PATH, "file3")
        directories = []
        files = ['file3']
        directories_result = []
        files_result = []
        for item in search_test:
            if isinstance(item, File):
                files_result.append(item.get_file_name())
            elif isinstance(item, Directory):
                directories_result.append(item.get_dir_name())
        self.assertEqual(directories, directories_result)
        files.sort(key=str)
        files_result.sort(key=str)
        self.assertEqual(files, files_result)

    def test_search_by_exact_common_name_with_extension_that_returns_coincidences(self):
        search_test = Search().search_by_exact_common_name(PATH, "file3.txt")
        directories = []
        files = ['file3.txt']
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

    def test_search_by_exact_common_extension_with_point_that_returns_coincidences(self):
        search_test = Search().search_by_exact_common_extension(PATH, ".txt")
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


    def test_search_by_exact_common_extension_without_point_that_returns_coincidences(self):
        search_test = Search().search_by_exact_common_extension(PATH, "txt")
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

    def test_search_by_exact_common_extension_without_point_that_returns_coincidences(self):
        search_test = Search().search_by_exact_common_extension(PATH, "*.txt")
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

    def test_search_files_by_less_than_a_size_that_returns_coincidences(self):
        # Search less than 1 MB
        search_test = Search().search_files_by_less_than_a_size(PATH, 1)
        directories = []
        files = ['file1.txt', 'file2.dat', 'dir_file.txt', 'file1_1.txt', 'none', 'diledir2.txt', 'sr.bat']
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

    def test_search_files_by_bigger_than_a_size_that_returns_coincidences(self):
        # Search bigger than 1 MB
        search_test = Search().search_files_by_bigger_than_a_size(PATH, 1)
        directories = []
        files = ['file3.txt']
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
