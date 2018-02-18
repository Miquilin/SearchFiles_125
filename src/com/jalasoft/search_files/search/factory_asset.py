import os
import win32security
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.search.directory import Directory
from src.com.jalasoft.search_files.utils.logging_config import logger


class FactoryAsset(object):
    """ Class FactoryAsset """

    def __init__(self):
        """
                initial data by default
                                        Args:
                                            self._list_actual_directories_and_files [Asset] : It contains initial asset list
                                            self._first_root_path (string) : It contains the first path to only search on the actual path

                                        """
        self._list_actual_directories_and_files = []
        self._first_root_path = ""

    def create_asset(self, path, is_sub_directory_search):
        """Store all directories and/or files that are present under root path
                        Args:
                        path (String): The first parameter.
                        is_sub_directory_search (boolean): The Second parameter.

                        """
        logger.info("Starting the method")
        for root, directories, files in os.walk(path):
            if self._first_root_path == "":
                self._first_root_path = root
            if is_sub_directory_search:
                for directory in directories:
                    current_directory = Directory(os.path.join(root, directory), directory, False)
                    current_directory.set_owner(self.get_owner(current_directory.get_path()))
                    self._list_actual_directories_and_files.append(current_directory)
                for file in files:
                    sub_file = File(os.path.join(root, file), file, True)
                    sub_file.set_owner(self.get_owner(sub_file.get_path()))
                    self._list_actual_directories_and_files.append(sub_file)
            else:
                for directory in directories:
                    if self._first_root_path == root:
                        current_directory = Directory(os.path.join(root, directory), directory, False)
                        current_directory.set_owner(self.get_owner(current_directory.get_path()))
                        self._list_actual_directories_and_files.append(current_directory)
                for file in files:
                    if self._first_root_path == root:
                        current_file = File(os.path.join(root, file), file, True)
                        current_file.set_owner(self.get_owner(current_file.get_path()))
                        self._list_actual_directories_and_files.append(current_file)
        logger.info("Ending the method")

    def get_list_actual_directories_and_files(self):
        """ Return all directories and/or files that are present under root path that sent on  function
                                Args:

                                Return:
                                Array [Asset]: The return directories and/or files list.

                                """
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._list_actual_directories_and_files

    def get_first_root_path(self):
        """Return the first path to search on the actual directory
                                Args:

                                Return:
                                Array [Asset]: List of directories and/or files list.

                                """
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._first_root_path

    def get_owner(self, path):
        """Return actual owner of a Windows path
                                Args:
                                path (String): The first parameter.

                                Return:
                                owner [String]: Return actual owner of a Windows path

                                """
        logger.info("Starting the method")
        security_description = win32security.GetFileSecurity(path,
                                           win32security.OWNER_SECURITY_INFORMATION)
        sid = security_description.GetSecurityDescriptorOwner()
        logger.info("Ending the method")
        return win32security.LookupAccountSid(None, sid)[0]
