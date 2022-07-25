
"""Bucle While"""

numero = int(input("Ingrese numero menos de 10: "))

while numero < 10:
    numero += 1 #Aumenta en uno el valor de la variable "numero"
    print("El numero es: {}".format(numero))
    if numero == 8:
        print("Numero encontrado!!")
        break  #Break: Nos permite romper el bucle antes que llegue al tope de la condicion


print("Llego al final del bucle while")

