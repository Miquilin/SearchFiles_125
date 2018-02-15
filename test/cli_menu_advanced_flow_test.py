import unittest
from src.com.jalasoft.search_files.menu.cli_menu_advanced_flow import CLIMenuAdvancedFlow


class CLIMenuTest(unittest.TestCase):
    """
    Test the CLIMenuAdvancedFlow class functions
    """

    def test_main_menu_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.main_menu_validation("1")
        self.assertEqual(result_validation, True)

    def test_main_menu_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.main_menu_validation("2")
        self.assertEqual(result_validation, True)

    def test_main_menu_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.main_menu_validation("-1")
        self.assertEqual(result_validation, False)

    def test_main_menu_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.main_menu_validation("0")
        self.assertEqual(result_validation, False)

    def test_main_menu_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.main_menu_validation("125")
        self.assertEqual(result_validation, False)

    def test_main_menu_validation_returns_false_when_option_provided_contains_a_string_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.main_menu_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_main_menu_validation_returns_false_when_option_provided_contains_non_valid_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.main_menu_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_get_results_dictionary_returns_the_results_data_dict(self):
        result_dict = {'number_files': '0', 'number_folders': '0', 'files': [], 'folders': []}
        menu = CLIMenuAdvancedFlow()
        option = menu.get_results_dictionary()
        self.assertEqual(option, result_dict)

    def test_advanced_search_for_name_menu_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_menu_validation("1")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_name_menu_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_menu_validation("2")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_name_menu_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_menu_validation("-1")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_name_menu_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_menu_validation("0")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_name_menu_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_menu_validation("125")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_name_menu_validation_returns__false_when_option_provided_has_a_string_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_menu_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_name_menu_validation_returns_false_when_option_provided_has_non_valid_chars(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_menu_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_name_criteria_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_criteria_validation("6125")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_name_criteria_validation_returns_true_when_option_provided_has_a_string_char(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_criteria_validation("MyOption")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_name_criteria_validation_returns_false_when_option_provided_has_non_valid_chars(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_criteria_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_name_criteria_validation_returns_true_when_option_provided_is_void(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_criteria_validation("")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_name_criteria_validation_returns_true_when_option_provided_is_none(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_name_criteria_validation(None)
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_extension_criteria_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_extension_criteria_validation("6125")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_extension_criteria_validation_returns_true_when_option_provided_has_string_char(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_extension_criteria_validation("MyOption")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_extension_criteria_validation_returns_false_when_option_provided_has_non_valid_char(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_extension_criteria_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_extension_criteria_validation_returns_true_when_option_provided_is_void(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_extension_criteria_validation("")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_extension_criteria_validation_returns_true_when_option_provided_is_none(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_extension_criteria_validation(None)
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_size_menu_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_menu_validation("1")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_size_menu_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_menu_validation("2")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_size_menu_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_menu_validation("-1")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_size_menu_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_menu_validation("0")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_size_menu_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_menu_validation("125")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_size_menu_validation_returns_false_when_option_provided_has_a_string_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_menu_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_size_menu_validation_returns_false_when_option_provided_has_non_valid_chars(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_menu_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_size_criteria_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_criteria_validation("6125")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_size_criteria_validation_returns_true_when_option_provided_has_a_string_char(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_criteria_validation("MyOption")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_size_criteria_validation_returns_false_when_option_provided_has_non_valid_chars(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_criteria_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_size_criteria_validation_returns_true_when_option_provided_is_void(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_criteria_validation("")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_size_criteria_validation_returns_true_when_option_provided_is_none(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_size_criteria_validation(None)
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_owner_criteria_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_owner_criteria_validation("6125")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_owner_criteria_validation_returns_true_when_option_provided_has_a_string_char(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_owner_criteria_validation("MyOption")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_owner_criteria_validation_returns_false_when_option_provided_has_non_valid_chars(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_owner_criteria_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_owner_criteria_validation_returns_true_when_option_provided_is_void(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_owner_criteria_validation("")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_owner_criteria_validation_returns_true_when_option_provided_is_none(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_owner_criteria_validation(None)
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_date_menu_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_menu_validation("1")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_date_menu_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_menu_validation("2")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_date_menu_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_menu_validation("-1")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_date_menu_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_menu_validation("0")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_date_menu_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_menu_validation("125")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_date_menu_validation_retruns_false_when_option_provided_has_a_string_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_menu_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_date_menu_validation_returns_false_when_option_provided_has_non_valid_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_menu_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_date_criteria_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_criteria_validation("6125")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_date_criteria_validation_returns_true_when_option_provided_has_a_string_char(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_criteria_validation("MyOption")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_date_criteria_validation_returns_false_when_option_provided_has_non_valid_chars(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_criteria_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_date_criteria_validation_returns_true_when_option_provided_is_void(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_criteria_validation("")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_date_criteria_validation_returns_true_when_option_provided_is_none(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_date_criteria_validation(None)
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_content_criteria_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_content_criteria_validation("6125")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_content_criteria_validation_returns_true_when_option_provided_has_a_string_char(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_content_criteria_validation("MyOption")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_content_criteria_validation_returns_false_when_option_provided_has_non_valid_chars(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_content_criteria_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_for_content_criteria_validation_returns_true_when_option_provided_is_void(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_content_criteria_validation("")
        self.assertEqual(result_validation, True)

    def test_advanced_search_for_content_criteria_validation_returns_true_when_option_provided_is_none(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_for_content_criteria_validation(None)
        self.assertEqual(result_validation, True)

    def test_advanced_search_in_menu_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_menu_validation("1")
        self.assertEqual(result_validation, True)

    def test_advanced_search_in_menu_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_menu_validation("2")
        self.assertEqual(result_validation, True)

    def test_advanced_search_in_menu_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_menu_validation("-1")
        self.assertEqual(result_validation, False)

    def test_advanced_search_in_menu_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_menu_validation("0")
        self.assertEqual(result_validation, False)

    def test_advanced_search_in_menu_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_menu_validation("125")
        self.assertEqual(result_validation, False)

    def test_advanced_search_in_menu_validation_returns_false_when_option_provided_contains_a_string_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_menu_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_advanced_search_in_menu_validation_returns_false_when_option_provided_contains_non_valid_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_menu_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_in_path_criteria_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_path_criteria_validation("6125")
        self.assertEqual(result_validation, True)

    def test_advanced_search_in_path_criteria_validation_returns_true_when_option_provided_has_a_string_char(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_path_criteria_validation("MyOption")
        self.assertEqual(result_validation, True)

    def test_advanced_search_in_path_criteria_validation_returns_false_when_option_provided_has_non_valid_chars(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_path_criteria_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_search_in_path_criteria_validation_returns_true_when_option_provided_is_void(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_path_criteria_validation("")
        self.assertEqual(result_validation, True)

    def test_advanced_search_in_path_criteria_validation_returns_true_when_option_provided_is_none(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_search_in_path_criteria_validation(None)
        self.assertEqual(result_validation, True)

    def test_advanced_summary_menu_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_summary_menu_validation("1")
        self.assertEqual(result_validation, True)

    def test_advanced_summary_menu_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_summary_menu_validation("2")
        self.assertEqual(result_validation, True)

    def test_advanced_summary_menu_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_summary_menu_validation("-1")
        self.assertEqual(result_validation, False)

    def test_advanced_summary_menu_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_summary_menu_validation("0")
        self.assertEqual(result_validation, False)

    def test_advanced_summary_menu_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_summary_menu_validation("125")
        self.assertEqual(result_validation, False)

    def test_advanced_summary_menu_validation_returns_false_when_option_provided_contains_a_string_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_summary_menu_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_advanced_summary_menu_validation_returns_false_when_option_provided_contains_non_valid_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_summary_menu_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_advanced_result_menu_validation_returns_true_when_option_provided_is_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_result_menu_validation("1")
        self.assertEqual(result_validation, True)

    def test_advanced_result_menu_validation_returns_true_when_option_provided_is_into_the_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_result_menu_validation("2")
        self.assertEqual(result_validation, True)

    def test_advanced_result_menu_validation_returns_false_when_option_provided_is_a_negative_number(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_result_menu_validation("-1")
        self.assertEqual(result_validation, False)

    def test_advanced_result_menu_validation_returns_false_when_option_provided_is_zero(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_result_menu_validation("0")
        self.assertEqual(result_validation, False)

    def test_advanced_result_menu_validation_returns_false_when_option_provided_is_out_of_range(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_result_menu_validation("125")
        self.assertEqual(result_validation, False)

    def test_advanced_result_menu_validation_returns_false_when_option_provided_contains_a_string_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_result_menu_validation("MyOption")
        self.assertEqual(result_validation, False)

    def test_advanced_result_menu_validation_returns_false_when_option_provided_contains_non_valid_character(self):
        menu = CLIMenuAdvancedFlow()
        result_validation = menu.advanced_result_menu_validation("_!#$%&/()=?¡[]_:;'¿{},.-")
        self.assertEqual(result_validation, False)

    def test_set_a_option_value_into_advanced_summary_data_entry_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("125", "A new Summary option")
        option = menu.get_advanced_summary_data_items("125")
        self.assertEqual(option, "A new Summary option")

    def test_get_search_for_name_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_for_name", "Exact Name")
        option = menu.get_advanced_summary_data_items("search_for_name")
        self.assertEqual(option, "Exact Name")

    def test_get_search_for_name_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_for_name_criteria", "My Criteria")
        option = menu.get_advanced_summary_data_items("search_for_name_criteria")
        self.assertEqual(option, "My Criteria")

    def test_get_search_for_extension_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_for_extension_criteria", "Extension Criteria")
        option = menu.get_advanced_summary_data_items("search_for_extension_criteria")
        self.assertEqual(option, "Extension Criteria")

    def test_get_search_for_size_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_for_size", "Major Than")
        option = menu.get_advanced_summary_data_items("search_for_size")
        self.assertEqual(option, "Major Than")

    def test_get_search_for_size_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_for_size_criteria", "100")
        option = menu.get_advanced_summary_data_items("search_for_size_criteria")
        self.assertEqual(option, "100")

    def test_get_search_for_owner_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_for_owner_criteria", "Me")
        option = menu.get_advanced_summary_data_items("search_for_owner_criteria")
        self.assertEqual(option, "Me")

    def test_get_search_for_date_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_for_date", "Major Than")
        option = menu.get_advanced_summary_data_items("search_for_date")
        self.assertEqual(option, "Major Than")

    def test_get_search_for_date_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_for_date_criteria", "2018/02/28")
        option = menu.get_advanced_summary_data_items("search_for_date_criteria")
        self.assertEqual(option, "2018/02/28")

    def test_get_search_for_content_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_for_content_criteria", "Any Text")
        option = menu.get_advanced_summary_data_items("search_for_content_criteria")
        self.assertEqual(option, "Any Text")

    def test_get_search_in_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_in", "All")
        option = menu.get_advanced_summary_data_items("search_in")
        self.assertEqual(option, "All")

    def test_get_search_in_criteria_option_value_from_advanced_summary_data_entry_items(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_summary_data_items("search_in_criteria", "/home/miqui/Music/")
        option = menu.get_advanced_summary_data_items("search_in_criteria")
        self.assertEqual(option, "/home/miqui/Music/")

    def test_set_a_option_value_into_advanced_search_for_name_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_search_for_name_menu_items("125", "A new search option")
        option = menu.get_advanced_search_for_name_menu_items("125")
        self.assertEqual(option, "A new search option")

    def test_get_name_contains_option_value_from_advanced_search_for_name_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_name_menu_items("1")
        self.assertEqual(option, "Name - Contains text")

    def test_get_name_exact_option_value_from_advanced_search_for_name_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_name_menu_items("2")
        self.assertEqual(option, "Name - Exact Text")

    def test_get_none_option_value_from_advanced_search_for_name_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_name_menu_items("3")
        self.assertEqual(option, "None")

    def test_get_exit_option_value_from_advanced_search_for_name_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_name_menu_items("0")
        self.assertEqual(option, "Exit")

    def test_set_a_option_value_into_advanced_search_for_size_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_search_for_size_menu_items("125", "A new size option")
        option = menu.get_advanced_search_for_size_menu_items("125")
        self.assertEqual(option, "A new size option")

    def test_get_major_than_option_value_from_advanced_search_for_size_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_size_menu_items("1")
        self.assertEqual(option, "Major than 'X' MB.")

    def test_get_minor_than_option_value_from_advanced_search_for_size_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_size_menu_items("2")
        self.assertEqual(option, "Minor than 'X' MB.")

    def test_get_none_option_value_from_advanced_search_for_size_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_size_menu_items("3")
        self.assertEqual(option, "None")

    def test_get_exit_option_value_from_advanced_search_for_size_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_size_menu_items("0")
        self.assertEqual(option, "Exit")

    def test_set_a_option_value_into_advanced_search_for_date_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_search_for_date_menu_items("125", "A new date option")
        option = menu.get_advanced_search_for_date_menu_items("125")
        self.assertEqual(option, "A new date option")

    def test_get_major_than_option_value_from_advanced_search_for_date_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_date_menu_items("1")
        self.assertEqual(option, "Major than 'X' date")

    def test_get_minor_than_option_value_from_advanced_search_for_date_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_date_menu_items("2")
        self.assertEqual(option, "Minor than 'X' date")

    def test_get_none_option_value_from_advanced_search_for_date_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_date_menu_items("3")
        self.assertEqual(option, "None")

    def test_get_exit_option_value_from_advanced_search_for_date_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_for_date_menu_items("0")
        self.assertEqual(option, "Exit")

    def test_set_a_option_value_into_advanced_search_in_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        menu.set_advanced_search_in_items("6125", "A new search in option")
        option = menu.get_advanced_search_in_items("6125")
        self.assertEqual(option, "A new search in option")

    def test_get_all_option_value_from_advanced_search_in_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_in_items("1")
        self.assertEqual(option, "All [including sub-folders]")

    def test_get_current_folder_option_value_from_advanced_search_in_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_in_items("2")
        self.assertEqual(option, "Current Folder")

    def test_get_exit_option_value_from_advanced_search_in_items_dict(self):
        menu = CLIMenuAdvancedFlow()
        option = menu.get_advanced_search_in_items("0")
        self.assertEqual(option, "Exit")


if __name__ == "__main__":
    unittest.main()
