from src.com.jalasoft.search_files.menu.cli_menu import CLIMenu
from src.com.jalasoft.search_files.utils.menu_validation import Validation
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.search.directory import Directory
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria
from src.com.jalasoft.search_files.utils.logging_config import logger
import sys


class CLIMenuBasicFlow(object):
    """
    CLIMenuBasicFlow class contains the needed validations and functions for Basic Search
    """

    def __init__(self):
        """
        This method is the constructor of the class
        :param None
        :return None
        """
        logger.info("Starting the method")
        self.cli_menu = CLIMenu()
        self.validator = Validation()
        self.files = []
        self.folders = []
        logger.info("Ending the method")

    def show_menu(self, option):
        """
        show_menu method permits to load a specific menu according to the option provided and gets the option selected
        by the user.
        :param option:
        :return: value
        """
        logger.info("Starting the method")
        if option == 0:
            logger.debug("Option selected: %s. Ending the application.", option)
            sys.exit()
        elif option == 1:
            logger.debug("Option selected: %s. Loading the 'Main' menu.", option)
            value = self.cli_menu.main_menu()
        elif option == 2:
            logger.debug("Option selected: %s. Loading the 'Basic - Search For' menu.", option)
            value = self.cli_menu.basic_search_for_menu()
        elif option == 3:
            logger.debug("Option selected: %s. Loading the 'Basic - Search For' criteria.", option)
            value = self.cli_menu.basic_search_for_criteria()
        elif option == 4:
            logger.debug("Option selected: %s. Loading the 'Basic - Search In' criteria.", option)
            value = self.cli_menu.basic_search_in_path()
        elif option == 5:
            logger.debug("Option selected: %s. Loading the 'Basic - Summary' menu.", option)
            value = self.cli_menu.basic_summary_menu()
        elif option == 6:
            logger.debug("Option selected: %s. Loading the 'Results' menu.", option)
            value = self.cli_menu.results_menu()
        logger.info("Ending the method")
        return value

    def get_results_dictionary(self):
        """
        This method permits to get the results_data dictionary
        :return: results_dictionary
        """
        logger.info("Starting the method")
        results_dictionary = self.cli_menu.results_data
        logger.debug("The value returned is: %s", results_dictionary)
        logger.info("Ending the method")
        return results_dictionary

    def main_menu_validation(self, option):
        """
        This method does the validations on main menu
        :param option:
        :return: boolean_contain
        """
        logger.info("Starting the method")
        boolean_contain = self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.basic_search_for_menu_items) - 1, 1) and self.validator.has_valid_characters(option)
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def basic_search_for_option_validation(self, option):
        """
        This method does the validations on Search for menu
        :param option:
        :return: boolean_contain
        """
        logger.info("Starting the method")
        boolean_contain = self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.basic_search_for_menu_items) - 1, 1) and self.validator.has_valid_characters(option)
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def basic_search_for_criteria_validation(self, option):
        """
        This method does the validations on Search for criteria menu
        :param option:
        :return: boolean_contain
        """
        logger.info("Starting the method")
        boolean_contain = self.validator.has_valid_characters(option)
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def basic_search_in_path_validation(self, option):
        """
        This method does the validations on Search in criteria menu
        :param option:
        :return: boolean_contain
        """
        logger.info("Starting the method")
        boolean_contain = self.validator.is_path_valid(option)
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def basic_summary_option_validation(self, option):
        """
        This method does the validations on summary menu
        :param option:
        :return: boolean_contain
        """
        logger.info("Starting the method")
        boolean_contain = self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.summary_items) - 1, 1) and self.validator.has_valid_characters(option)
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def basic_result_option_validation(self, option):
        """
        This method does the validations on results menu
        :param option:
        :return: boolean_contain
        """
        logger.info("Starting the method")
        boolean_contain = self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.result_items) - 1, 1) and self.validator.has_valid_characters(option)
        logger.debug("The value returned is: %s", boolean_contain)
        logger.info("Ending the method")
        return boolean_contain

    def get_summary_data_items(self, key):
        """
        This method permits to get a value from get_basic_summary_data_items dictionary
        :param key:
        :return: summary_data_item
        """
        logger.info("Starting the method")
        summary_data_item = self.cli_menu.get_basic_summary_data_items(key)
        logger.debug("The value returned is: %s", summary_data_item)
        logger.info("Ending the method")
        return summary_data_item

    def set_summary_data_items(self, key, value):
        """
        This method permits to set/update a value in set_basic_summary_data_items dictionary
        :param key:
        :param value:
        :return: None
        """
        logger.info("Starting the method")
        self.cli_menu.set_basic_summary_data_items(key, value)
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("Ending the method")

    def get_search_for_menu_item(self, key):
        """
        This method permits to get a value from get_basic_search_for_menu_items dictionary
        :param key:
        :return: search_for_menu_item
        """
        logger.info("Starting the method")
        search_for_menu_item = self.cli_menu.get_basic_search_for_menu_items(key)
        logger.debug("The value returned is: %s", search_for_menu_item)
        logger.info("Ending the method")
        return search_for_menu_item

    def set_search_for_menu_item(self, key, value):
        """
        This method permits to set/update a value in set_basic_search_for_menu_items dictionary
        :param key:
        :param value:
        :return: None
        """
        logger.info("Starting the method")
        self.cli_menu.set_basic_search_for_menu_items(key, value)
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("Ending the method")

    def start_search_process(self):
        """
        This method configures the search_criteria parameters and start the search process
        :return: None
        """
        logger.info("Starting the method")
        self.files = []
        self.folders = []
        # Basic Search - Doing the search by Name
        if self.cli_menu.get_basic_summary_data_items("search_for_option") == "Name":
            logger.debug("Executing a Search process for Name")
            path = self.cli_menu.get_basic_summary_data_items("search_in_path")
            criteria = self.cli_menu.get_basic_summary_data_items("search_for_criteria")
            search_criteria = SearchCriteria()
            search_criteria.set_is_advance_search(False)
            search_criteria.set_root_path(path)
            search_criteria.set_common_name(criteria)
            search_criteria.set_is_include_sub_folders(True)
            search = Search()
            logger.debug("Starting the search")
            search_result = search.start_a_search(search_criteria)
            logger.debug("The search result returned is: %s", search_result)
            self.save_search_result(search_result)

        # Basic Search - Doing the search by Extension
        if self.cli_menu.get_basic_summary_data_items("search_for_option") == "Extension":
            logger.debug("Executing a Search process for Extension")
            path = self.cli_menu.get_basic_summary_data_items("search_in_path")
            criteria = self.cli_menu.get_basic_summary_data_items("search_for_criteria")
            search_criteria = SearchCriteria()
            search_criteria.set_is_advance_search(False)
            search_criteria.set_root_path(path)
            search_criteria.set_extension(criteria)
            search_criteria.set_is_include_sub_folders(True)
            search = Search()
            logger.debug("Starting the search")
            search_result = search.start_a_search(search_criteria)
            logger.debug("The search result returned is: %s", search_result)
            self.save_search_result(search_result)
            logger.info("Ending the method")

    def save_search_result(self, search_result):
        """
        This method saves the search result into the set_results_data dictionary
        :param search_result:
        :return: None
        """
        logger.info("Starting the method")
        logger.debug("Iterating the search result list")
        for sr in search_result:
            if isinstance(sr, File):
                self.files.append(sr.get_path())
            if isinstance(sr, Directory):
                self.folders.append(sr.get_path())
        logger.debug("The list of folders obtained is: %s", self.folders)
        logger.debug("The list of files obtained is: %s", self.files)
        self.cli_menu.set_results_data("number_files", len(self.files))
        self.cli_menu.set_results_data("number_folders", len(self.folders))
        self.cli_menu.set_results_data("files", self.files)
        self.cli_menu.set_results_data("folders", self.folders)
        logger.info("Ending the method")
