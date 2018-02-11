import re
import bitmath
from src.com.jalasoft.search_files.utils.logging_config import logger


class SearchValidation(object):
    def __init__(self):
        pass

    def string1_exists_within_string2(self, string_1, string_2, flag):
        logger.info("Starting the method")
        case_sensitive = bool(flag)
        if case_sensitive is True:
            search_match = re.search(string_1, string_2)
            if search_match is None:
                boolean_contain = False
            else:
                boolean_contain = True
        else:
            search_match = re.search(string_1, string_2, re.IGNORECASE)
            if search_match is None:
                boolean_contain = False
            else:
                boolean_contain = True
        logger.info("The value return is: %s", boolean_contain)
        logger.info("Exit method")
        return boolean_contain

    def is_string1_equal_to_string2(self, string_1, string_2, flag):
        logger.info("Starting the method")
        case_sensitive = bool(flag)
        if case_sensitive is True:
            search_match = re.match(string_1, string_2)
            if search_match is None:
                boolean_contain = False
            else:
                boolean_contain = True
        else:
            search_match = re.match(string_1, string_2, re.IGNORECASE)
            if search_match is None:
                boolean_contain = False
            else:
                boolean_contain = True
        logger.info("The value return is: %s", boolean_contain)
        logger.info("Exit method")
        return boolean_contain

    def is_less_than_or_equal(self, bit_size, mega_bit_size):
        logger.info("Starting the method")
        num_bit = bitmath.Bit(bit_size)
        num_mega_bit = bitmath.Mib(mega_bit_size)
        if num_bit <= num_mega_bit:
            boolean_contain = True
        else:
            boolean_contain = False
        logger.info("The value return is: %s", boolean_contain)
        logger.info("Exit method")
        return boolean_contain

    def is_bigger_than_other(self, bit_size, mega_bit_size):
        # it is possible that the is_bigger_than_other() method is redundant
        logger.info("Starting the method")
        num_bit = bitmath.Bit(bit_size)
        num_mega_bit = bitmath.Mib(mega_bit_size)
        if num_bit < num_mega_bit:
            boolean_contain = True
        else:
            boolean_contain = False
        logger.info("The value return is: %s", boolean_contain)
        logger.info("Exit method")
        return boolean_contain
