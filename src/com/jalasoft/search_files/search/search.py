from src.com.jalasoft.search_files.search.factory_asset import FactoryAsset
from src.com.jalasoft.search_files.search.asset import File, Directory
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria

class Search(object):
    def __init__(self):
        pass

    def get_search(self,search_criteria):
        if search_criteria.get_is_advance_search():
            return self.get_advance_search(search_criteria)
        else:
            return self.get_basic_search(search_criteria)

    def get_basic_search(self, search_criteria):
        result = []
        factory_asset = FactoryAsset()
        factory_asset.create_asset(search_criteria.get_root_path(), search_criteria.get_is_include_sub_folders())
        if search_criteria.get_extension() != "":
            result = self.search_by_exact_common_extension(search_criteria.get_extension(), factory_asset.get_list_actual_directories_and_files())
        elif search_criteria.get_common_name() != "":
            result = self.search_by_contain_common_name(search_criteria.get_common_name(),  factory_asset.get_list_actual_directories_and_files(), search_criteria.get_which_search())
        return result


    def get_advance_search(self, search_criteria):
        result = []
        factory_asset = FactoryAsset()
        factory_asset.create_asset(search_criteria.get_root_path(), search_criteria.get_is_include_sub_folders())
        temporal_result = factory_asset.get_list_actual_directories_and_files()
        if search_criteria.get_extension() != "":
            temporal_result = self.search_by_exact_common_extension(search_criteria.get_extension(), temporal_result)
        elif search_criteria.get_less_size() != 0 or search_criteria.get_bigger_size() != 0:
            temporal_result = self.search_files_by_size( temporal_result, search_criteria.get_less_size(), search_criteria.get_bigger_size())
        elif search_criteria.get_common_name() != "":
            temporal_result = self.search_by_contain_common_name( search_criteria.get_common_name(), temporal_result, search_criteria.get_which_search())

        return temporal_result

    def get_all_directories_and_files(self, path_absolute):
        """Return all directories and files
        Args:
        path_absolute (str): The first parameter.
        param1 (str): The second parameter.

        Return:
        Array [Asset]: The return directories and/or files list.

        """
        factory_asset = FactoryAsset()
        factory_asset.create_asset(path_absolute)
        self.print_list_all(factory_asset.get_list_actual_directories_and_files())
        return factory_asset.get_list_actual_directories_and_files()

    def search_by_contain_common_name(self, common_name, actual_search_list, which_search=0):
        """
                Args:
                path_absolute (str): The first parameter.
                common_name (str): The second parameter.
                which_search (int): It can contains three values:
                    0: Search on Files ad directories
                    1: Search on Directories
                    2: Search on Files

                Return:
                Array [Asset]: The return directories and/or files list.

                """
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

        return result

    def search_by_exact_common_name(self, path_absolute, common_name, which_search=0):
        """
                Args:
                path_absolute (str): The first parameter.
                common_name (str): The second parameter.
                which_search (int): It can contains three values:
                    0: Search on Files ad directories
                    1: Search on Directories
                    2: Search on Files

                Return:
                Array [Asset]: The return directories and/or files list that have exact common name

                """
        result = []
        factory_asset = FactoryAsset()
        factory_asset.create_asset(path_absolute)
        file_name, separator, extension = common_name.partition(".")
        for item in factory_asset.get_list_actual_directories_and_files():
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

        return result

    def search_by_exact_common_extension(self, common_extension, actual_search_list):
        """
                Args:
                path_absolute (str): The first parameter.
                common_extension (str): The second parameter.

                Return:
                Array [Asset]: The return directories and/or files list that have exact common extension

                """
        result = []
        if "." in common_extension:
            file_name, separator, extension = common_extension.partition(".")
        else:
            extension = common_extension
        for item in actual_search_list:
            if isinstance(item, File):
                if extension == item.get_extension():
                    result.append(item)

        return result

    def search_files_by_less_than_a_size(self, path_absolute, size_on_megabites):
        """
                Args:
                path_absolute (str): The first parameter.
                size_on_megabites (int): The second parameter.

                Return:
                Array [Asset]: The return directories and/or files list that have less than a size

                """
        result = []
        factory_asset = FactoryAsset()
        factory_asset.create_asset(path_absolute)
        for item in factory_asset.get_list_actual_directories_and_files():
            if isinstance(item, File):
                if item.get_size() / (1024 * 1024) < size_on_megabites:
                    result.append(item)

        return result

    def search_files_by_bigger_than_a_size(self, path_absolute, size_on_megabites):
        """
                Args:
                path_absolute (str): The first parameter.
                size_on_megabites (int): The second parameter.

                Return:
                Array [Asset]: The return directories and/or files list that have bigger than a size

                """
        result = []
        factory_asset = FactoryAsset()
        factory_asset.create_asset(path_absolute)
        for item in factory_asset.get_list_actual_directories_and_files():
            if isinstance(item, File):

                if item.get_size() / (1024 * 1024) > size_on_megabites:
                    result.append(item)
                    print("item.get_size()/(1024*1024)", item.get_size() / (1024 * 1024))

        return result

    def search_files_by_size(self, actual_search_list, less_size, bigger_size):
        """
                Args:
                actual_search_list (List): The first parameter.
                less_size (int): The second parameter.
                bigger_size (int): The second parameter.

                Return:
                Array [Asset]: The return directories and/or files list that have bigger than a size

                """
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


        return result

    def print_list_all(self, list_to_be_print):
        for item in list_to_be_print:
            print(item.get_path(), "test size", item.get_size() / (1024 * 1024))
