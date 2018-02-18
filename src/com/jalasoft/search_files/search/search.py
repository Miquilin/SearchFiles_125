from src.com.jalasoft.search_files.search.factory_asset import FactoryAsset
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.search.directory import Directory
from src.com.jalasoft.search_files.utils.logging_config import logger
import definition


class Search(object):
    """ Class Search """
    def __init__(self):
        pass

    def start_a_search(self, search_criteria):
        """Return all directories and files that were true with search criteria
                Args:
                search_criteria (SearchCriteria): The first parameter.

                Return:
                Array [Asset]: The return directories and/or files list.

                """
        logger.info("Starting the method")
        result_asert_list = []
        if search_criteria.get_is_advance_search():
            result_asert_list = self.get_advance_search(search_criteria)
        else:
            result_asert_list = self.get_basic_search(search_criteria)
        logger.info("Ending the method")
        return result_asert_list

    def get_basic_search(self, search_criteria):
        """Return all directories and files that were true with basic search criteria
                        Args:
                        search_criteria (SearchCriteria): The first parameter.

                        Return:
                        Array [Asset]: The return directories and/or files list.

                        """
        logger.info("Starting the method")
        result_asert_list = []
        factory_asset = FactoryAsset()
        factory_asset.create_asset(search_criteria.get_root_path(), search_criteria.get_is_include_sub_folders())
        if search_criteria.get_extension() != "":
            result_asert_list = self.search_by_exact_common_extension(search_criteria.get_extension(), factory_asset.get_list_actual_directories_and_files())
        elif search_criteria.get_common_name() != "":
            result_asert_list = self.search_by_contain_common_name(search_criteria.get_common_name(), factory_asset.get_list_actual_directories_and_files(), search_criteria.get_which_search())
        else:
            result_asert_list = self.get_all_directories_and_files(search_criteria.get_root_path(), search_criteria.get_is_include_sub_folders())

        logger.info("Ending the method")
        return result_asert_list

    def get_advance_search(self, search_criteria):
        """Return all directories and files that were true with advance search criteria
                                Args:
                                search_criteria (SearchCriteria): The first parameter.

                                Return:
                                Array [Asset]: The return directories and/or files list.

                                """
        logger.info("Starting the method")
        result_asert_list = []
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
        if search_criteria.get_less_creation_date() is not None or search_criteria.get_bigger_creation_date() is not None:
            temporal_result = self.search_files_by_creation_date(temporal_result, search_criteria.get_less_creation_date(), search_criteria.get_bigger_creation_date(), search_criteria.get_which_search())
            is_there_a_result = True
        if search_criteria.get_less_modification_date() is not None or search_criteria.get_bigger_modification_date() is not None:
            temporal_result = self.search_files_by_modification_date(temporal_result, search_criteria.get_less_modification_date(), search_criteria.get_bigger_modification_date(), search_criteria.get_which_search())
            is_there_a_result = True
        if search_criteria.get_owner() != "":
            temporal_result = self.search_files_by_owner(temporal_result, search_criteria.get_owner(), search_criteria.get_which_search())
            is_there_a_result = True
        if search_criteria.get_content_word() != "":
            temporal_result = self.search_files_by_content_on_text_files(temporal_result, search_criteria.get_content_word())
            is_there_a_result = True
        if is_there_a_result:
            result_asert_list = temporal_result
        logger.info("Ending the method")
        return result_asert_list

    def get_all_directories_and_files(self, root_path, is_sub_directory_search ):
        """Return all directories and files
        Args:
        path_absolute (str): The first parameter.
        param1 (str): The second parameter.

        Return:
        Array [Asset]: The return directories and/or files list.

        """
        logger.info("Starting the method")
        factory_asset = FactoryAsset()
        factory_asset.create_asset(root_path, is_sub_directory_search)
        logger.info("Ending the method")
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
        logger.info("Starting the method")
        result_asert_list = []
        for item in actual_search_list:
            if which_search == 0:
                if isinstance(item, File):
                    if common_name in item.get_file_name():
                        result_asert_list.append(item)
                elif isinstance(item, Directory):
                    if common_name in item.get_dir_name():
                        result_asert_list.append(item)
            elif which_search == 2:
                if isinstance(item, File):
                    if common_name in item.get_file_name():
                        result_asert_list.append(item)
            elif which_search == 1:
                if isinstance(item, Directory):
                    if common_name in item.get_dir_name():
                        result_asert_list.append(item)
        logger.info("Ending the method")
        return result_asert_list

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
        logger.info("Starting the method")
        result_asert_list = []
        file_name, separator, extension = common_name.partition(".")
        for item in actual_search_list:
            if which_search == 0:
                if isinstance(item, File):
                    if extension != "":
                        if file_name == item.get_file_name() and extension == item.get_extension():
                            result_asert_list.append(item)
                    else:
                        if file_name == item.get_file_name():
                            result_asert_list.append(item)
                elif isinstance(item, Directory):
                    if common_name == item.get_dir_name():
                        result_asert_list.append(item)
            elif which_search == 2:
                if isinstance(item, File):
                    file_name, separator, extension = common_name.partition(".")
                    if extension != "":
                        if file_name == item.get_file_name() and extension == item.get_extension():
                            result_asert_list.append(item)
                    else:
                        if common_name == item.get_file_name():
                            result_asert_list.append(item)
            elif which_search == 1:
                if isinstance(item, Directory):
                    if common_name == item.get_dir_name():
                        result_asert_list.append(item)
        logger.info("Ending the method")
        return result_asert_list

    def search_by_exact_common_extension(self, common_extension, actual_search_list):
        """
                Args:
                common_extension (str): The first parameter.
                actual_search_list [Asset]: The second parameter.

                Return:
                Array [Asset]: The return files list that have exact common extension

                """
        logger.info("Starting the method")
        result_asert_list = []
        if "." in common_extension:
            file_name, separator, extension = common_extension.partition(".")
        else:
            extension = common_extension
        for item in actual_search_list:
            if isinstance(item, File):
                if extension == item.get_extension():
                    result_asert_list.append(item)
        logger.info("Ending the method")
        return result_asert_list


    def search_files_by_size(self, actual_search_list, less_size, bigger_size):
        """
                Args:
                actual_search_list [Asset]: The first parameter.
                less_size (int): The second parameter.
                bigger_size (int): The second parameter.

                Return:
                Array [Asset]: The return directories and/or files list that have bigger than a size

                """
        logger.info("Starting the method")
        result_asert_list = []
        for item in actual_search_list:
            if isinstance(item, File):
                item_mb = item.get_size() / (1024 * 1024)
                if less_size != 0 and bigger_size != 0:
                    if less_size >= item_mb >= bigger_size:
                        result_asert_list.append(item)
                elif less_size != 0 and bigger_size == 0:
                    if item_mb <= less_size :
                        result_asert_list.append(item)
                elif less_size == 0 and bigger_size != 0:
                    if item_mb >= bigger_size :
                        result_asert_list.append(item)
        logger.info("Ending the method")
        return result_asert_list

    def search_files_by_content_on_text_files(self, actual_search_list, word_search):
        """
                Args:
                actual_search_list [Asset]: The first parameter.
                word_search (int): The second parameter.

                Return:
                Array [Asset]: The return files list that contains word_search

                """
        logger.info("Starting the method")
        result_asert_list = []
        is_word_contains_on_file = False
        for item in actual_search_list:
            if isinstance(item, File):
                if item.get_separator() != "" and item.get_extension() in definition.SEARCH_BY_CONTENT_ENABLE_EXTENSION_LIST:
                    with open(item.get_path()) as f:
                        for line in f:
                            if word_search in line:
                                is_word_contains_on_file = True
                    if is_word_contains_on_file:
                        result_asert_list.append(item)
                        is_word_contains_on_file = False
        logger.info("Ending the method")
        return result_asert_list

    def search_files_by_creation_date(self, actual_search_list, less_date, bigger_date, which_search=0):
        """
                Args:
                actual_search_list [Asset]: The first parameter.
                less_date [Date]: The second parameter.
                bigger_date [Date]: The third parameter.
                which_search (int): It can contains three values:
                    0: Search on Files ad directories
                    1: Search on Directories
                    2: Search on Files

                Return:
                Array [Asset]: The return directories and/or files list.

                """
        logger.info("Starting the method")
        result_asert_list = []
        for item in actual_search_list:
            if which_search == 0:
                if isinstance(item, File) or isinstance(item, Directory):
                    if less_date is not None and bigger_date is not None:
                        if less_date >= item.get_st_creation_time() >= bigger_date:
                            result_asert_list.append(item)
                    elif less_date is not None and bigger_date is None:
                        if item.get_st_creation_time() <= less_date:
                            result_asert_list.append(item)
                    elif less_date is None and bigger_date is not None:
                        if item.get_st_creation_time() >= bigger_date:
                            result_asert_list.append(item)
            elif which_search == 2:
                if isinstance(item, File):
                    if less_date is not None and bigger_date is not None:
                        if less_date >= item.get_st_creation_time() >= bigger_date:
                            result_asert_list.append(item)
                    elif less_date is not None and bigger_date is None:
                        if item.get_st_creation_time() <= less_date:
                            result_asert_list.append(item)
                    elif less_date is None and bigger_date is not None:
                        if item.get_st_creation_time() >= bigger_date:
                            result_asert_list.append(item)
            elif which_search == 1:
                if isinstance(item, Directory):
                    if less_date is not None and bigger_date is not None:
                        if less_date >= item.get_st_creation_time() >= bigger_date:
                            result_asert_list.append(item)
                    elif less_date is not None and bigger_date is None:
                        if item.get_st_creation_time() <= less_date:
                            result_asert_list.append(item)
                    elif less_date is None and bigger_date is not None:
                        if item.get_st_creation_time() >= bigger_date:
                            result_asert_list.append(item)
        logger.info("Ending the method")
        return result_asert_list

    def search_files_by_modification_date(self, actual_search_list, less_date, bigger_date, which_search=0):
        """
                Args:
                actual_search_list [Asset]: The first parameter.
                less_date [Date]: The second parameter.
                bigger_date [Date]: The third parameter.
                which_search (int): It can contains three values:
                    0: Search on Files ad directories
                    1: Search on Directories
                    2: Search on Files

                Return:
                Array [Asset]: The return directories and/or files list.

                """
        logger.info("Starting the method")
        result_asert_list = []
        for item in actual_search_list:
            if which_search == 0:
                if isinstance(item, File) or isinstance(item, Directory):
                    if less_date is not None and bigger_date is not None:
                        if less_date >= item.get_st_modification_time() >= bigger_date:
                            result_asert_list.append(item)
                    elif less_date is not None and bigger_date is None:
                        if item.get_st_modification_time() <= less_date:
                            result_asert_list.append(item)
                    elif less_date is None and bigger_date is not None:
                        if item.get_st_modification_time() >= bigger_date:
                            result_asert_list.append(item)
            elif which_search == 2:
                if isinstance(item, File):
                    if less_date is not None and bigger_date is not None:
                        if less_date >= item.get_st_modification_time() >= bigger_date:
                            result_asert_list.append(item)
                    elif less_date is not None and bigger_date is None:
                        if item.get_st_modification_time() <= less_date:
                            result_asert_list.append(item)
                    elif less_date is None and bigger_date is not None:
                        if item.get_st_modification_time() >= bigger_date:
                            result_asert_list.append(item)
            elif which_search == 1:
                if isinstance(item, Directory):
                    if less_date is not None and bigger_date is not None:
                        if less_date >= item.get_st_modification_time() >= bigger_date:
                            result_asert_list.append(item)
                    elif less_date is not None and bigger_date is None:
                        if item.get_st_modification_time() <= less_date:
                            result_asert_list.append(item)
                    elif less_date is None and bigger_date is not None:
                        if item.get_st_modification_time() >= bigger_date:
                            result_asert_list.append(item)
        logger.info("Ending the method")
        return result_asert_list

    def search_files_by_owner(self, actual_search_list, owner, which_search=0):
        """
                Args:
                actual_search_list [Asset]: The first parameter.
                less_date [Date]: The second parameter.
                bigger_date [Date]: The third parameter.
                which_search (int): It can contains three values:
                    0: Search on Files ad directories
                    1: Search on Directories
                    2: Search on Files

                Return:
                Array [Asset]: The return directories and/or files list.

                """
        logger.info("Starting the method")
        result_asert_list = []
        for item in actual_search_list:
            if which_search == 0:
                if isinstance(item, File) or isinstance(item, Directory):
                    if item.get_owner() in owner:
                        result_asert_list.append(item)
            elif which_search == 2:
                if isinstance(item, File):
                    if item.get_owner() in owner:
                        result_asert_list.append(item)
            elif which_search == 1:
                if isinstance(item, Directory):
                    if item.get_owner() in owner:
                        result_asert_list.append(item)
        logger.info("Ending the method")
        return result_asert_list
