"""
1. Escribir un programa para el manejo de listas el cuál cumplirá los siguientes
requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 número aleatorios e
imprimirlos por consola.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará lista para ordenar de mayor a menor la
lista que se creará en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlo por
consola.
- Crear una función para indicar cuál es mayor número de la lista (lista del
ítem 2), retornar este valor e imprimirlo por consola.
"""

import random

def generarNumeros():
    list = []
    for i in range(10):
        num = random.randint(1, 20)
        list.append(num)
    return list

def ordenar(list):
    return list.sort()

def imprimir(list):
    print(list)


