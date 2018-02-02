import os


class Asset(object):

    def __init__(self, path, is_file):
        self._path = path
        self._is_file = is_file
        self._size = os.path.getsize(path)

    def get_path(self):
        return self._path

    def get_size(self):
        return self._size

    def get_is_file(self):
        return self._is_file


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

class Directory(Asset):

    def __init__(self, path, dir_name, is_file):
        super().__init__(path, is_file)
        self.count_content = 0
        self.dir_name = dir_name

    def get_dir_name(self):
        return self.dir_name
