import unittest
from src.com.jalasoft.search_files.utils.validation import Validation

class ValidationsTest(unittest.TestCase):
    def the_value_is_a_number(self):
        value_example = ["Hola", "2", "-2"]
        message = "El valor es {Value} = {boolean}"
        for cadena in value_example:
            value_boolean = Validation.is_number(Validation, cadena)
            print(message.format(Value=cadena, boolean=value_boolean))
            self.assertTrue(value_boolean)

    def the_value_is_within_a_range(self):
        pass


if __name__ == "__main__":
    unittest.main()
