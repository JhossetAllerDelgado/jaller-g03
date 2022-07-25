
"""Gestion de errores"""
"""Estructura y uso"""

while True:
    try:
        numero = int(input("Ingrese un numero entero: "))
    except:    #Dentro del except se activara una accion si ocurre cierto tipo de error dentro del try
        print("No es un valor entero")

        #print("Se encontro un dato erroneo en la posicion 80")
