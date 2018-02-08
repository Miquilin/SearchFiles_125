import os


class Validation(object):
    def __init__(self):
        pass

    def is_number(self, cadena):
        response_bool = cadena.isdigit()
        return response_bool

    def is_the_range(self, number, upper_limit, lower_limit):
        number = int(number)
        if number >= lower_limit and number <= upper_limit:
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




