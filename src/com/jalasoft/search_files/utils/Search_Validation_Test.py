from src.com.jalasoft.search_files.utils.Search_Validation import SearchValidation

print("**********Primer Test************************")
string_1 = ["HOLA", "hola", "1234,", "la mu"]
string_2 = "HOLA mundo"
flag = 1
message = "{string_1} existe en {string_2}: {boolean}"
for cadena in string_1:
    ValueBoolean = SearchValidation.the_string1_exists_within_the_string2(SearchValidation, cadena, string_2, flag)
    print(message.format(string_1=cadena, string_2=string_2, boolean=ValueBoolean))


print("**********Segundo Test************************")
string_1 = ["HOLA mundo", "hola mundo", "HOLAmundo", "123456", " "]
string_2 = "HOLA mundo"
flag = 1
message = "{string_1} es igual a {string_2}: {boolean}"
for cadena in string_1:
    ValueBoolean = SearchValidation.string1_equal_to_string2(SearchValidation, cadena, string_2, flag)
    print(message.format(string_1=cadena, string_2=string_2, boolean=ValueBoolean))




