"""
3. Escribir un programa para gestionar los errores en Python
Reglas:
- El programa deberá tener una función para ingresar dos datos los
cuáles serán ingresado por consola.
- Deberá tener una función en el caso haya una división entre cero y
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos.
- Todas las funciones creadas tendrás la facultad de volver a pedir el
número hasta que se ingrese correctamente.
"""
try:
    #val1 = 100/00

    valor1 = int(input("Ingrese el valor 1: "))
    valor2 = int(input("Ingrese el valor 2: "))
    divide = valor1/valor2

    if valor2 != 0:
        print("Valor valido")
    else:
        print("Valor no valido")

except ZeroDivisionError:
    print("No es posible una division entre cero")
except TypeError:
    print("No es posible dividir")
else:
    print("Entro al else, todo salio bien")



