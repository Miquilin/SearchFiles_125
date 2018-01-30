from src.com.jalasoft.search_files.utils.validation import Validation


print("***********PRIMER TEST***********")
ValueExample = ["Hola", "2", "-2"]
message = "El valor es {Value} = {boolean}"
for cadena in ValueExample:
    ValueBoolean = Validation.Isnumber(Validation, cadena)
    print(message.format(Value=cadena, boolean=ValueBoolean))

print("***********SEGUNDO TEST***********")
upperLimit = 2
lowerLimit = 0
ValueExample = ["-1", "0", "1", "2", "3"]
message = "Los limites son de {lowerLimit} a {upperLimit} el valor es {Value}: {boolean}"
for cadena in ValueExample:
    ValueBoolean = Validation.isTheRange(Validation, cadena, upperLimit, lowerLimit)
    print(message.format(Value=cadena, boolean=ValueBoolean, lowerLimit=lowerLimit, upperLimit=upperLimit))

print("***********TERCER TEST***********")
ValueExample = ["0", "1", "2", "3", "4", "5", "6"]
message = "La cantidad maxima de intentos es 5 intento numero {Value}: {boolean}"
for cadena in ValueExample:
    ValueBoolean = Validation.AttemptMaximum(Validation, cadena)
    print(message.format(Value=cadena, boolean=ValueBoolean))

print("***********CUARTO TEST***********")

ValueExample = ["D:\FundacionJALA\Fundations of SW\Leccion2", "C:\Program Files", "Hola como estan"]
message = "{Value} es: {boolean}"
for cadena in ValueExample:
    ValueBoolean = Validation.isPathValid(Validation, cadena)
    print(message.format(Value=cadena, boolean=ValueBoolean))

print("***********QUINTO TEST***********")
ValueExample = ["text*", "Text", "Text12", ]
message = "{Value} es: {boolean}"
for cadena in ValueExample:
    ValueBoolean = Validation.hasValidCharacters1(Validation, cadena)
    print(message.format(Value=cadena, boolean=ValueBoolean))



