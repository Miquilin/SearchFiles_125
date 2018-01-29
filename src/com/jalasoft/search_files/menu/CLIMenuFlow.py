import os
from src.com.jalasoft.search_files.menu.CLIMenu import CLIMenu

class CLIMenuFlow(object):

    def __init__(self):
        self.cli_menu = CLIMenu()

    def show_menu(self, option):
        if option == 0:
            value = 0
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


def main():
    menu = CLIMenuFlow()
    while (True):
        go_to_search_criteria = False
        choice = menu.show_menu(1)
        #Search For - menu 1
        while(go_to_search_criteria == False):
            if menu.search_for_option_validation(choice):
                menu.set_summary_data_items("search_for_option", menu.get_search_for_items(choice))
                go_to_search_criteria = True
                go_to_search_in_menu = False
                choice = menu.show_menu(2)
            else:
                  choice = menu.show_menu(1)
        #Search For Criteria - Menu 2
        while(go_to_search_in_menu == False):
            if menu.search_for_criteria_validation(choice):
                menu.set_summary_data_items("search_for_criteria", choice)
                go_to_search_in_menu = True
                go_to_search_in_path = False
                choice = menu.show_menu(3)
            else:
                  choice = menu.show_menu(2)
        #Search In - Menu 3
        while(go_to_search_in_path == False):
            if menu.search_in_option_validation(choice):
                menu.set_summary_data_items("search_in_option", menu.get_search_in_items(choice))
                go_to_search_in_path = True
                go_to_summary_option = False
                choice = menu.show_menu(4)
            else:
                  choice = menu.show_menu(3)
        #Searh in path - Menu 4
        while(go_to_summary_option == False):
            if menu.search_in_path_validation(choice):
                menu.set_summary_data_items("search_in_path", choice)
                go_to_summary_option = True
                go_to_search_results = False
                choice = menu.show_menu(5)
            else:
                choice = menu.show_menu(4)
        #Summary - Menu 5
        while(go_to_search_results == False):
            if menu.summary_option_validation(choice):
                if choice == "1":
                    print("doing the search")
                    #here add the search method
                    go_to_search_results = True
                    go_to_new_search = False
                    choice = menu.show_menu(6)
                if choice == "2":
                    go_to_new_search = True
                    break
            else:
                choice = menu.show_menu(5)
        #Result - Menu 6
        while(go_to_new_search == False):
            if menu.result_option_validation(choice):
                if choice == "1":
                    print(choice, " doing the copy to clipboard")
                    ## Here the code related to Clipboard
                    choice = menu.show_menu(6)
                if choice == "2":
                    print(choice, " doing a new search")
                    break


if __name__ == "__main__":
    #menu = CLIMenu()
    #menu.search_for_menu()
    main()


