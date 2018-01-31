import unittest
from src.com.jalasoft.search_files.utils.validation import Validation


class ValidationTest(unittest.TestCase):

    def test_is_a_number_method_returns_true_when_a_number_is_provided(self):
        validation = Validation()
        value_example = "2"
        value_boolean = validation.is_number(value_example)
        self.assertTrue(value_boolean)


if __name__ == '__main__':
    unittest.main()
