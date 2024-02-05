## VARIABLES 

# declarar una varible 

# String 
my_string_variable = "My string variable"
print(my_string_variable)
# int(entero)
my_int_variable = 5 
print(my_int_variable)
# cambio 
my_int_to_str_variable = str(my_int_variable) # cambio de int a str
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
# booleadas 
my_bool_variable = False
print(my_bool_variable)

# concatenación de varibale en un print 
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

# FUNCIONES DEL SISTEMA 

print(len(my_string_variable)) # tamaño de la cadena de caracteres 

# variables en una sola linea 
name, surname, alias, age = "Guido", "Reyes","Reguido", 25
print(" Me llamo: ", name, surname, ". Mi edad es :", age,
      ". Y mi alias es : ", alias)

# INPUT o entradas 

name = input('¿Cuál es tu nombre? ')
age = input('¿Cuál es tu edada? ')
print(name)
print(age)

#cambio de las entradas o cambio de las variables ingresadas 

name = "Evelyn Aponte"
age = 32
print(name)
print(age)

#forzar el tipo de la variable 

address: str = "Mi direccion"
address = True
address = 5 
address = 1.2 
print(type(address))