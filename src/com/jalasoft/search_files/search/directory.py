from src.com.jalasoft.search_files.search.asset import Asset


class Directory(Asset):

    def __init__(self, path, dir_name, is_file):
        super().__init__(path, is_file)
        self.count_content = 0
        self.dir_name = dir_name

    def get_dir_name(self):
        return self.dir_name
