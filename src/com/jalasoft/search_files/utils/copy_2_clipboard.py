import pyperclip
import json
from src.com.jalasoft.search_files.utils.logging_config import logger


class Copy2ClipBoard(object):

    def __init__(self):
        logger.info("Starting the method")
        self.json_result = ""
        logger.info("Ending the method")

    def convert_dictionary_to_json(self, dictionary):
        logger.info("Starting the method")
        logger.debug("The dictionary to be converted is: %s", dictionary)
        json_dict = json.dumps(dictionary, ensure_ascii=False)
        logger.debug("The obtained json is: %s", json_dict)
        logger.info("Ending the method")
        return json_dict

    def copy_to_clip(self, dictionary):
        logger.info("Starting the method")
        logger.debug("calling to 'convert_dictionary_to_json' method")
        self.json_result = self.convert_dictionary_to_json(dictionary)
        pyperclip.copy(self.json_result)
        logger.debug("Data copied to clipboard is: %s", pyperclip.paste())
        logger.info("Ending the method")
