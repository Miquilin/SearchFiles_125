import datetime
import os
from src.com.jalasoft.search_files.utils.logging_config import logger


class CLIMenu(object):
    MENU_TITLE = "WELCOME TO SEARCH FILE TOOL"

    def __init__(self):
        logger.info("Starting the method")
        self.main_menu_items = {
            "1": "Basic Search",
            "2": "Advanced Search",
            "0": "Exit"
        }
        self.basic_search_for_menu_items = {
            "1": "Name",
            "2": "Extension",
            "0": "Exit"
        }
        self.summary_items = {
            "1": "Start to search",
            "2": "Back to main menu",
            "0": "Exit"
        }
        self.basic_summary_data_entry_items = {
            "search_for_option": "",
            "search_for_criteria": "",
            "search_in_path": ""
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
        self.advanced_search_for_name_items = {
            "1": "Name - Contains text",
            "2": "Name - Exact Text",
            "3": "None",
            "0": "Exit"
        }
        self.advanced_search_for_size_items = {
            "1": "Major than 'X' MB.",
            "2": "Minor than 'X' MB.",
            "3": "None",
            "0": "Exit"
        }
        self.advanced_search_for_date_criteria_items = {
            "1": "Creation date",
            "2": "Modification date",
            "3": "None",
            "0": "Exit"
        }
        self.advanced_search_for_date_operator_items = {
            "1": "Major than 'X' date",
            "2": "Minor than 'X' date",
            "0": "Exit"
        }
        self.advanced_summary_data_entry_items = {
            "search_for_name": "",
            "search_for_name_criteria": "",
            "search_for_extension_criteria": "",
            "search_for_size": "",
            "search_for_size_criteria": "",
            "search_for_owner_criteria": "",
            "search_for_date_criteria": "",
            "search_for_date_operation_criteria": "",
            "search_for_date_text_criteria": "",
            "search_for_content_criteria": "",
            "search_in": "",
            "search_in_criteria": ""
        }
        self.advanced_search_in_items = {
            "1": "All [including sub-folders]",
            "2": "Current Folder",
            "0": "Exit"
        }
        logger.info("Ending the method")

    def get_basic_search_for_menu_items(self, key):
        logger.info("Starting the method")
        search_for_menu_item = self.basic_search_for_menu_items[key]
        logger.debug("The value returned is: %s", search_for_menu_item)
        logger.info("ending the method")
        return search_for_menu_item

    def set_basic_search_for_menu_items(self, key, value):
        logger.info("Starting the method")
        self.basic_search_for_menu_items[key] = value
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("ending the method")

    def get_basic_summary_data_items(self, key):
        logger.info("Starting the method")
        summary_data_item = self.basic_summary_data_entry_items[key]
        logger.debug("The value returned is: %s", summary_data_item)
        logger.info("ending the method")
        return summary_data_item

    def set_basic_summary_data_items(self, key, value):
        logger.info("Starting the method")
        self.basic_summary_data_entry_items[key] = value
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("ending the method")

    def get_advanced_search_for_name_items(self, key):
        logger.info("Starting the method")
        search_for_name_item = self.advanced_search_for_name_items[key]
        logger.debug("The value returned is: %s", search_for_name_item)
        logger.info("ending the method")
        return search_for_name_item

    def set_advanced_search_for_name_items(self, key, value):
        logger.info("Starting the method")
        self.advanced_search_for_name_items[key] = value
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("ending the method")

    def get_advanced_search_for_size_items(self, key):
        logger.info("Starting the method")
        search_for_size_items = self.advanced_search_for_size_items[key]
        logger.debug("The value returned is: %s", search_for_size_items)
        logger.info("ending the method")
        return search_for_size_items

    def set_advanced_search_for_size_items(self, key, value):
        logger.info("Starting the method")
        self.advanced_search_for_size_items[key] = value
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("ending the method")

    def get_advanced_search_for_date_operator_items(self, key):
        logger.info("Starting the method")
        search_for_date_item = self.advanced_search_for_date_operator_items[key]
        logger.debug("The value returned is: %s", search_for_date_item)
        logger.info("ending the method")
        return search_for_date_item

    def set_advanced_search_for_date_operator_items(self, key, value):
        logger.info("Starting the method")
        self.advanced_search_for_date_operator_items[key] = value
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("ending the method")

    def get_advanced_search_for_date_criteria_items(self, key):
        logger.info("Starting the method")
        search_for_date_item = self.advanced_search_for_date_criteria_items[key]
        logger.debug("The value returned is: %s", search_for_date_item)
        logger.info("ending the method")
        return search_for_date_item

    def set_advanced_search_for_date_criteria_items(self, key, value):
        logger.info("Starting the method")
        self.advanced_search_for_date_criteria_items[key] = value
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("ending the method")

    def get_advanced_search_in_items(self, key):
        logger.info("Starting the method")
        search_in_item = self.advanced_search_in_items[key]
        logger.debug("The value returned is: %s", search_in_item)
        logger.info("ending the method")
        return search_in_item

    def set_advanced_search_in_items(self, key, value):
        logger.info("Starting the method")
        self.advanced_search_in_items[key] = value
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("ending the method")

    def get_advanced_summary_data_items(self, key):
        logger.info("Starting the method")
        summary_data_item = self.advanced_summary_data_entry_items[key]
        logger.debug("The value returned is: %s", summary_data_item)
        logger.info("ending the method")
        return summary_data_item

    def set_advanced_summary_data_items(self, key, value):
        logger.info("Starting the method")
        self.advanced_summary_data_entry_items[key] = value
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("ending the method")

    def get_results_data(self, key):
        logger.info("Starting the method")
        result_data = self.results_data[key]
        logger.debug("The value returned is: %s", result_data)
        logger.info("ending the method")
        return result_data

    def set_results_data(self, key, value):
        logger.info("Starting the method")
        self.results_data[key] = value
        logger.debug("The data updated into the dictionary is: key: %s, Value: %s", key, value)
        logger.info("ending the method")

    def get_dictionary_size(self, dictionary_name):
        logger.info("Starting the method")
        dictionary_size = len(dictionary_name)
        logger.debug("The value returned is: %s", dictionary_size)
        logger.info("ending the method")
        return dictionary_size

    def main_menu(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Main Menu:")
        for key, value in self.main_menu_items.items():
            print(key + ". ", value)
        print("Select and option:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("ending the method")
        return criteria

    def basic_search_for_menu(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Basic Search - Search For:")
        for key, value in self.basic_search_for_menu_items.items():
            print(key + ". ", value)
        print("Select and option:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def basic_search_for_criteria(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Basic Search - Introduce the search criteria:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def basic_search_in_path(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Basic Search - Introduce the folder path:")
        criteria = input(" >>  ")
        return criteria

    def basic_summary_menu(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Basic Search - Summary:")
        print(" - Search For: ", self.basic_summary_data_entry_items["search_for_option"])
        print(" - Criteria: ", self.basic_summary_data_entry_items["search_for_criteria"])
        print(" - Path: ", self.basic_summary_data_entry_items["search_in_path"])
        print("")
        print("What do you want to do?")
        for key, value in self.summary_items.items():
            print(key + ". ", value)
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def results_menu(self):
        logger.info("Starting the method")
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
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_for_name_menu(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Search For Name:")
        for key, value in self.advanced_search_for_name_items.items():
            print(key + ". ", value)
        print("Select and option:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_for_name_criteria(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Introduce the 'Name' criteria:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_for_extension_criteria(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Introduce the 'Extension' criteria:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_for_size_menu(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Search For Size:")
        for key, value in self.advanced_search_for_size_items.items():
            print(key + ". ", value)
        print("Select and option:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_for_size_criteria(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Introduce the 'Size' criteria:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_for_owner_criteria(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Introduce the 'Owner' criteria:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_for_date_operator_menu(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Search For Date:")
        for key, value in self.advanced_search_for_date_operator_items.items():
            print(key + ". ", value)
        print("Select and option:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_for_date_criteria_menu(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Search For Date:")
        for key, value in self.advanced_search_for_date_criteria_items.items():
            print(key + ". ", value)
        print("Select and option:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_for_date_criteria(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Introduce the 'Date' criteria in YYYY-MM-DD hh:mm:ss format:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        date_criteria, time_criteria = map(str, criteria.split(' '))
        year, month, day = map(int, date_criteria.split('-'))
        hour, minutes, seconds = map(int, time_criteria.split(':'))
        datetime_criteria = datetime.datetime(year, month, day, hour, minutes, seconds)
        logger.info("Ending the method")
        return datetime_criteria

    def advanced_search_for_content_criteria(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Introduce the 'Content' criteria:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_in_menu(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Search For:")
        for key, value in self.advanced_search_in_items.items():
            print(key + ". ", value)
        print("Select and option:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_search_in_criteria_path(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Introduce the folder path:")
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def advanced_summary_menu(self):
        logger.info("Starting the method")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.MENU_TITLE)
        print("Advanced Search - Summary:")
        print(" - Search For Name: ", self.advanced_summary_data_entry_items["search_for_name"])
        print(" - Search For Name Criteria: ", self.advanced_summary_data_entry_items["search_for_name_criteria"])
        print(" - Search For Extension Criteria: ", self.advanced_summary_data_entry_items["search_for_extension_criteria"])
        print(" - Search For Size: ", self.advanced_summary_data_entry_items["search_for_size"])
        print(" - Search For Size Criteria: ", self.advanced_summary_data_entry_items["search_for_size_criteria"])
        print(" - Search For Owner Criteria: ", self.advanced_summary_data_entry_items["search_for_owner_criteria"])
        print(" - Search For Date Criteria: ", self.advanced_summary_data_entry_items["search_for_date_criteria"])
        print(" - Search For Date Operator: ", self.advanced_summary_data_entry_items["search_for_date_operation_criteria"])
        print(" - Search For Date Value Criteria: ", self.advanced_summary_data_entry_items["search_for_date_text_criteria"])
        print(" - Search For Content Criteria: ", self.advanced_summary_data_entry_items["search_for_content_criteria"])
        print(" - Search In: ", self.advanced_summary_data_entry_items["search_in"])
        print(" - Search In Criteria: ", self.advanced_summary_data_entry_items["search_in_criteria"])
        print("")
        print("What do you want to do?")
        for key, value in self.summary_items.items():
            print(key + ". ", value)
        criteria = input(" >>  ")
        logger.debug("The option selected is: %s", criteria)
        logger.info("Ending the method")
        return criteria

    def clean_summary_data_entry_items_dict(self):
        self.advanced_summary_data_entry_items["search_for_name"] = ""
        self.advanced_summary_data_entry_items["search_for_name_criteria"] = ""
        self.advanced_summary_data_entry_items["search_for_extension_criteria"] = ""
        self.advanced_summary_data_entry_items["search_for_size"] = ""
        self.advanced_summary_data_entry_items["search_for_size_criteria"] = ""
        self.advanced_summary_data_entry_items["search_for_owner_criteria"] = ""
        self.advanced_summary_data_entry_items["search_for_date_criteria"] = ""
        self.advanced_summary_data_entry_items["search_for_date_operation_criteria"] = ""
        self.advanced_summary_data_entry_items["search_for_date_text_criteria"] = ""
        self.advanced_summary_data_entry_items["search_for_content_criteria"] = ""
        self.advanced_summary_data_entry_items["search_in"] = ""
        self.advanced_summary_data_entry_items["search_in_criteria"] = ""
