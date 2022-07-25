"""
Usando los tipos de datos y sus conversiones realizar lo siguiente
- Pedir por consola nombre y edad.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos ingresados.
- Pedir los nombre para dos personales y finalmente mostrar en pantalla la suma de ambos.
"""
nombre = input("Hola, ¿Cual es tu nombre?")
edad = int(input("por favor ingrese su edad"))
nombre2 = input("Hola, ¿Cual es tu nombre?")
edad2 = int(input("por favor ingrese su edad"))
var1 = edad
var2 = edad2

if type(var1) == type(var1):
    print(type(var1))
    print("El dato es tipo entero")

else:
    print("El dato ingresado por el usuario no es entero")
if type(var2) == type(var2):
    print(type(var1))
    print("El dato es tipo entero")

else:
    print("El dato ingresado por el usuario no es entero")

suma= var1 + var2

print("La suma de ambas edades es : {}".format(suma))




