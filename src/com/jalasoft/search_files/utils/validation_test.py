import unittest
from validations.validation import Validation

class ValidationsTest(unittest.TestCase):
    def The_value_is_a_number(self):
        ValueExample = ["Hola", "2", "-2"]
        message = "El valor es {Value} = {boolean}"
        for cadena in ValueExample:
            ValueBoolean = Validation.Isnumber(Validation, cadena)
            print(message.format(Value=cadena, boolean=ValueBoolean))
            self.assertTrue(ValueBoolean)

    def The_value_is_within_a_range(self):
        pass


if __name__ == "__main__":
    unittest.main()
