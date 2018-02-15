import os
import datetime


class Asset(object):

    def __init__(self, path, is_file):
        self._path = path
        self._is_file = is_file
        self._size = os.path.getsize(path)
        attributes = os.stat(path)
        self._st_access_time = datetime.datetime.fromtimestamp(attributes[7])
        self._st_modification_time = datetime.datetime.fromtimestamp(attributes[8])
        self._st_creation_time = datetime.datetime.fromtimestamp(attributes[9])
        # supported only on unix
        self._st_uid_user_id = attributes[4]
        self._st_gid_group_id = attributes[5]

    def get_st_access_time(self):
        return self._st_access_time

    def get_st_modification_time(self):
        return self._st_modification_time

    def get_st_creation_time(self):
        return self._st_creation_time

    def get_st_uid_user_id(self):
        return self._st_uid_user_id

    def get_st_gid_group_id(self):
        return self._st_gid_group_id

    def get_path(self):
        return self._path

    def get_size(self):
        return self._size

    def get_is_file(self):
        return self._is_file


