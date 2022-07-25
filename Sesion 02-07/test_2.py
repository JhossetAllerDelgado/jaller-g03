"""Conversion de datos"""

var1 = "2023"
var2 = type(int(var1))
"""Esto no es posible porque el valor contiene una letra"""
var3 = "Año 2023"
var4 = type(int(var3))

print("El tipo de dato de mi var 2 es: {}".format(var2))
"""Mostrara un valor que no lo puede convertir a entero"""
print("El tipo de dato de mi var 2 es: {}".format(var4))

