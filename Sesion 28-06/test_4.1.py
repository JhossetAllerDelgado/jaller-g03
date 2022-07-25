
"""Estructura de datos"""

"""Listas:  Agregando un item al final de nuestra lista"""

lista = []
lista2 = []
"""Usando interaccion con for"""

for item in range(5):
    lista.append(item*2)

print("El valor de mi lista es: {}".format(lista))


for item in range(6, 11):
    lista.append(item)

print("El valor de mi lista2 es: {}".format(lista2))
