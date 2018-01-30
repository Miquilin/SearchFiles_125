from src.com.jalasoft.search_files.search.factory_asset import FactoryAsset
from src.com.jalasoft.search_files.search.asset import File, Directory


class Search(object):
    def __init__(self):
        self._path = ""

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

    def search_by_contain_common_name(self, path_absolute, common_name, which_search=0):
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
        factory_asset = FactoryAsset()
        factory_asset.create_asset(path_absolute)
        for item in factory_asset.get_list_actual_directories_and_files():
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

    def search_by_exact_common_extension(self, path_absolute, common_extension):
        """
                Args:
                path_absolute (str): The first parameter.
                common_extension (str): The second parameter.

                Return:
                Array [Asset]: The return directories and/or files list that have exact common extension

                """
        result = []
        factory_asset = FactoryAsset()
        factory_asset.create_asset(path_absolute)
        if "." in common_extension:
            file_name, separator, extension = common_extension.partition(".")
        else:
            extension = common_extension
        for item in factory_asset.get_list_actual_directories_and_files():
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
                if item.get_size() / (1024 * 1224) < size_on_megabites:
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

                if item.get_size() / (1024 * 1224) > size_on_megabites:
                    result.append(item)
                    print("item.get_size()/(1024*1224)", item.get_size() / (1024 * 1224))

        return result

    def print_list_all(self, list_to_be_print):
        for item in list_to_be_print:
            print(item.get_path(), "test sixe", item.get_size() / (1024 * 1224))
