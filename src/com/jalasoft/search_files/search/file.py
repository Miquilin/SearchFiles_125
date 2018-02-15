from src.com.jalasoft.search_files.search.asset import Asset


class File(Asset):

    def __init__(self, path, file_name, is_file):
        super().__init__(path, is_file)

        self._file_name, self._separator, self._extension = file_name.partition(".")

    def get_file_name(self):
        return self._file_name

    def get_extension(self):
        return self._extension

    def get_separator(self):
        return self._separator
