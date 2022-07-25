
"""Bucle while"""
"""
Reglas:
- Ingresar numeros enteros por teclado hasta que el usuario ingrese 1
- Realizar la sumatoria de todos los numeros ingresados
 """

numero = int(input("Ingrese un numero: "))
total = 0
while numero != 1:
    total = total + numero
    print("Mi suma hasta el momento es: {}".format(total))
    numero = int(input("Ingrese un numero: "))

print("La sumatoria de todos tus numeross ingresados es: {}".format(total))




