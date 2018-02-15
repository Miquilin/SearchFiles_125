

class SearchCriteria(object):

    def __init__(self):
        """
        initial data by default
                                Args:
                                which_search (int): It can contains three values:
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
        self._less_creation_date = None
        self._bigger_creation_date = None
        self._less_modification_date = None
        self._bigger_modification_date = None

    def set_which_search(self, which_search):
        self._which_search = which_search

    def get_which_search(self):
        return self._which_search

    def set_root_path(self, root_path):
        self._root_path = root_path

    def get_root_path(self):
        return self._root_path

    def set_is_advance_search(self, is_advance_search):
        self._is_advance_search = is_advance_search

    def get_is_advance_search(self):
        return self._is_advance_search

    def set_common_name(self, common_name):
        self._common_name = common_name

    def get_common_name(self):
        return self._common_name

    def set_extension(self, extension):
        self._extension = extension

    def get_extension(self):
        return self._extension

    def set_is_exact_common_name(self, is_exact_common_name):
        self._is_exact_common_name = is_exact_common_name

    def get_is_exact_common_name(self):
        return self._is_exact_common_name

    def set_is_include_sub_folders(self, is_include_sub_folders):
        self._is_include_sub_folders = is_include_sub_folders

    def get_is_include_sub_folders(self):
        return self._is_include_sub_folders

    def set_less_size(self, less_size):
        self._less_size = less_size

    def get_less_size(self):
        return self._less_size

    def set_bigger_size(self, bigger_size):
        self._bigger_size = bigger_size

    def get_bigger_size(self):
        return self._bigger_size

    def set_content_word(self, content_word):
        self._content_word = content_word

    def get_content_word(self):
        return self._content_word

    def set_less_creation_date(self, less_creation_date):
        self._less_creation_date = less_creation_date

    def get_less_creation_date(self):
        return self._less_creation_date

    def set_bigger_creation_date(self, bigger_creation_date):
        self._bigger_creation_date = bigger_creation_date

    def get_bigger_creation_date(self):
        return self._bigger_creation_date

    def set_less_modification_date(self, less_modification_date):
        self._less_modification_date = less_modification_date

    def get_less_modification_date(self):
        return self._less_modification_date

    def set_bigger_modification_date(self, bigger_modification_date):
        self._bigger_modification_date = bigger_modification_date

    def get_bigger_modification_date(self):
        return self._bigger_modification_date

