from src.com.jalasoft.search_files.utils.logging_config import logger


class SearchCriteria(object):
    """ Class SearchCriteria """

    def __init__(self):
        """
        initial data by default
                                Args:
                                    self._root_path (String) : It contains root path
                                    self._is_advance_search (boolean) : search criteria by default is False
                                    #basic_search
                                    self._common_name (String) : It contains common name criteria
                                    self._extension (String) : It contains extension criteria
                                    self._is_include_sub_folders (boolean) : search criteria by default is True
                                    #Advance_search
                                    self._is_exact_common_name (boolean) : search criteria by default is False
                                    self._less_size (int)
                                    self._bigger_size (int)
                                    self._which_search (int)
                                    self._content_word (String) : It contains contain criteria
                                    self._owner (String) : It contains exact owner criteria
                                    self._less_creation_date (date)
                                    self._bigger_creation_date (date)
                                    self._less_modification_date (date)
                                    self._bigger_modification_date (date)
                                    self.which_search (int): It can contain three values:
                                        0: Search on Files ad directories
                                        1: Search on Directories
                                        2: Search on Files


                                """

        self._root_path = ""
        self._is_advance_search = False
        #basic_search
        self._common_name = ""
        self._extension = ""
        self._is_include_sub_folders = True
        #Advance_search
        self._is_exact_common_name = False
        self._less_size = 0
        self._bigger_size = 0
        self._which_search = 0
        self._content_word = ""
        self._owner = ""
        self._less_creation_date = None
        self._bigger_creation_date = None
        self._less_modification_date = None
        self._bigger_modification_date = None

    def set_which_search(self, which_search):
        logger.info("Starting the method")
        self._which_search = which_search
        logger.info("Ending the method")

    def get_which_search(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._which_search

    def set_root_path(self, root_path):
        logger.info("Starting the method")
        self._root_path = root_path
        logger.info("Ending the method")

    def get_root_path(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._root_path

    def set_is_advance_search(self, is_advance_search):
        logger.info("Starting the method")
        self._is_advance_search = is_advance_search
        logger.info("Ending the method")

    def get_is_advance_search(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._is_advance_search

    def set_common_name(self, common_name):
        logger.info("Starting the method")
        self._common_name = common_name
        logger.info("Ending the method")

    def get_common_name(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._common_name

    def set_extension(self, extension):
        logger.info("Starting the method")
        self._extension = extension
        logger.info("Ending the method")

    def get_extension(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._extension

    def set_is_exact_common_name(self, is_exact_common_name):
        logger.info("Starting the method")
        self._is_exact_common_name = is_exact_common_name
        logger.info("Ending the method")

    def get_is_exact_common_name(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._is_exact_common_name

    def set_is_include_sub_folders(self, is_include_sub_folders):
        logger.info("Starting the method")
        self._is_include_sub_folders = is_include_sub_folders
        logger.info("Ending the method")

    def get_is_include_sub_folders(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._is_include_sub_folders

    def set_less_size(self, less_size):
        logger.info("Starting the method")
        self._less_size = less_size
        logger.info("Ending the method")

    def get_less_size(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._less_size

    def set_bigger_size(self, bigger_size):
        logger.info("Starting the method")
        self._bigger_size = bigger_size
        logger.info("Ending the method")

    def get_bigger_size(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._bigger_size

    def set_content_word(self, content_word):
        logger.info("Starting the method")
        self._content_word = content_word
        logger.info("Ending the method")

    def get_content_word(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._content_word

    def set_less_creation_date(self, less_creation_date):
        logger.info("Starting the method")
        self._less_creation_date = less_creation_date
        logger.info("Ending the method")

    def get_less_creation_date(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._less_creation_date

    def set_bigger_creation_date(self, bigger_creation_date):
        logger.info("Starting the method")
        self._bigger_creation_date = bigger_creation_date
        logger.info("Ending the method")

    def get_bigger_creation_date(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._bigger_creation_date

    def set_less_modification_date(self, less_modification_date):
        logger.info("Starting the method")
        self._less_modification_date = less_modification_date
        logger.info("Ending the method")

    def get_less_modification_date(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._less_modification_date

    def set_bigger_modification_date(self, bigger_modification_date):
        logger.info("Starting the method")
        self._bigger_modification_date = bigger_modification_date
        logger.info("Ending the method")

    def get_bigger_modification_date(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._bigger_modification_date

    def get_owner(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._owner

    def set_owner(self, owner):
        logger.info("Starting the method")
        self._owner = owner
        logger.info("Ending the method")
