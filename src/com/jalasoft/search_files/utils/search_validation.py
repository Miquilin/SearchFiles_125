import re
import bitmath
import sys
from src.com.jalasoft.search_files.utils.logging_config import logger


class SearchValidation(object):
    """
    Validations required by Search
    """
    def __init__(self):
        pass

    def string1_exists_within_string2(self, string_1, string_2, flag):
        """
        This method determines whether the string_1 exists within the string_2, besides doing this search with and
        without sensitive case(flag= True or False)

        :param string_1:
        :param string_2:
        :param flag:
        :return boolean_contain:
        """
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
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def is_string1_equal_to_string2(self, string_1, string_2, flag):
        """
        This method determines whether the string_1 is equals to the string_2, besides doing this search with and
        without sensitive case(flag= True or False)

        :param string_1:
        :param string_2:
        :param flag:
        :return boolean_contain:
        """
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
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def is_less_than_or_equal(self, bit_size, mega_bit_size):
        """
        This method returns True if bit_size is less than or equals to mega_bit_size otherwise return False

        :param bit_size:
        :param mega_bit_size:
        :return boolean_contain:
        """
        logger.info("Starting the method")
        num_bit = bitmath.Bit(bit_size)
        num_mega_bit = bitmath.Mib(mega_bit_size)
        if num_bit.to_MiB() <= num_mega_bit:
            boolean_contain = True
        else:
            boolean_contain = False
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def is_less_than_and_bigger_than_or_equal(self, bit_size, mega_bit_size_less, mega_bit_size_bigger):
        logger.info("Starting the method")
        num_bit = bitmath.Bit(bit_size)
        num_mega_bit_less = bitmath.Mib(mega_bit_size_less)
        num_mega_bit_bigger = bitmath.Mib(mega_bit_size_bigger)
        if num_mega_bit_less >= num_bit.to_MiB() >= num_mega_bit_bigger:
            boolean_contain = True
        else:
            boolean_contain = False
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain


    def is_bigger_than_other(self, bit_size, mega_bit_size):
        """
        This method returns True if bit_size is bigger than mega_bit_size otherwise return False

        :param bit_size:
        :param mega_bit_size:
        :return otherwise return False:
        """
        logger.info("Starting the method")
        num_bit = bitmath.Bit(bit_size)
        num_mega_bit = bitmath.Mib(mega_bit_size)
        if num_bit.to_MiB() > num_mega_bit:
            boolean_contain = True
        else:
            boolean_contain = False
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def is_windows(self):
        """
        this method returns True if the OS is Windows

        :return boolean_contain:
        """
        logger.info("Starting the method")
        operation_system = sys.platform
        search_match = re.search("win", operation_system)
        if search_match is None:
            boolean_contain = False
        else:
            boolean_contain = True
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def is_linux(self):
        """
        this method returns True if the OS is Linux

        :return boolean_contain:
        """
        logger.info("Starting the method")
        operation_system = sys.platform
        search_match = re.search("linux", operation_system)
        if search_match is None:
            boolean_contain = False
        else:
            boolean_contain = True
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain






