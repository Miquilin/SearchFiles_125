import os
import fnmatch

import re


class Validation(object):
    def __init__(self):
        pass

    def Isnumber(self, cadena):
        responseBool = cadena.isdigit()
        return responseBool

    def isTheRange(self, number, upperLimit, lowerLimit):
        number = int(number)
        if number >= lowerLimit and number <= upperLimit:
            return True
        else:
            return False

    def AttemptMaximum(self, intentos):
        intentos = int(intentos)
        if intentos <= 5:
            return True
        else:
            return False

    def isPathValid(self, directory):
        directory = str(directory)
        return os.path.exists(directory)

    def hasValidCharacters(self, cadena):
        cadena = str(cadena)
        return cadena.isalnum()

    def hasValidCharacters1(self, cadena):
        cadena = str(cadena)
        if (cadena.isalnum()):
            return True
        elif re.search("*"):
            return True
        else:
            return False















