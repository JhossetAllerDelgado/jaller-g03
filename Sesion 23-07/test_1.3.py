"""Decoradores en Python"""
import time

def mesureTime(func):

    def calculator(*args, **kwargs):
        start = time.time()

        resul = func(*args, **kwargs)

        total = time.time() - start
        print("Tiempo de ejecucion es: {}".format(total))

        return resul

    return calculator

@mesureTime
def suma(a, b):
    time.sleep(1)
    resultado = a + b
    return resultado

print(suma(90, 500, 600, 1000))