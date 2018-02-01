import os


class CLIMenu(object):
    MENU_TITLE = "WELCOME TO SEARCH FILE TOOL"

    def __init__(self):
        self.search_for_menu_items = {
            "1": "Name",
            "2": "Extension",
            "3": "Content",
            "4": "Size",
            "0": "Exit"
        }
        self.search_in_items = {
            "1": "All [including sub-folders]",
            "2": "Current Folder",
            "0": "Exit"
        }
        self.summary_items = {
            "1": "Start to search",
            "2": "Back to main menu",
            "0": "Exit"
        }
        self.summary_data_entry_items = {
            "search_for_option": "Name",
            "search_for_criteria": "Test",
            "search_in_option": "Current Folder",
            "search_in_path": "c:\My Documents\share"
        }
        self.result_items = {
            "1": "Copy to clipboard",
            "2": "New Search",
            "0": "Exit"
        }
        self.results_data = {
            "number_files": "0",
            "number_folders": "0",
            "files": [],
            "folders": []
        }

    def get_search_for_menu_items(self, key):
        return self.search_for_menu_items[key]

    def set_search_for_menu_items(self, key, value):
        self.search_for_menu_items[key] = value

    def get_search_in_items(self, key):
        return self.search_in_items[key]

    def set_search_in_items(self, key, value):
        self.search_in_items[key] = value

    def get_summary_data_items(self, key):
        return self.summary_data_entry_items[key]

    def set_summary_data_items(self, key, value):
        self.summary_data_entry_items[key] = value

    def get_results_data(self, key):
        return self.results_data[key]

    def set_results_data(self, key, value):
        self.results_data[key] = value

    def get_dictionary_size(self, dictionary_name):
        return len(dictionary_name)

    def search_for_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Search For:")
        for key, value in self.search_for_menu_items.items():
            print(key + ". ", value)
        print("Select and option:")
        criteria = input(" >>  ")
        return criteria

    def search_for_criteria(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Introduce the search criteria:")
        criteria = input(" >>  ")
        return criteria

    def search_in_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Search in:")
        for key, value in self.search_in_items.items():
            print(key + ". ", value)
        print("Select an option:")
        choice = input(" >>  ")
        return choice

    def search_in_path(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Introduce the folder path:")
        criteria = input(" >>  ")
        return criteria

    def summary_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Summary:")
        print(" - Search For: ", self.summary_data_entry_items["search_for_option"])
        print(" - Criteria: ", self.summary_data_entry_items["search_for_criteria"])
        print(" - Search in: ", self.summary_data_entry_items["search_in_option"])
        print(" - Path: ", self.summary_data_entry_items["search_in_path"])
        print("")
        print("What do you want to do?")
        for key, value in self.summary_items.items():
            print(key + ". ", value)
        choice = input(" >>  ")
        return choice

    def results_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Search Results:")
        print("%s file(s) and %s folder(s) found"
              % (self.results_data["number_files"], self.results_data["number_folders"]))
        for key, value in self.results_data.items():
            if key == "files":
                print("   -----")
                for file in value:
                    print(" - ", file)
            elif key == "folders":
                print("   -----")
                for folder in value:
                    print(" - ", folder)
        print("   -----")
        print("What do you want to do?")
        for key, value in self.result_items.items():
            print(key + ". ", value)
        choice = input(" >>  ")
        return choice

