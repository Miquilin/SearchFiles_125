from src.com.jalasoft.search_files.utils.validation import Validation


print("***********PRIMER TEST***********")
value_example = ["Hola", "2", "-2"]
message = "El valor es {Value} = {boolean}"
for cadena in value_example:
    value_boolean = Validation.is_number(Validation, cadena)
    print(message.format(Value=cadena, boolean=value_boolean))

print("***********SEGUNDO TEST***********")
upperLimit = 2
lowerLimit = 0
value_example = ["-1", "0", "1", "2", "3"]
message = "Los limites son de {lowerLimit} a {upperLimit} el valor es {Value}: {boolean}"
for cadena in value_example:
    value_boolean = Validation.is_the_range(Validation, cadena, upperLimit, lowerLimit)
    print(message.format(Value=cadena, boolean=value_boolean, lowerLimit=lowerLimit, upperLimit=upperLimit))

print("***********TERCER TEST***********")
value_example = ["0", "1", "2", "3", "4", "5", "6"]
message = "La cantidad maxima de intentos es 5 intento numero {Value}: {boolean}"
for cadena in value_example:
    value_boolean = Validation.attempt_maximum(Validation, cadena)
    print(message.format(Value=cadena, boolean=value_boolean))

print("***********CUARTO TEST***********")

value_example = ["D:\FundacionJALA\Fundations of SW\Leccion2", "C:\Program Files", "Hola como estan"]
message = "{Value} es: {boolean}"
for cadena in value_example:
    value_boolean = Validation.is_path_valid(Validation, cadena)
    print(message.format(Value=cadena, boolean=value_boolean))

print("***********QUINTO TEST***********")
value_example = ["text*", "Text", "Text12", ]
message = "{Value} es: {boolean}"
for cadena in value_example:
    value_boolean = Validation.has_valid_characters(Validation, cadena)
    print(message.format(Value=cadena, boolean=value_boolean))



