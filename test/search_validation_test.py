import unittest
from src.com.jalasoft.search_files.utils.search_validation import SearchValidation


class SearchValidationTest(unittest.TestCase):
    def test_return_true_if_string_1_exist_within_string2_with_case_sensitive_inactive(self):
        search_validation = SearchValidation()
        string_1 = "LA mu"
        string_2 = "HOLA mundo"
        case_sensitive = False
        value_boolean = search_validation.string1_exists_within_string2(string_1, string_2, case_sensitive)
        self.assertTrue(value_boolean)

    def test_return_false_if_string_1_does_not_exist_within_string2_with_case_sensitive_inactive(self):
        search_validation = SearchValidation()
        string_1 = "la MU"
        string_2 = "HOLA mundo"
        case_sensitive = False
        value_boolean = search_validation.string1_exists_within_string2(string_1, string_2, case_sensitive)
        self.assertTrue(value_boolean)

    def test_return_true_if_string_1_exist_within_string2_with_case_sensitive_active(self):
        search_validation = SearchValidation()
        string_1 = "LA mu"
        string_2 = "HOLA mundo"
        case_sensitive = True
        value_boolean = search_validation.string1_exists_within_string2(string_1, string_2, case_sensitive)
        self.assertTrue(value_boolean)

    def test_return_false_if_string_1_exists_as_uppercase_or_lowercase_within_string2_with_case_sensitive_active(self):
        search_validation = SearchValidation()
        string_1 = "la MU"
        string_2 = "HOLA mundo"
        case_sensitive = True
        value_boolean = search_validation.string1_exists_within_string2(string_1, string_2, case_sensitive)
        self.assertFalse(value_boolean)

    def test_return_true_if_string_1_is_equal_to_string2_with_case_sensitive_inactive(self):
        search_validation = SearchValidation()
        string_1 = "HOLA mundo"
        string_2 = "HOLA mundo"
        case_sensitive = False
        value_boolean = search_validation.is_string1_equal_to_string2(string_1, string_2, case_sensitive)
        self.assertTrue(value_boolean)

    def test_return_true_if_string_1_is_not_equal_to_string2_with_case_sensitive_inactive(self):
        search_validation = SearchValidation()
        string_1 = "hola MUNDO"
        string_2 = "HOLA mundo"
        case_sensitive = False
        value_boolean = search_validation.is_string1_equal_to_string2(string_1, string_2, case_sensitive)
        self.assertTrue(value_boolean)

    def test_return_true_if_string_1_is_equal_to_string2_with_case_sensitive_active(self):
        search_validation = SearchValidation()
        string_1 = "HOLA mundo"
        string_2 = "HOLA mundo"
        case_sensitive = True
        value_boolean = search_validation.is_string1_equal_to_string2(string_1, string_2, case_sensitive)
        self.assertTrue(value_boolean)

    def test_return_false_if_string_1_with_upper_and_lower_case_is_equal_to_string2_with_case_sensitive_active(self):
        search_validation = SearchValidation()
        string_1 = "hola MUNDO"
        string_2 = "HOLA mundo"
        case_sensitive = True
        value_boolean = search_validation.is_string1_equal_to_string2(string_1, string_2, case_sensitive)
        self.assertFalse(value_boolean)

    def test_return_true_if_the_bit_size_is_less_than_to_mega_bit_size(self):
        search_validation = SearchValidation()
        num_bit = 1000000
        num_mega_bit = 2
        value_boolean = search_validation.is_less_than_or_equal(num_bit, num_mega_bit)
        self.assertTrue(value_boolean)

    def test_return_true_if_the_bit_size_is_equals_to_mega_bit_size(self):
        num_bit = 2000000
        num_mega_bit = 2
        value_boolean = SearchValidation().is_less_than_or_equal(num_bit, num_mega_bit)
        self.assertTrue(value_boolean)

    def test_return_false_if_the_bit_size_is_bigger_than_to_mega_bit_size(self):
        num_bit = 3000000
        num_mega_bit = 2
        value_boolean = SearchValidation().is_less_than_or_equal(num_bit, num_mega_bit)
        self.assertFalse(value_boolean)


if __name__ == "__main__":
    unittest.main()


