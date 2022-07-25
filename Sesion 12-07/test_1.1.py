"""Manejo de excepciones"""

"""Para controlar el error de division entre cero y el tipo de dato"""
"""Multiples excepts en uno solo"""

try:
    valor1 =500 / 0
    suma = "Hola Pythonistas" + 500
except (ZeroDivisionError, TypeError):
    print("Ha ocurrido un error de DivisionZero o TypeError")








