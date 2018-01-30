import os
import re


class Validation(object):
    def __init__(self):
        pass

    def is_number(self, cadena):
        responseBool = cadena.isdigit()
        return responseBool

    def is_the_range(self, number, upperLimit, lowerLimit):
        number = int(number)
        if number >= lowerLimit and number <= upperLimit:
            return True
        else:
            return False

    def attempt_maximum(self, intentos):
        intentos = int(intentos)
        if intentos <= 5:
            return True
        else:
            return False

    def is_path_valid(self, directory):
        directory = str(directory)
        return os.path.exists(directory)

    def has_valid_characters(self, cadena):
        cadena = str(cadena)
        return cadena.isalnum()

    def has_valid_characters1(self, cadena):
        cadena = str(cadena)
        if (cadena.isalnum()):
            return True
        elif re.search("*"):
            return True
        else:
            return False















