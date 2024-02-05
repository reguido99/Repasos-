## Operaciones aritméticas 

# operaciones con ENTEROS

print(4 + 8) 
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)  # doble barra inclinada es una división entera
        # devuelve solo el cociente de la división (es decir, sin residuo)
print(2 ** 3) #exponente 3 
print(2 ** 3 + 3 - 7 / 1 // 4)

#operaciones con cadenas de texto 

print("Hola" + " Python" + " ¿Qué tal?")
print("Hola " + str(2))

# operaciones mixtas
print("hola " * 5)     # escribe 5 veces la palabra hola 
print("Hola " * (2**3)) # imprime 8 veces hola  

my_float = 2.5 * 2 
print(" Hola " * int(my_float)) # concatena a la cadena la variable flotante para imprimir 

## OPERACIONES OMPARATIVAS 

# operaciones con enteros 
print(3 > 4) # mayor 
print(3 < 4) # menor
print(3 >= 4) # mayor o igual 
print(4 <= 4) # menor o igual 
print(3 == 4) # igual mismo tipo de variable 
print(3 != 4) # diferente 

# operaciones con cadena de text 

print("Hola" > "Python")
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")


### Operadores Lógicos ###

# Basada en el Álgebra de Boole

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python") 
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))
