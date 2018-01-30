from src.com.jalasoft.search_files.menu.CLIMenu import CLIMenu
import sys


class CLIMenuFlow(object):

    def __init__(self):
        self.cli_menu = CLIMenu()

    def show_menu(self, option):
        if option == 0:
            sys.exit()
        elif option == 1:
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
        #return False
        return True
        #if is_number(option) && is_in_range(option) && is_void():
            #return True
        #else:
            #return False

    def search_for_criteria_validation(self, option):
        return True
        #return False
        #if is_void() && has_non_supported_character():
            #return True
        #else:
            #return False

    def search_in_option_validation(self, option):
        return True
        #if is_number(option) && is_in_range(option) && is_void():
            #return True
        #else:
            #return False

    def search_in_path_validation(self, option):
        return True
        #if is_void() && is_a_valid_path(option):
            #return True
        #else:
            #return False

    def summary_option_validation(self, option):
        return True
        #if is_number(option) && is_in_range(option) && is_void():
            #return True
        #else:
            #return False

    def result_option_validation(self, option):
        return True
        #if is_number(option) && is_in_range(option) && is_void():
            #return True
        #else:
            #return False

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
        value = "doing the search"
        return value





