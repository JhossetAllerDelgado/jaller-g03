"""Decoradores en Python"""
"""Creacion de funcion decoradora"""
def funcionA(funcionB):
     """Funcion interna de la funcion decoradora"""
     def funcionC():
         print("1. Antes de ejecutar la funcion decorar")
         funcionB()
         print("\n2. Despues de ejecutar la funcion a decorar")

     return funcionC()

@funcionA
def saludar():
    print("Hola Pytonista!!")


