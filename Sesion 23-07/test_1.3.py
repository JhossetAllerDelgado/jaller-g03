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
def suma(a, b, c, d):
    time.sleep(1)
    return a + b + c + d

@mesureTime
def resta(x, y):
    time.sleep(1)
    return x - y

print(suma(90, 500, 600, 1000))
print(resta(90,500))