"""Manejo de excepciones"""
"""Analisis de try except"""

try:
   # valor1 = 1000/4
    valor2 = 1000/0
except:
    print("Entro al except, ha ocurrido una excepcion")
else:
    print("Entro al else, no ha ocurrido un error")


