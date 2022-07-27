"""
3. (3 ptos) Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que medirá el tiempo de
ejecución. Apoyarse importando la librería time
- Crear una función, por ejemplo, división de dos números para decorarla con
la función anterior.
- Usar la propiedad de N parámetros para la función a decorar (*, **) y
visualizar los resultados con un mínimo tres ejemplos.
Sugerencia: Usar sleep para visualizar mejor el tiempo de ejecución
"""

import time

def times(func):

    def calculator(*args, **kwargs):
        start = time.time()

        resul = func(*args, **kwargs)

        total = time.time() - start
        print("El tiempo de ejecucion es: {}".format(total))

        return resul

    return calculator

@times
def dividir(a, b):
    time.sleep(1)
    return a / b

print(dividir(500, 5))

"""los tiempos de los 3 ejemplos son:"""
#1.0125236511230469
#1.0036616325378418
#1.0075907707214355