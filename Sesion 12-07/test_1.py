"""Manejo de excepciones"""

"""Para controlar el error de division entre cero y el tipo de dato"""

try:
    #val1 = 100/0
    suma = 1000 + "Hola Python"
except ZeroDivisionError:
    print("No es posible una division entre cero")
except TypeError:
    print("No es posible sumar el tipo de dato entero y tipo string")