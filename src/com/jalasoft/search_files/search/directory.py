from src.com.jalasoft.search_files.search.asset import Asset
from src.com.jalasoft.search_files.utils.logging_config import logger


class Directory(Asset):
    """ Class Directory """

    def __init__(self, path, dir_name, is_file):
        super().__init__(path, is_file)
        self.count_content = 0
        self.dir_name = dir_name

    def get_dir_name(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self.dir_name
