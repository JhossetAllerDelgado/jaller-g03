"""
Usando el concepto y funciones de lista, realizar un programa con las siguiente características:

- Crear una lista con 10 valores random o alatorios
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas.
"""

import random
listaRandom = []

for indice in range(1,11):
    listaRandom.append(random.randint(0, 20))
print(listaRandom)

"""ejemplos para elevar al cuadrado y al cubo"""
for valor in listaRandom:
    print("El valor del cuadrado es: {}".format(valor**2))

for valor in listaRandom:
    print("El valor del cubo es: {}".format(valor**3))

for valor in listaRandom:
    print("La suma es: {}".format(valor**2 + valor**3))
