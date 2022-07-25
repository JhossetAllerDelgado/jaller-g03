"""Bucle while"""
"""
- Leer por teclado enteros positivos hasta que el usuario ingrese -1
- Imprimir la suma de todos los digitos que lo componen
"""
numero = int(input("Ingrese un numero positivo"))
suma = 0

while numero != 0:
    digito = numero % 10
    suma = suma + digito
    print("digito {}".format(digito))
    print("suma {}".format(suma))
    numero = numero//10

    print("La suma de los digitos es: {}".format(suma))






