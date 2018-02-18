import os
import re
import datetime
from src.com.jalasoft.search_files.utils.logging_config import logger


class Validation(object):
    def __init__(self):
        pass

    def is_number(self, string_value):
        logger.info("Starting the method")
        boolean_contain = string_value.isdigit()
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def is_the_range(self, number, upper_limit, lower_limit):
        logger.info("Starting the method")
        number = int(number)
        if number >= lower_limit and number <= upper_limit:
            boolean_contain = True
        else:
            boolean_contain = False
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def attempt_maximum(self, attempts):
        logger.info("Starting the method")
        attempts = int(attempts)
        if attempts <= 5:
            boolean_contain = True
        else:
            boolean_contain = False
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def is_path_valid(self, directory):
        logger.info("Starting the method")
        directory = str(directory)
        boolean_contain = os.path.exists(directory)
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def has_valid_characters(self, string_value):
        logger.info("Starting the method")
        string_value = str(string_value)
        boolean_contain = string_value.isalnum()
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def is_blank(self, string_value):
        logger.info("Starting the method")
        string_value = str(string_value)
        if string_value and string_value.strip():
            boolean_contain = False
        else:
            boolean_contain = True
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def is_valid_date(self, str_date):
        logger.info("Starting the method")
        regex = re.compile("(\d{1,4})-(\d{1,2})-(\d{1,2}) (\d{1,2}):(\d{1,2}):(\d{1,2})")
        match = regex.match(str_date)
        if match:
            year, month, day, hour, minute, seconds = match.groups()
            if len(year) == 4:
                date_format = "%Y-%m-%d %H:%S:%M"
            else:
                date_format = "%y-%m-%d %H:%S:%M"
            try:
                datetime.datetime.strptime(str_date, date_format)
            except ValueError:
                logger.debug("The value returned is: %s", False)
                logger.info("Ending the method")
                return False
            boolean_contain = True
        else:
            boolean_contain = False
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain
    