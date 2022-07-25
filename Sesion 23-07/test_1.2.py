"""Decoradores en Python"""

"""Creacion de una funcion decoradora"""
def funcionA(funcionB):

    def funcionC(*args, **kwargs):
        print("Antes de ejecutar la funcion que para por parametro")
        resultado = funcionB(*args, **kwargs)
        print("Despues de ejecutar la funcion decoradora")
        print(resultado)

    return funcionC()



@funcionA
def suma(a, b, c, d):
    total = a + b + c + d
    return total

print(suma(30, 40, 100, 200))



