
"""Creacion de una lista"""
"""Una variable que contenga 30 numeros aleatorios"""
"""Mostrar los valores al cuadrado y al cubo de los datos de la lista Random"""
import random
listaRandom = []

for indice in range(1,31):
    listaRandom.append(random.randint(5, 20))
print(listaRandom)
"""Obtener el tamaño de mi lista"""
print("El tamaño de mi lista es: {}".format(len(listaRandom)))
valor1 = 3**2
valor2 = 3**3
"""ejemplos para elevar al cuadrado y al cubo"""
for valor in listaRandom:
    print("El valor cuadrado es: {} y el valor cubo es: {}".format(valor**2, valor**3))

for indice in range(1, 31):
    val = random.randint(5, 20)
    print("Numero random original {}".format(val))
    print("el cuadrado: {} y el cubo es: {}".format(val**2, val**3))

    v = 39
    print("es {}".format(v%10))


