import unittest
import os
import sys
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria
if sys.platform.startswith("win"):
    import win32security


PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

class SearchByOwnerTest(unittest.TestCase):
    """ Test to verify that can list all directories"""

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_advance_search_by_owner_that_returns_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(True)
        security_description = win32security.GetFileSecurity(PATH,
                                           win32security.OWNER_SECURITY_INFORMATION)
        sid = security_description.GetSecurityDescriptorOwner()
        owner_name_root_path = win32security.LookupAccountSid(None, sid)[0]
        search_criteria.set_owner(owner_name_root_path)
        search_test = Search().start_a_search(search_criteria)
        for item in search_test:
            sd = win32security.GetFileSecurity(item.get_path(),
                                               win32security.OWNER_SECURITY_INFORMATION)
            sid = sd.GetSecurityDescriptorOwner()
            owner_name = win32security.LookupAccountSid(None, sid)[0]
            self.assertEqual(owner_name, item.get_owner())

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_advance_search_by_owner_that_does_not_return_coincidences(self):
        search_criteria = SearchCriteria()
        search_criteria.set_is_advance_search(True)
        search_criteria.set_root_path(PATH)
        search_criteria.set_is_include_sub_folders(True)
        owner_name_root_path = "non owner"
        search_criteria.set_owner(owner_name_root_path)
        search_test = Search().start_a_search(search_criteria)
        for item in search_test:
            self.assertEqual("", item.get_owner())
