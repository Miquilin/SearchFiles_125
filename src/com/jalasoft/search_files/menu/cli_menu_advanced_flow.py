from src.com.jalasoft.search_files.menu.cli_menu import CLIMenu
from src.com.jalasoft.search_files.utils.logging_config import logger
from src.com.jalasoft.search_files.utils.menu_validation import Validation
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.search.directory import Directory
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria
import sys


class CLIMenuAdvancedFlow(object):

    def __init__(self):
        logger.info("Starting the method")
        self.cli_menu = CLIMenu()
        self.validator = Validation()
        self.files = []
        self.folders = []
        logger.info("Ending the method")

    def show_menu(self, option):
        logger.info("Starting the method")
        if option == 0:
            logger.debug("Option selected: %s. Ending the application.", option)
            sys.exit()
        elif option == 1:
            logger.debug("Option selected: %s. Loading the 'Main' menu.", option)
            value = self.cli_menu.main_menu()
        elif option == 2:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search For Name' menu.", option)
            value = self.cli_menu.advanced_search_for_name_menu()
        elif option == 3:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search For Name Criteria'.", option)
            value = self.cli_menu.advanced_search_for_name_criteria()
        elif option == 4:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search For Extension Criteria'.", option)
            value = self.cli_menu.advanced_search_for_extension_criteria()
        elif option == 5:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search For Size' menu.", option)
            value = self.cli_menu.advanced_search_for_size_menu()
        elif option == 6:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search For Size Criteria'.", option)
            value = self.cli_menu.advanced_search_for_size_criteria()
        elif option == 7:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search For Owner Criteria'.", option)
            value = self.cli_menu.advanced_search_for_owner_criteria()
        elif option == 8:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search For Date' menu.", option)
            value = self.cli_menu.advanced_search_for_date_menu()
        elif option == 9:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search For Date Criteria'.", option)
            value = self.cli_menu.advanced_search_for_date_criteria()
        elif option == 10:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search For Content Criteria'.", option)
            value = self.cli_menu.advanced_search_for_content_criteria()
        elif option == 11:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search In' menu.", option)
            value = self.cli_menu.advanced_search_in_menu()
        elif option == 12:
            logger.debug("Option selected: %s. Loading the 'Advanced - Search In Criteria'.", option)
            value = self.cli_menu.advanced_search_in_criteria_path()
        elif option == 13:
            logger.debug("Option selected: %s. Loading the 'Advanced - Summary' menu.", option)
            value = self.cli_menu.advanced_summary_menu()
        elif option == 14:
            logger.debug("Option selected: %s. Loading the 'Results' menu.", option)
            value = self.cli_menu.results_menu()
        logger.info("Ending the method")
        return value

    def main_menu_validation(self, option):
        logger.info("Starting the method")
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.main_menu_items) - 1, 1) and self.validator.has_valid_characters(option):
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return True
        else:
            logger.debug("The value returned is: %s", False)
            logger.info("Ending the method")
            return False

    def get_results_dictionary(self):
        logger.info("Starting the method")
        result_dictionary = self.cli_menu.results_data
        logger.debug("The dictionary returned is: %s", result_dictionary)
        logger.info("Ending the method")
        return result_dictionary

    def advanced_search_for_name_menu_validation(self, option):
        logger.info("Starting the method")
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.advanced_search_for_name_items) - 1, 1):
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return True
        else:
            logger.debug("The value returned is: %s", False)
            logger.info("Ending the method")
            return False

    def advanced_search_for_name_criteria_validation(self, option):
        logger.info("Starting the method")
        return True
        # if self.validator.has_valid_characters(option):
        #     logger.debug("The value returned is: %s", True)
        #     logger.info("Ending the method")
        #     return True
        # else:
        #     logger.debug("The value returned is: %s", False)
        #     logger.info("Ending the method")
        #     return False

    def advanced_search_for_extension_criteria_validation(self, option):
        logger.info("Starting the method")
        return True
        # if self.validator.has_valid_characters(option):
        #     logger.debug("The value returned is: %s", True)
        #     logger.info("Ending the method")
        #     return True
        # else:
        #     logger.debug("The value returned is: %s", False)
        #     logger.info("Ending the method")
        #     return False

    def advanced_search_for_size_menu_validation(self, option):
        logger.info("Starting the method")
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.advanced_search_for_size_items) - 1, 1):
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return True
        else:
            logger.debug("The value returned is: %s", False)
            logger.info("Ending the method")
            return False

    def advanced_search_for_size_criteria_validation(self, option):
        logger.info("Starting the method")
        return True
        # if self.validator.has_valid_characters(option):
        #     logger.debug("The value returned is: %s", True)
        #     logger.info("Ending the method")
        #     return True
        # else:
        #     logger.debug("The value returned is: %s", False)
        #     logger.info("Ending the method")
        #     return False

    def advanced_search_for_owner_criteria_validation(self, option):
        logger.info("Starting the method")
        return True
        # if self.validator.has_valid_characters(option):
        #     logger.debug("The value returned is: %s", True)
        #     logger.info("Ending the method")
        #     return True
        # else:
        #     logger.debug("The value returned is: %s", False)
        #     logger.info("Ending the method")
        #     return False

    def advanced_search_for_date_menu_validation(self, option):
        logger.info("Starting the method")
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.advanced_search_for_date_items) - 1, 1):
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return True
        else:
            logger.debug("The value returned is: %s", False)
            logger.info("Ending the method")
            return False

    def advanced_search_for_date_criteria_validation(self, option):
        logger.info("Starting the method")
        return True
        # if self.validator.has_valid_characters(option):
        #     logger.debug("The value returned is: %s", True)
        #     logger.info("Ending the method")
        #     return True
        # else:
        #     logger.debug("The value returned is: %s", False)
        #     logger.info("Ending the method")
        #     return False

    def advanced_search_for_content_criteria_validation(self, option):
        logger.info("Starting the method")
        return True
        # if self.validator.has_valid_characters(option):
        #     logger.debug("The value returned is: %s", True)
        #     logger.info("Ending the method")
        #     return True
        # else:
        #     logger.debug("The value returned is: %s", False)
        #     logger.info("Ending the method")
        #     return False

    def advanced_search_in_menu_validation(self, option):
        logger.info("Starting the method")
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.advanced_search_in_items) - 1, 1):
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return True
        else:
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return False

    def advanced_search_in_path_criteria_validation(self, option):
        logger.info("Starting the method")
        if self.validator.is_path_valid(option):
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return True
        else:
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return False

    def advanced_summary_menu_validation(self, option):
        logger.info("Starting the method")
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.summary_items) - 1, 1):
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return True
        else:
            logger.debug("The value returned is: %s", False)
            logger.info("Ending the method")
            return False

    def advanced_result_menu_validation(self, option):
        logger.info("Starting the method")
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.result_items) - 1, 1):
            logger.debug("The value returned is: %s", True)
            logger.info("Ending the method")
            return True
        else:
            logger.debug("The value returned is: %s", False)
            logger.info("Ending the method")
            return False

    def get_advanced_summary_data_items(self, key):
        logger.info("Starting the method")
        summary_data_item = self.cli_menu.get_advanced_summary_data_items(key)
        logger.debug("The value returned is: %s", summary_data_item)
        logger.info("Ending the method")
        return summary_data_item

    def set_advanced_summary_data_items(self, key, value):
        logger.info("Starting the method")
        self.cli_menu.set_advanced_summary_data_items(key, value)
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("Ending the method")

    def get_advanced_search_for_name_menu_items(self, key):
        logger.info("Starting the method")
        search_for_menu_item = self.cli_menu.get_advanced_search_for_name_items(key)
        logger.debug("The value returned is: %s", search_for_menu_item)
        logger.info("Ending the method")
        return search_for_menu_item

    def set_advanced_search_for_name_menu_items(self, key, value):
        logger.info("Starting the method")
        self.cli_menu.set_advanced_search_for_name_items(key, value)
        logger.info("Ending the method")

    def get_advanced_search_for_size_menu_items(self, key):
        logger.info("Starting the method")
        search_for_size_item = self.cli_menu.get_advanced_search_for_size_items(key)
        logger.debug("The value returned is: %s", search_for_size_item)
        logger.info("Ending the method")
        return search_for_size_item

    def set_advanced_search_for_size_menu_items(self, key, value):
        logger.info("Starting the method")
        self.cli_menu.set_advanced_search_for_size_items(key, value)
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("Ending the method")

    def get_advanced_search_for_date_menu_items(self, key):
        logger.info("Starting the method")
        search_for_date_item = self.cli_menu.get_advanced_search_for_date_items(key)
        logger.debug("The value returned is: %s", search_for_date_item)
        logger.info("Ending the method")
        return search_for_date_item

    def set_advanced_search_for_date_menu_items(self, key, value):
        logger.info("Starting the method")
        self.cli_menu.set_advanced_search_for_date_items(key, value)
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("Ending the method")

    def get_advanced_search_in_items(self, key):
        logger.info("Starting the method")
        search_in_item = self.cli_menu.get_advanced_search_in_items(key)
        logger.debug("The value returned is: %s", search_in_item)
        logger.info("Ending the method")
        return search_in_item

    def set_advanced_search_in_items(self, key, value):
        logger.info("Starting the method")
        self.cli_menu.set_advanced_search_in_items(key, value)
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("Ending the method")

    def start_search_process(self):
        logger.info("Starting the method")
        self.files = []
        self.folders = []
        search_for_name = self.cli_menu.get_advanced_summary_data_items("search_in_criteria")
        search_for_name_criteria = self.cli_menu.get_advanced_summary_data_items("search_for_name_criteria")
        search_for_extension_criteria = self.cli_menu.get_advanced_summary_data_items("search_for_extension_criteria")
        search_for_size = self.cli_menu.get_advanced_summary_data_items("search_for_size")
        search_for_size_criteria = self.cli_menu.get_advanced_summary_data_items("search_for_size_criteria")
        search_for_owner_criteria = self.cli_menu.get_advanced_summary_data_items("search_for_owner_criteria")
        search_for_date = self.cli_menu.get_advanced_summary_data_items("search_for_date")
        search_for_date_criteria = self.cli_menu.get_advanced_summary_data_items("search_for_date_criteria")
        search_for_content_criteria = self.cli_menu.get_advanced_summary_data_items("search_for_content_criteria")
        search_in = self.cli_menu.get_advanced_summary_data_items("search_in")
        search_in_criteria = self.cli_menu.get_advanced_summary_data_items("search_in_criteria")

        search_criteria = SearchCriteria()
        logger.debug("Starting to configure the search criteria")
        search_criteria.set_root_path(search_in_criteria)
        search_criteria.set_is_advance_search(True)
        search_criteria.set_common_name(search_for_name_criteria)
        search_criteria.set_extension(search_for_extension_criteria)
        search_criteria.set_content_word(search_for_content_criteria)
        if search_in == "All [including sub-folders]":
            search_criteria.set_is_include_sub_folders(True)
        elif search_in == "Current Folder":
            search_criteria.set_is_include_sub_folders(False)
        elif search_for_name == "Name - Contains text":
            search_criteria.set_is_exact_common_name(False)
        elif search_for_name == "Name - Exact Text":
            search_criteria.set_is_exact_common_name(True)
        elif search_for_size == "Major than 'X' MB.":
            search_criteria.set_bigger_size(int(search_for_size_criteria))
        elif search_for_size == "Minor than 'X' MB.":
            search_criteria.set_less_size(int(search_for_size_criteria))
        search = Search()
        logger.debug("Starting the Search")
        search_result = search.start_a_search(search_criteria)
        logger.debug("The search result returned is: %s", search_result)
        self.save_search_result(search_result)
        logger.info("Ending the method")

    def save_search_result(self, search_result):
        logger.info("Starting the method")
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
