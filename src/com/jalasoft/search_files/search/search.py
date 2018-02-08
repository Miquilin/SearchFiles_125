from src.com.jalasoft.search_files.search.factory_asset import FactoryAsset
from src.com.jalasoft.search_files.search.asset import File, Directory
from src.com.jalasoft.search_files.utils.logging_config import logger
import os,argparse


class Search(object):
    def __init__(self):
        pass

    def start_a_search(self, search_criteria):
        """Return all directories and files that were true with search criteria
                Args:
                search_criteria (SearchCriteria): The first parameter.

                Return:
                Array [Asset]: The return directories and/or files list.

                """
        logger.info("start_a_search : Enter")
        result = []
        if search_criteria.get_is_advance_search():
            result = self.get_advance_search(search_criteria)
        else:
            result = self.get_basic_search(search_criteria)
        logger.info("start_a_search : Exit")
        return result

    def get_basic_search(self, search_criteria):
        """Return all directories and files that were true with basic search criteria
                        Args:
                        search_criteria (SearchCriteria): The first parameter.

                        Return:
                        Array [Asset]: The return directories and/or files list.

                        """
        logger.info("get_basic_search : Enter")
        result = []
        factory_asset = FactoryAsset()
        factory_asset.create_asset(search_criteria.get_root_path(), search_criteria.get_is_include_sub_folders())
        if search_criteria.get_extension() != "":
            result = self.search_by_exact_common_extension(search_criteria.get_extension(), factory_asset.get_list_actual_directories_and_files())
        elif search_criteria.get_common_name() != "":
            result = self.search_by_contain_common_name(search_criteria.get_common_name(), factory_asset.get_list_actual_directories_and_files(), search_criteria.get_which_search())
        else:
            result = self.get_all_directories_and_files(search_criteria.get_root_path(), search_criteria.get_is_include_sub_folders())

        logger.info("get_basic_search : Exit")
        return result

    def get_advance_search(self, search_criteria):
        """Return all directories and files that were true with advance search criteria
                                Args:
                                search_criteria (SearchCriteria): The first parameter.

                                Return:
                                Array [Asset]: The return directories and/or files list.

                                """
        logger.info("get_advance_search : Enter")
        result = []
        is_there_a_result = False
        factory_asset = FactoryAsset()
        factory_asset.create_asset(search_criteria.get_root_path(), search_criteria.get_is_include_sub_folders())
        temporal_result = factory_asset.get_list_actual_directories_and_files()
        if search_criteria.get_extension() != "":
            temporal_result = self.search_by_exact_common_extension(search_criteria.get_extension(), temporal_result)
            is_there_a_result = True
        if search_criteria.get_less_size() != 0 or search_criteria.get_bigger_size() != 0:
            temporal_result = self.search_files_by_size(temporal_result, search_criteria.get_less_size(), search_criteria.get_bigger_size())
            is_there_a_result = True
        if search_criteria.get_is_exact_common_name():
            if search_criteria.get_common_name() != "":
                temporal_result = self.search_by_exact_common_name(search_criteria.get_common_name(), temporal_result, search_criteria.get_which_search())
                is_there_a_result = True
        else:
            if search_criteria.get_common_name() != "":
                temporal_result = self.search_by_contain_common_name(search_criteria.get_common_name(), temporal_result, search_criteria.get_which_search())
                is_there_a_result = True
        if search_criteria.get_content_word() != "":
            temporal_result = self.search_files_by_content(temporal_result, search_criteria.get_content_word())
            is_there_a_result = True
        if is_there_a_result:
            result = temporal_result
        logger.info("get_advance_search : Exit")
        return result

    def get_all_directories_and_files(self, root_path, is_sub_directory_search ):
        """Return all directories and files
        Args:
        path_absolute (str): The first parameter.
        param1 (str): The second parameter.

        Return:
        Array [Asset]: The return directories and/or files list.

        """
        logger.info("get_all_directories_and_files : Enter")
        factory_asset = FactoryAsset()
        factory_asset.create_asset(root_path, is_sub_directory_search)
        logger.info("get_all_directories_and_files : Exit")
        return factory_asset.get_list_actual_directories_and_files()

    def search_by_contain_common_name(self, common_name, actual_search_list, which_search=0):
        """
                Args:
                common_name (str): The first parameter.
                actual_search_list [Asset]: The second parameter.
                which_search (int): It can contains three values:
                    0: Search on Files ad directories
                    1: Search on Directories
                    2: Search on Files

                Return:
                Array [Asset]: The return directories and/or files list.

                """
        logger.info("search_by_contain_common_name : Enter")
        result = []
        for item in actual_search_list:
            if which_search == 0:
                if isinstance(item, File):
                    if common_name in item.get_file_name():
                        result.append(item)
                elif isinstance(item, Directory):
                    if common_name in item.get_dir_name():
                        result.append(item)
            elif which_search == 2:
                if isinstance(item, File):
                    if common_name in item.get_file_name():
                        result.append(item)
            elif which_search == 1:
                if isinstance(item, Directory):
                    if common_name in item.get_dir_name():
                        result.append(item)
        logger.info("search_by_contain_common_name : Exit")
        return result

    def search_by_exact_common_name(self, common_name, actual_search_list, which_search=0):
        """
                Args:
                common_name (str): The first parameter.
                actual_search_list [Asset]: The second parameter.
                which_search (int): It can contains three values:
                    0: Search on Files ad directories
                    1: Search on Directories
                    2: Search on Files

                Return:
                Array [Asset]: The return directories and/or files list.

                """
        logger.info("search_by_exact_common_name : Enter")
        result = []
        file_name, separator, extension = common_name.partition(".")
        for item in actual_search_list:
            if which_search == 0:
                if isinstance(item, File):
                    if extension != "":
                        if file_name == item.get_file_name() and extension == item.get_extension():
                            result.append(item)
                    else:
                        if file_name == item.get_file_name():
                            result.append(item)
                elif isinstance(item, Directory):
                    if common_name == item.get_dir_name():
                        result.append(item)
            elif which_search == 2:
                if isinstance(item, File):
                    file_name, separator, extension = common_name.partition(".")
                    if extension != "":
                        if file_name == item.get_file_name() and extension == item.get_extension():
                            result.append(item)
                    else:
                        if common_name == item.get_file_name():
                            result.append(item)
            elif which_search == 1:
                if isinstance(item, Directory):
                    if common_name == item.get_dir_name():
                        result.append(item)
        logger.info("search_by_exact_common_name : Exit")
        return result

    def search_by_exact_common_extension(self, common_extension, actual_search_list):
        """
                Args:
                common_extension (str): The first parameter.
                actual_search_list [Asset]: The second parameter.

                Return:
                Array [Asset]: The return files list that have exact common extension

                """
        logger.info("search_by_exact_common_extension : Enter")
        result = []
        if "." in common_extension:
            file_name, separator, extension = common_extension.partition(".")
        else:
            extension = common_extension
        for item in actual_search_list:
            if isinstance(item, File):
                if extension == item.get_extension():
                    result.append(item)
        logger.info("search_by_exact_common_extension : Exit")
        return result


    def search_files_by_size(self, actual_search_list, less_size, bigger_size):
        """
                Args:
                actual_search_list [Asset]: The first parameter.
                less_size (int): The second parameter.
                bigger_size (int): The second parameter.

                Return:
                Array [Asset]: The return directories and/or files list that have bigger than a size

                """
        logger.info("search_files_by_size : Enter")
        result = []
        for item in actual_search_list:
            if isinstance(item, File):
                item_mb = item.get_size() / (1024 * 1024)
                if less_size !=0 and bigger_size !=0:
                    if item_mb <= less_size and item_mb >= bigger_size:
                        result.append(item)
                elif less_size !=0 and bigger_size == 0:
                    if item_mb <= less_size :
                        result.append(item)
                elif less_size ==0 and bigger_size != 0:
                    if item_mb >= bigger_size :
                        result.append(item)
        logger.info("search_files_by_size : Exit")
        return result

    def search_files_by_content(self, actual_search_list, word_search):
        """
                Args:
                actual_search_list [Asset]: The first parameter.
                word_search (int): The second parameter.

                Return:
                Array [Asset]: The return files list that contains word_search

                """
        logger.info("search_files_by_content : Enter")
        result = []
        is_word_contains_on_file = False
        for item in actual_search_list:
            if isinstance(item, File):
                file_name = ""
                if item.get_separator() != "":
                    file_name = item.get_file_name() + item.get_separator() + item.get_extension()
                else:
                    file_name = item.get_file_name()
                with open(item.get_path()) as f:
                    for line in f:
                        if word_search in line:
                            is_word_contains_on_file = True
                            print("test::::", word_search)
                if is_word_contains_on_file:
                    result.append(item)
                    is_word_contains_on_file = False
        logger.info("search_files_by_content : Exit")
        return result

    def print_list_all(self, list_to_be_print):
        for item in list_to_be_print:
            print(item.get_path(), "test size", item.get_size() / (1024 * 1024))
