import unittest
from src.com.jalasoft.search_files.utils.validation import Validation


class ValidationTest(unittest.TestCase):

    def test_is_a_number_method_returns_true_when_a_number_is_provided(self):
        validation = Validation()
        value_example = "2"
        value_boolean = validation.is_number(value_example)
        self.assertTrue(value_boolean)

    def test_is_a_number_method_returns_false_when_a_negative_number_is_provided(self):
        validation = Validation()
        value_example = "-2"
        value_boolean = validation.is_number(value_example)
        self.assertFalse(value_boolean)

    def test_is_a_number_method_returns_false_when_a_alphanumeric_value_is_provided(self):
        validation = Validation()
        value_example = "Hola2"
        value_boolean = validation.is_number(value_example)
        self.assertFalse(value_boolean)

    def test_is_the_range_method_returns_true_when_string_number_is_in_the_range(self):
        validation = Validation()
        upper_limit = 2
        lower_limit = 0
        value_example = "2"
        value_boolean = validation.is_the_range(value_example, upper_limit, lower_limit)
        self.assertTrue(value_boolean)

    def test_is_the_range_method_returns_false_when_string_number_is_not_in_the_upper_range(self):
        validation = Validation()
        upper_limit = 2
        lower_limit = 0
        value_example = "3"
        value_boolean = validation.is_the_range(value_example, upper_limit, lower_limit)
        self.assertFalse(value_boolean)

    def test_is_the_range_method_returns_false_when_string_number_is_not_in_the_lower_range(self):
        validation = Validation()
        upper_limit = 2
        lower_limit = 0
        value_example = "-1"
        value_boolean = validation.is_the_range(value_example, upper_limit, lower_limit)
        self.assertFalse(value_boolean)

    def test_attempt_maximum_method_returns_true_when_the_attempt_number_does_not_exceed_5(self):
        validation = Validation()
        value_example = "2"
        value_boolean = validation.attempt_maximum(value_example)
        self.assertTrue(value_boolean)

    def test_attempt_maximum_method_returns_false_when_the_attempt_number_exceed_5(self):
        validation = Validation()
        value_example = "6"
        value_boolean = validation.attempt_maximum(value_example)
        self.assertFalse(value_boolean)

    def test_attempt_maximum_method_returns_true_when_the_attempt_number_is_equals_to_5(self):
        validation = Validation()
        value_example = "5"
        value_boolean = validation.attempt_maximum(value_example)
        self.assertTrue(value_boolean)

    def test_is_path_valid_method_returns_true_when_the_string_path_exists(self):
        validation = Validation()
        value_example = "C:\Program Files"
        value_boolean = validation.is_path_valid(value_example)
        self.assertTrue(value_boolean)

    def test_is_path_valid_method_returns_false_when_the_string_path_does_not_exist(self):
        validation = Validation()
        value_example = "X:\FundacionJALA\Fundations of SW\Leccion2"
        value_boolean = validation.is_path_valid(value_example)
        self.assertFalse(value_boolean)

    def test_is_path_valid_method_returns_false_when_value_is_null(self):
        validation = Validation()
        value_example = None
        value_boolean = validation.is_path_valid(value_example)
        self.assertFalse(value_boolean)

    def test_has_valid_characters_method_returns_true_when_value_is_numeric(self):
        validation = Validation()
        value_example = "123456789"
        value_boolean = validation.has_valid_characters(value_example)
        self.assertTrue(value_boolean)

    def test_has_valid_characters_method_returns_true_when_value_is_alphabetical_upper_case_and_lower_case(self):
        validation = Validation()
        value_example = "aAbAcC"
        value_boolean = validation.has_valid_characters(value_example)
        self.assertTrue(value_boolean)

    def test_has_valid_characters_method_returns_true_when_value_is_alphanumeric(self):
        validation = Validation()
        value_example = "aAbAcC123"
        value_boolean = validation.has_valid_characters(value_example)
        self.assertTrue(value_boolean)

    def test_has_valid_characters_method_returns_false_when_value_contain_special_characters(self):
        validation = Validation()
        value_example = "aAbAcC123+!@#"
        value_boolean = validation.has_valid_characters(value_example)
        self.assertFalse(value_boolean)

    def test_is_blank_method_returns_true_if_the_string_contain_blank_string(self):
        validation = Validation()
        value_example = "   "
        value_boolean = validation.is_blank(value_example)
        self.assertTrue(value_boolean)

    def test_is_blank_method_returns_false_if_the_string_does_not_contain_blank_string(self):
        validation = Validation()
        value_example = "HELLO"
        value_boolean = validation.is_blank(value_example)
        self.assertFalse(value_boolean)

    def test_return_true_if_the_date_string_contain_the_date_format_year_month_day_when_year_is_in_short_format(self):
        validation = Validation()
        value_example = "2018/01/25"
        value_boolean = validation.is_valid_date(value_example)
        self.assertTrue(value_boolean)

    def test_return_true_if_the_date_string_contain_the_date_format_year_month_day_when_year_is_in_long_format(self):
        validation = Validation()
        value_example = "18/01/25"
        value_boolean = validation.is_valid_date(value_example)
        self.assertTrue(value_boolean)

    def test_return_false_if_the_date_string_does_not_contain_the_date_format_year_month_day(self):
        validation = Validation()
        value_example = "123sadasd123asdas"
        value_boolean = validation.is_valid_date(value_example)
        self.assertFalse(value_boolean)

    def test_return_false_if_the_date_string_contain_the_date_format_year_month_day_but_the_day_is_no_valid(self):
        validation = Validation()
        value_example = "2018/01/60"
        value_boolean = validation.is_valid_date(value_example)
        self.assertFalse(value_boolean)

    def test_return_false_if_the_date_string_contain_the_date_format_year_month_day_but_the_month_is_no_valid(self):
        validation = Validation()
        value_example = "2018/16/03"
        value_boolean = validation.is_valid_date(value_example)
        self.assertFalse(value_boolean)


if __name__ == "__main__":
    unittest.main()
