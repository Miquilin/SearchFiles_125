import unittest
from unittest import mock
from src.com.jalasoft.search_files.menu.cli_menu import CLIMenu


class CLIMenuTest(unittest.TestCase):
    """
    Test the CLIMenu class functions
    """

    def test_set_a_option_value_into_basic_search_for_menu_items_dict(self):
        menu = CLIMenu()
        menu.set_basic_search_for_menu_items("125", "A new search option")
        option = menu.get_basic_search_for_menu_items("125")

        self.assertEqual(option, "A new search option")

    def test_get_name_option_value_from_basic_search_for_menu_items_dict(self):
        menu = CLIMenu()
        option = menu.get_basic_search_for_menu_items("1")
        self.assertEqual(option, "Name")

    def test_get_extension_option_value_from_basic_search_for_menu_items_dict(self):
        menu = CLIMenu()
        option = menu.get_basic_search_for_menu_items("2")
        self.assertEqual(option, "Extension")

    def test_get_exit_option_value_from_basic_search_for_menu_items_dict(self):
        menu = CLIMenu()
        option = menu.get_basic_search_for_menu_items("0")
        self.assertEqual(option, "Exit")

    def test_set_a_option_value_into_basic_summary_data_entry_items_dict(self):
        menu = CLIMenu()
        menu.set_basic_summary_data_items("125", "A new Summary option")
        option = menu.get_basic_summary_data_items("125")
        self.assertEqual(option, "A new Summary option")

    def test_get_search_for_option_option_value_from_basic_summary_data_entry_items_dict(self):
        menu = CLIMenu()
        menu.set_basic_summary_data_items("search_for_option", "Extension")
        option = menu.get_basic_summary_data_items("search_for_option")
        self.assertEqual(option, "Extension")

    def test_get_search_for_criteria_option_value_from_basic_summary_data_entry_items_dict(self):
        menu = CLIMenu()
        menu.set_basic_summary_data_items("search_for_criteria", "My Criteria")
        option = menu.get_basic_summary_data_items("search_for_criteria")
        self.assertEqual(option, "My Criteria")

    def test_get_search_in_path_option_value_from_basic_summary_data_entry_items_dict(self):
        menu = CLIMenu()
        menu.set_basic_summary_data_items("search_in_path", "/home/miqui/Music/")
        option = menu.get_basic_summary_data_items("search_in_path")
        self.assertEqual(option, "/home/miqui/Music/")

    def test_set_a_option_value_into_advanced_search_for_name_items_dict(self):
        menu = CLIMenu()
        menu.set_advanced_search_for_name_items("125", "A new search option")
        option = menu.get_advanced_search_for_name_items("125")
        self.assertEqual(option, "A new search option")

    def test_get_name_contains_option_value_from_advanced_search_for_name_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_name_items("1")
        self.assertEqual(option, "Name - Contains text")

    def test_get_name_exact_option_value_from_advanced_search_for_name_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_name_items("2")
        self.assertEqual(option, "Name - Exact Text")

    def test_get_none_option_value_from_advanced_search_for_name_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_name_items("3")
        self.assertEqual(option, "None")

    def test_get_exit_option_value_from_advanced_search_for_name_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_name_items("0")
        self.assertEqual(option, "Exit")

    def test_set_a_option_value_into_advanced_search_for_size_items_dict(self):
        menu = CLIMenu()
        menu.set_advanced_search_for_size_items("125", "A new size option")
        option = menu.get_advanced_search_for_size_items("125")
        self.assertEqual(option, "A new size option")

    def test_get_major_than_option_value_from_advanced_search_for_size_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_size_items("1")
        self.assertEqual(option, "Major than 'X' MB.")

    def test_get_minor_than_option_value_from_advanced_search_for_size_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_size_items("2")
        self.assertEqual(option, "Minor than 'X' MB.")

    def test_get_none_option_value_from_advanced_search_for_size_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_size_items("3")
        self.assertEqual(option, "None")

    def test_get_exit_option_value_from_advanced_search_for_size_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_size_items("0")
        self.assertEqual(option, "Exit")

    def test_set_a_option_value_into_advanced_search_for_date_items_dict(self):
        menu = CLIMenu()
        menu.set_advanced_search_for_date_items("125", "A new date option")
        option = menu.get_advanced_search_for_date_items("125")
        self.assertEqual(option, "A new date option")

    def test_get_major_than_option_value_from_advanced_search_for_date_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_date_items("1")
        self.assertEqual(option, "Major than 'X' date")

    def test_get_minor_than_option_value_from_advanced_search_for_date_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_date_items("2")
        self.assertEqual(option, "Minor than 'X' date")

    def test_get_none_option_value_from_advanced_search_for_date_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_date_items("3")
        self.assertEqual(option, "None")

    def test_get_exit_option_value_from_advanced_search_for_date_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_for_date_items("0")
        self.assertEqual(option, "Exit")

    def test_set_a_option_value_into_advanced_search_in_items_dict(self):
        menu = CLIMenu()
        menu.set_advanced_search_in_items("125", "A new search in option")
        option = menu.get_advanced_search_in_items("125")
        self.assertEqual(option, "A new search in option")

    def test_get_all_option_value_from_advanced_search_in_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_in_items("1")
        self.assertEqual(option, "All [including sub-folders]")

    def test_get_current_folder_option_value_from_advanced_search_in_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_in_items("2")
        self.assertEqual(option, "Current Folder")

    def test_get_exit_option_value_from_advanced_search_in_items_dict(self):
        menu = CLIMenu()
        option = menu.get_advanced_search_in_items("0")
        self.assertEqual(option, "Exit")

    def test_set_a_option_value_into_advanced_summary_data_entry_items_dict(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("125", "A new Summary option")
        option = menu.get_advanced_summary_data_items("125")
        self.assertEqual(option, "A new Summary option")

    def test_get_search_for_name_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_for_name", "Exact Name")
        option = menu.get_advanced_summary_data_items("search_for_name")
        self.assertEqual(option, "Exact Name")

    def test_get_search_for_name_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_for_name_criteria", "My Criteria")
        option = menu.get_advanced_summary_data_items("search_for_name_criteria")
        self.assertEqual(option, "My Criteria")

    def test_get_search_for_extension_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_for_extension_criteria", "Extension Criteria")
        option = menu.get_advanced_summary_data_items("search_for_extension_criteria")
        self.assertEqual(option, "Extension Criteria")

    def test_get_search_for_size_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_for_size", "Major Than")
        option = menu.get_advanced_summary_data_items("search_for_size")
        self.assertEqual(option, "Major Than")

    def test_get_search_for_size_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_for_size_criteria", "100")
        option = menu.get_advanced_summary_data_items("search_for_size_criteria")
        self.assertEqual(option, "100")

    def test_get_search_for_owner_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_for_owner_criteria", "Me")
        option = menu.get_advanced_summary_data_items("search_for_owner_criteria")
        self.assertEqual(option, "Me")

    def test_get_search_for_date_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_for_date", "Major Than")
        option = menu.get_advanced_summary_data_items("search_for_date")
        self.assertEqual(option, "Major Than")

    def test_get_search_for_date_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_for_date_criteria", "2018/02/28")
        option = menu.get_advanced_summary_data_items("search_for_date_criteria")
        self.assertEqual(option, "2018/02/28")

    def test_get_search_for_content_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_for_content_criteria", "Any Text")
        option = menu.get_advanced_summary_data_items("search_for_content_criteria")
        self.assertEqual(option, "Any Text")

    def test_get_search_in_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_in", "All")
        option = menu.get_advanced_summary_data_items("search_in")
        self.assertEqual(option, "All")

    def test_get_search_in_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenu()
        menu.set_advanced_summary_data_items("search_in_criteria", "/home/miqui/Music/")
        option = menu.get_advanced_summary_data_items("search_in_criteria")
        self.assertEqual(option, "/home/miqui/Music/")

    def test_set_a_option_value_into_results_data_dict(self):
        menu = CLIMenu()
        menu.set_results_data("125", "A new result")
        option = menu.get_results_data("125")
        self.assertEqual(option, "A new result")

    def test_get_number_files_option_value_from_results_data_items(self):
        menu = CLIMenu()
        option = menu.get_results_data("number_files")
        self.assertEqual(option, "0")

    def test_get_number_folders_option_value_from_results_data_items(self):
        menu = CLIMenu()
        option = menu.get_results_data("number_folders")
        self.assertEqual(option, "0")

    def test_get_files_option_value_from_results_data_items(self):
        menu = CLIMenu()
        file_list = ["file1", "file2", "file3"]
        menu.set_results_data("files", file_list)
        option = menu.get_results_data("files")
        self.assertEqual(option, file_list)

    def test_get_folders_option_value_from_results_data_items(self):
        menu = CLIMenu()
        folder_list = ["folder1", "folder2", "folder3"]
        menu.set_results_data("folders", folder_list)
        option = menu.get_results_data("folders")
        self.assertListEqual(option, folder_list)

    def test_get_dictionary_size(self):
        menu = CLIMenu()
        option = menu.get_dictionary_size(menu.results_data)
        self.assertEqual(option, 4)

    @mock.patch('builtins.input', return_value='1')
    def test_main_menu_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.main_menu() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_main_menu_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.main_menu() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_main_menu_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.main_menu() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_main_menu_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.main_menu() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_basic_search_for_menu_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.basic_search_for_menu() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_basic_search_for_menu_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.basic_search_for_menu() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_basic_search_for_menu_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.basic_search_for_menu() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_basic_search_for_menu_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.basic_search_for_menu() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_basic_search_for_criteria_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.basic_search_for_criteria() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_basic_search_for_criteria_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.basic_search_for_criteria() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_basic_search_for_criteria_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.basic_search_for_criteria() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_basic_search_for_criteria_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.basic_search_for_criteria() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_basic_search_in_path_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.basic_search_in_path() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_basic_search_in_path_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.basic_search_in_path() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_basic_search_in_path_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.basic_search_in_path() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_basic_search_in_path_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.basic_search_in_path() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_basic_summary_menu_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.basic_summary_menu() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_basic_summary_menu_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.basic_summary_menu() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_basic_summary_menu_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.basic_summary_menu() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_basic_summary_menu_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.basic_summary_menu() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_results_menu_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.results_menu() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_results_menu_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.results_menu() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_results_menu_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.results_menu() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_results_menu_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.results_menu() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_for_name_menu_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_name_menu() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_for_name_menu_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_name_menu() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_for_name_menu_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_name_menu() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_for_name_menu_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_name_menu() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_for_name_criteria_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_name_criteria() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_for_name_criteria_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_name_criteria() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_for_name_criteria_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_name_criteria() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_for_name_criteria_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_name_criteria() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_for_extension_criteria_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_extension_criteria() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_for_extension_criteria_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_extension_criteria() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_for_extension_criteria_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_extension_criteria() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_for_extension_criteria_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_extension_criteria() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_for_size_menu_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_size_menu() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_for_size_menu_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_size_menu() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_for_size_menu_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_size_menu() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_for_size_menu_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_size_menu() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_for_size_criteria_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_size_criteria() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_for_size_criteria_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_size_criteria() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_for_size_criteria_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_size_criteria() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_for_size_criteria_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_size_criteria() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_for_owner_criteria_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_owner_criteria() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_for_owner_criteria_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_owner_criteria() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_for_owner_criteria_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_owner_criteria() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_for_owner_criteria_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_owner_criteria() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_for_date_menu_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_date_menu() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_for_date_menu_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_date_menu() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_for_date_menu_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_date_menu() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_for_date_menu_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_date_menu() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_for_date_criteria_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_date_criteria() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_for_date_criteria_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_date_criteria() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_for_date_criteria_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_date_criteria() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_for_date_criteria_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_date_criteria() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_for_content_criteria_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_content_criteria() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_for_content_criteria_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_content_criteria() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_for_content_criteria_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_content_criteria() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_for_content_criteria_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_for_content_criteria() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_in_menu_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_in_menu() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_in_menu_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_in_menu() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_in_menu_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_in_menu() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_in_menu_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_in_menu() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_search_in_criteria_path_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_in_criteria_path() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_search_in_criteria_path_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_in_criteria_path() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_search_in_criteria_path_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_in_criteria_path() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_search_in_criteria_path_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_search_in_criteria_path() == '*_-\[]/()'

    @mock.patch('builtins.input', return_value='1')
    def test_advanced_summary_menu_is_retuning_a_numeric_option_(self, input):
        menu = CLIMenu()
        assert menu.advanced_summary_menu() == '1'

    @mock.patch('builtins.input', return_value='AnyOption')
    def test_advanced_summary_menu_is_retuning_a_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_summary_menu() == 'AnyOption'

    @mock.patch('builtins.input', return_value='')
    def test_advanced_summary_menu_is_retuning_a_void_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_summary_menu() == ''

    @mock.patch('builtins.input', return_value='*_-\[]/()')
    def test_advanced_summary_menu_is_retuning_a_valid_special_characters_option(self, input):
        menu = CLIMenu()
        assert menu.advanced_summary_menu() == '*_-\[]/()'


if __name__ == "__main__":
    unittest.main()
