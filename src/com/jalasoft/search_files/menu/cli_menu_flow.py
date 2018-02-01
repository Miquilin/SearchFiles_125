from src.com.jalasoft.search_files.menu.cli_menu import CLIMenu
from src.com.jalasoft.search_files.utils.validation import Validation
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.search.asset import File, Directory
import sys


class CLIMenuFlow(object):

    def __init__(self):
        self.cli_menu = CLIMenu()
        self.validator = Validation()
        self.search = Search()
        self.files = []
        self.folders = []

    def show_menu(self, option):
        if option == 0:
            sys.exit()
        elif option == 1:
            self.cli_menu.set_results_data("number_files", "0")
            self.cli_menu.set_results_data("number_folders", "0")
            self.cli_menu.set_results_data("files", [])
            self.cli_menu.set_results_data("folders", [])
            print(self.cli_menu.results_data)
            value = self.cli_menu.search_for_menu()
        elif option == 2:
            value = self.cli_menu.search_for_criteria()
        elif option == 3:
            value = self.cli_menu.search_in_menu()
        elif option == 4:
            value = self.cli_menu.search_in_path()
        elif option == 5:
            value = self.cli_menu.summary_menu()
        elif option == 6:
            value = self.cli_menu.results_menu()
        return value

    def search_for_option_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.search_for_menu_items) - 1, 1) and self.validator.has_valid_characters(option):
            return True
        else:
            return False

    def search_for_criteria_validation(self, option):
        if self.validator.has_valid_characters(option):
            return True
        else:
            return False

    def search_in_option_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.search_in_items) - 1, 1) and self.validator.has_valid_characters(option):
            return True
        else:
            return False

    def search_in_path_validation(self, option):
        if self.validator.is_path_valid(option):
            return True
        else:
            return False

    def summary_option_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.summary_items) - 1, 1) and self.validator.has_valid_characters(option):
            return True
        else:
            return False

    def result_option_validation(self, option):
        if self.validator.is_number(option) and self.validator.is_the_range(option, self.cli_menu.get_dictionary_size(
                self.cli_menu.result_items) - 1, 1) and self.validator.has_valid_characters(option):
            return True
        else:
            return False

    def get_summary_data_items(self, key):
        return self.cli_menu.get_summary_data_items(key)

    def set_summary_data_items(self, key, value):
        self.cli_menu.set_summary_data_items(key, value)

    def get_search_for_items(self, key):
        return self.cli_menu.get_search_for_menu_items(key)

    def set_search_for_menu_item(self, key, value):
        self.cli_menu.set_search_for_menu_items(key, value)

    def get_search_in_items(self, key):
        return self.cli_menu.get_search_in_items(key)

    def set_search_in_items(self, key, value):
        self.set_search_in_items(key, value)

    def start_search_process(self):
        # Basic Search - Doing the search by Name
        if self.cli_menu.get_summary_data_items("search_for_option") == "Name":
            path = self.cli_menu.get_summary_data_items("search_in_path")
            criteria = self.cli_menu.get_summary_data_items("search_for_criteria")
            search_result = self.search.search_by_contain_common_name(path, criteria)
            self.save_search_result(search_result)

        # Basic Search - Doing the search by Extension
        if self.cli_menu.get_summary_data_items("search_for_option") == "Extension":
            path = self.cli_menu.get_summary_data_items("search_in_path")
            criteria = self.cli_menu.get_summary_data_items("search_for_criteria")
            search_result = self.search.search_by_exact_common_extension(path, criteria)
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