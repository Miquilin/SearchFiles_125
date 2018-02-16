import unittest
import sys
from src.com.jalasoft.search_files.menu.cli_menu_basic_flow import CLIMenuBasicFlow


class CLIMenuBasicFlowTest(unittest.TestCase):
    """
    Test the CLIMenuBasicFlow class functions
    """

    def test_get_results_dictionary_function_is_returning_the_dictionary(self):
        menu = CLIMenuBasicFlow()
        option = menu.get_results_dictionary()
        self.assertEqual(option, {'number_files': '0', 'number_folders': '0', 'files': [], 'folders': []})

    def test_main_new_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.main_menu_validation("1")
        self.assertEqual(result_validation, True)

    def test_main_new_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.main_menu_validation("2")
        self.assertEqual(result_validation, True)

    def test_main_new_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.main_menu_validation("-1")
        self.assertEqual(result_validation, False)

    def test_main_new_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.main_menu_validation("0")
        self.assertEqual(result_validation, False)

    def test_main_new_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.main_menu_validation("125")
        self.assertEqual(result_validation, False)

    def test_main_new_validation_returns_false_when_option_provided_contains_a_string_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.main_menu_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_main_new_validation_returns_false__when_option_provided_contains_non_valid_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.main_menu_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_basic_search_for_option_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_option_validation("1")
        self.assertEqual(result_validation, True)

    def test_basic_search_for_option_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_option_validation("2")
        self.assertEqual(result_validation, True)

    def test_basic_search_for_option_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_option_validation("-1")
        self.assertEqual(result_validation, False)

    def test_basic_search_for_option_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_option_validation("0")
        self.assertEqual(result_validation, False)

    def test_basic_search_for_option_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_option_validation("125")
        self.assertEqual(result_validation, False)

    def test_basic_search_for_option_validation_false_when_option_provided_contains_a_string_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_option_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_basic_search_for_option_validation_returns_false_when_option_provided_contains_non_valid_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_criteria_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_basic_search_for_criteria_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_criteria_validation("6125")
        self.assertEqual(result_validation, True)

    def test_basic_search_for_criteria_validation_true_when_option_provided_contains_a_string_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_criteria_validation("MyOption")
        self.assertEqual(result_validation, True)

    def test_basic_search_for_criteria_validation_returns_false_when_option_provided_contains_non_valid_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_for_criteria_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    @unittest.skipUnless(sys.platform.startswith("lin"), "requires Linux")
    def test_basic_search_in_path_validation_returns_true_when_option_provided_contains_a_valid_linux_path(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_in_path_validation("/home/")
        self.assertEqual(result_validation, True)

    @unittest.skipUnless(sys.platform.startswith("lin"), "requires Linux")
    def test_basic_search_in_path_validation_returns_true_when_option_provided_contains_a_non_valid_linux_path(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_in_path_validation("/home/other/path/")
        self.assertEqual(result_validation, False)

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_basic_search_in_path_validation_returns_true_when_option_provided_contains_a_valid_windows_path(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_in_path_validation("c:\\")
        self.assertEqual(result_validation, True)

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_basic_search_in_path_validation_returns_true_when_option_provided_contains_a_non_valid_windows_path(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_search_in_path_validation("x:\\other\\path\\")
        self.assertEqual(result_validation, False)

    def test_basic_summary_option_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_summary_option_validation("1")
        self.assertEqual(result_validation, True)

    def test_basic_summary_option_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_summary_option_validation("2")
        self.assertEqual(result_validation, True)

    def test_basic_summary_option_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_summary_option_validation("-1")
        self.assertEqual(result_validation, False)

    def test_basic_summary_option_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_summary_option_validation("0")
        self.assertEqual(result_validation, False)

    def test_basic_summary_option_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_summary_option_validation("125")
        self.assertEqual(result_validation, False)

    def test_basic_summary_option_validation_returns_false_when_option_provided_contains_a_string_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_summary_option_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_basic_summary_option_validation_returns_false__when_option_provided_contains_non_valid_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_summary_option_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_basic_result_option_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_result_option_validation("1")
        self.assertEqual(result_validation, True)

    def test_basic_result_option_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_result_option_validation("2")
        self.assertEqual(result_validation, True)

    def test_basic_result_option_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_result_option_validation("-1")
        self.assertEqual(result_validation, False)

    def test_basic_result_option_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_result_option_validation("0")
        self.assertEqual(result_validation, False)

    def test_basic_result_option_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_result_option_validation("125")
        self.assertEqual(result_validation, False)

    def test_basic_result_option_validation_returns_false_when_option_provided_contains_a_string_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_result_option_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_basic_result_option_validation_returns_false__when_option_provided_contains_non_valid_character(self):
        menu = CLIMenuBasicFlow()
        result_validation = menu.basic_result_option_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_set_a_option_value_into_basic_summary_data_entry_items_dict(self):
        menu = CLIMenuBasicFlow()
        menu.set_summary_data_items("125", "A new Summary option")
        option = menu.get_summary_data_items("125")
        self.assertEqual(option, "A new Summary option")

    def test_get_search_for_option_option_value_from_basic_summary_data_entry_items_dict(self):
        menu = CLIMenuBasicFlow()
        menu.set_summary_data_items("search_for_option", "Extension")
        option = menu.get_summary_data_items("search_for_option")
        self.assertEqual(option, "Extension")

    def test_get_search_for_criteria_option_value_from_basic_summary_data_entry_items_dict(self):
        menu = CLIMenuBasicFlow()
        menu.set_summary_data_items("search_for_criteria", "My Criteria")
        option = menu.get_summary_data_items("search_for_criteria")
        self.assertEqual(option, "My Criteria")

    def test_get_search_in_path_option_value_from_basic_summary_data_entry_items_dict(self):
        menu = CLIMenuBasicFlow()
        menu.set_summary_data_items("search_in_path", "/home/miqui/Music/")
        option = menu.get_summary_data_items("search_in_path")
        self.assertEqual(option, "/home/miqui/Music/")

    def test_set_a_option_value_into_basic_search_for_menu_items_dict(self):
        menu = CLIMenuBasicFlow()
        menu.set_search_for_menu_item("125", "A new search option")
        option = menu.get_search_for_menu_item("125")

        self.assertEqual(option, "A new search option")

    def test_get_name_option_value_from_basic_search_for_menu_items_dict(self):
        menu = CLIMenuBasicFlow()
        option = menu.get_search_for_menu_item("1")
        self.assertEqual(option, "Name")

    def test_get_extension_option_value_from_basic_search_for_menu_items_dict(self):
        menu = CLIMenuBasicFlow()
        option = menu.get_search_for_menu_item("2")
        self.assertEqual(option, "Extension")

    def test_get_exit_option_value_from_basic_search_for_menu_items_dict(self):
        menu = CLIMenuBasicFlow()
        option = menu.get_search_for_menu_item("0")
        self.assertEqual(option, "Exit")
