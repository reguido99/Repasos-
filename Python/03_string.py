## STRINGS ##

my_string = "My String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

# salto de linea 
my_new_line_string = " Este es un string\n con salto de linea"
print(my_new_line_string)

# tabulador

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

# formatos en de Strings 

name, surname, age = "Guido", "REYES", 25
print("MI nombre es {} {} y mi edad es de {} años".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es de {age}")

# separar caracteres de un string 
lenguaje = "Python"
a,b,c,d,e,f = lenguaje
print(a) #P
print(f) #N

#Division de caracteres 

lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

language_slice = lenguaje[1:]
print(language_slice)


language_slice = lenguaje[-2]
print(language_slice)

language_slice = lenguaje[0:6:2]
print(language_slice)

## Reverse 

reversed_language = lenguaje[::-1]
print(reversed_language)

### FUNCIONES DEL LENGUAJE PARA STRING 

print(lenguaje.capitalize()) ## se utiliza para poner en mayúscula la primera letra de una cadena. 
                            # Convierte el resto de las letras en minúsculas
print(lenguaje.upper())     ## Mayusculas 
print(lenguaje.count("t"))  ## contará el número de letras indicadas 
print(lenguaje.isnumeric()) ## comprueba si todos los caracteres de la cadena son numéricos
print(lenguaje.lower())     ## Minusculas 
print(lenguaje.lower().isupper()) ## isupper() devuelve True si todos los caracteres están en mayúsculas, 
                            # en caso contrario False.
print(lenguaje.startswith("Py"))
print("Py" == "py")  # No es lo mismo
