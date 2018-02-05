import re
import bitmath


class SearchValidation(object):
    def __init__(self):
        pass

    def string1_exists_within_string2(self, string_1, string_2, flag):
        case_sensitive = bool(flag)
        if case_sensitive is True:
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
        case_sensitive = bool(flag)
        if case_sensitive is True:
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

    def is_less_than_or_equal(self, bit_size, mega_bit_size):
        num_bit = bitmath.Bit(bit_size)
        num_mega_bit = bitmath.Mb(mega_bit_size)
        if num_bit <= num_mega_bit:
            return True
        else:
            return False

    def is_bigger_than_other(self, bit_size, mega_bit_size):
        # it is possible that the is_bigger_than_other() method is redundant
        num_bit = bitmath.Bit(bit_size)
        num_mega_bit = bitmath.Mb(mega_bit_size)
        if num_bit < num_mega_bit:
            return True
        else:
            return False
