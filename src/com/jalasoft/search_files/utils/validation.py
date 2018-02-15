import os
from src.com.jalasoft.search_files.utils.logging_config import logger

class Validation(object):
    def __init__(self):
        pass

    def is_number(self, cadena):
        logger.info("Starting the method")
        boolean_contain = cadena.isdigit()
        logger.info("The value returned is: %s", boolean_contain)
        logger.info("Exit method")
        return boolean_contain

    def is_the_range(self, number, upper_limit, lower_limit):
        logger.info("Starting the method")
        number = int(number)
        if number >= lower_limit and number <= upper_limit:
            boolean_contain = True
        else:
            boolean_contain = False
        logger.info("The value returned is: %s", boolean_contain)
        logger.info("Exit method")
        return boolean_contain

    def attempt_maximum(self, intentos):
        logger.info("Starting the method")
        intentos = int(intentos)
        if intentos <= 5:
            boolean_contain = True
        else:
            boolean_contain = False
        logger.info("The value returned is: %s", boolean_contain)
        logger.info("Exit method")
        return boolean_contain

    def is_path_valid(self, directory):
        logger.info("Starting the method")
        directory = str(directory)
        boolean_contain = os.path.exists(directory)
        logger.info("The value returned is: %s", boolean_contain)
        logger.info("Exit method")
        return boolean_contain

    def has_valid_characters(self, cadena):
        logger.info("Starting the method")
        cadena = str(cadena)
        boolean_contain = cadena.isalnum()
        logger.info("The value returned is: %s", boolean_contain)
        logger.info("Exit method")
        return boolean_contain






