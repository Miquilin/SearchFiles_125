import re


class SearchValidation(object):
    def __init__(self):
        pass

    def the_string1_exists_within_the_string2(self, string_1, string_2, flag):
        case_sensitive = int(flag)
        if case_sensitive == 1:
            search_match = re.search(string_1, string_2, re.IGNORECASE)
            if search_match is None:
                return False
            else:
                return True
        else:
            search_match = re.search(string_1, string_2)
            if search_match is None:
                return False
            else:
                return True

    def string1_equal_to_string2(self, string_1, string_2, flag):
        case_sensitive = int(flag)
        if case_sensitive == 1:
            search_match = re.match(string_1, string_2, re.IGNORECASE)
            if search_match is None:
                return False
            else:
                return True
        else:
            search_match = re.match(string_1, string_2)
            if search_match is None:
                return False
            else:
                return True