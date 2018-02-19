import os
import datetime
from src.com.jalasoft.search_files.utils.logging_config import logger


class Asset(object):
    """ Class Asset """

    def __init__(self, path, is_file):
        self._path = path
        self._is_file = is_file
        self._size = os.path.getsize(path)
        attributes = os.stat(path)
        self._st_modification_time = datetime.datetime.now()
        if attributes[8] != 0:
            self._st_modification_time = datetime.datetime.fromtimestamp(attributes[8])
        self._st_modification_time = datetime.datetime.now()
        if attributes[9] != 0:
            self._st_creation_time = datetime.datetime.fromtimestamp(attributes[9])
        # supported only on unix
        self._st_uid_user_id = attributes[4]
        self._st_gid_group_id = attributes[5]
        self._owner = ""

    def get_st_modification_time(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._st_modification_time

    def get_st_creation_time(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._st_creation_time

    def get_st_uid_user_id(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._st_uid_user_id

    def get_st_gid_group_id(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._st_gid_group_id

    def get_path(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._path

    def get_size(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._size

    def get_is_file(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._is_file

    def get_owner(self):
        logger.info("Starting the method")
        logger.info("Ending the method")
        return self._owner

    def set_owner(self, owner):
        logger.info("Starting the method")
        self._owner = owner
        logger.info("Ending the method")
