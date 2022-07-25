
"""Decoradores en Python"""

"""Creacion de una funcion decoradora"""
def funcion(funcionB):

    def funcionC(*args, **kwargs):
        print("Antes de ejecutar la funcion decorar")
        resultado = funcionB(*args, **kwargs)
        print("Despues de ejecutar la funcion decorar")
        return resultado
    return funcionC

@funcionA
def saludar(nombre):
    print("Hola {} {}, usted tiene {} años".format(nombre, apellido, edad))

nombre = input("Ingrese su nombre por favor: ")
apellido = input("Ingrese su apellido por favor: ")
edad = input("Ingrese su edad finalmente: ")

saludar(nombre, apellido, edad)