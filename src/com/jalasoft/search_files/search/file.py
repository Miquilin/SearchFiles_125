from src.com.jalasoft.search_files.search.asset import Asset
from src.com.jalasoft.search_files.utils.logging_config import logger


class File(Asset):
    """ Class File """

    def __init__(self, path, file_name, is_file):
        super().__init__(path, is_file)

        self._file_name, self._separator, self._extension = file_name.partition(".")

    def get_file_name(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._file_name

    def get_extension(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._extension

    def get_separator(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._separator
