from src.com.jalasoft.search_files.menu.cli_menu import CLIMenu
from src.com.jalasoft.search_files.utils.validation import Validation
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.search.asset import File, Directory
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria
import sys


class CLIMenuAdvancedFlow(object):

    def __init__(self):
        self.cli_menu = CLIMenu()
        self.validator = Validation()
        #self.search = Search()
        self.files = []
        self.folders = []

    def show_menu(self, option):
        if option == 0:
            sys.exit()
        elif option == 1:
            value = self.cli_menu.main_menu()
        elif option == 2:
            value = self.cli_menu.advanced_search_for_name_menu()
        elif option == 3:
            value = self.cli_menu.advanced_search_for_name_criteria()
        elif option == 4:
            value = self.cli_menu.advanced_search_for_extension_criteria()
        elif option == 5:
            value = self.cli_menu.advanced_search_for_size_menu()
        elif option == 6:
            value = self.cli_menu.advanced_search_for_size_criteria()
        elif option == 7:
            value = self.cli_menu.advanced_search_for_owner_criteria()
        elif option == 8:
            value = self.cli_menu.advanced_search_for_date_menu()
        elif option == 9:
            value = self.cli_menu.advanced_search_for_date_criteria()
        elif option == 10:
            value = self.cli_menu.advanced_search_for_content_criteria()
        elif option == 11:
            value = self.cli_menu.advanced_search_in_menu()
        elif option == 12:
            value = self.cli_menu.advanced_search_in_criteria_path()
        elif option == 13:
            value = self.cli_menu.advanced_summary_menu()
        elif option == 14:
            value = self.cli_menu.results_menu()
        return value

    def main_menu_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.main_menu_items) - 1, 1) and self.validator.has_valid_characters(option):
            return True
        else:
            return False

    def get_results_dictionary(self):
        return self.cli_menu.results_data

    def advanced_search_for_name_menu_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.advanced_search_for_name_items) - 1, 1):
            return True
        else:
            return False

    def advanced_search_for_name_criteria_validation(self, option):
        return True
        #if self.validator.has_valid_characters(option):
        #    return True
        #else:
        #    return False

    def advanced_search_for_extension_criteria_validation(self, option):
        return True
        #if self.validator.has_valid_characters(option):
        #    return True
        #else:
        #    return False

    def advanced_search_for_size_menu_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.advanced_search_for_size_items) - 1, 1):
            return True
        else:
            return False

    def advanced_search_for_size_criteria_validation(self, option):
        return True
        #if self.validator.has_valid_characters(option):
        #    return True
        #else:
        #    return False

    def advanced_search_for_owner_criteria_validation(self, option):
        return True
        #if self.validator.has_valid_characters(option):
        #    return True
        #else:
        #    return False

    def advanced_search_for_date_menu_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.advanced_search_for_date_items) - 1, 1):
            return True
        else:
            return False

    def advanced_search_for_date_criteria_validation(self, option):
        return True
        #if self.validator.has_valid_characters(option):
        #    return True
        #else:
        #    return False

    def advanced_search_for_content_criteria_validation(self, option):
        return True
        #if self.validator.has_valid_characters(option):
        #    return True
        #else:
        #    return False

    def advanced_search_in_menu_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.advanced_search_in_items) - 1, 1):
            return True
        else:
            return False

    def advanced_search_in_path_criteria_validation(self, option):
        if self.validator.is_path_valid(option):
            return True
        else:
            return False

    def advanced_summary_menu_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.summary_items) - 1, 1):
            return True
        else:
            return False

    def advanced_result_menu_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.result_items) - 1, 1):
            return True
        else:
            return False

    def get_advanced_summary_data_items(self, key):
        return self.cli_menu.get_advanced_summary_data_items(key)

    def set_advanced_summary_data_items(self, key, value):
        self.cli_menu.set_advanced_summary_data_items(key, value)

    def get_advanced_search_for_name_menu_items(self, key):
        return self.cli_menu.get_advanced_search_for_name_items(key)

    def set_advanced_search_for_name_menu_items(self, key, value):
        self.cli_menu.set_advanced_search_for_name_items(key, value)

    def get_advanced_search_for_size_menu_items(self, key):
        return self.cli_menu.get_advanced_search_for_size_items(key)

    def set_advanced_search_for_size_menu_items(self, key, value):
        self.cli_menu.set_advanced_search_for_size_items(key, value)

    def get_advanced_search_for_date_menu_items(self, key):
        return self.cli_menu.get_advanced_search_for_date_items(key)

    def set_advanced_search_for_date_menu_items(self, key, value):
        self.cli_menu.set_advanced_search_for_date_items(key, value)

    def get_advanced_search_in_items(self, key):
        return self.cli_menu.get_advanced_search_in_items(key)

    def set_advanced_search_in_items(self, key, value):
        self.cli_menu.set_advanced_search_in_items(key, value)

    def start_search_process(self):
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
        search_result = search.start_a_search(search_criteria)
        self.save_search_result(search_result)

    def save_search_result(self, search_result):
            for sr in search_result:
                if isinstance(sr, File):
                    self.files.append(sr.get_path())
                if isinstance(sr, Directory):
                    self.folders.append(sr.get_path())
            self.cli_menu.set_results_data("number_files", len(self.files))
            self.cli_menu.set_results_data("number_folders", len(self.folders))
            self.cli_menu.set_results_data("files", self.files)
            self.cli_menu.set_results_data("folders", self.folders)
