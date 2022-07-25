"""Programacion orientada a objetos"""
"""Atributos de datos a una clase"""
class Carro:
    """Atributos"""
    ruedas = 4

    """Constructor: Valores que va a tener por defecto mi clase cuando se le instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Metodos: son las funciones de la clase"""
    def acelera(self):
            self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
            velocidad = self.velocidad - self.aceleracion
            if velocidad < 0:
                velocidad = 0
            self.velocidad = velocidad

carro1 = Carro("Rojo", 20)
print("El color de mi primer carro es: {}".format(carro1.color))

carro2 = Carro("Blanco", 40)
"""Se agregara atributo de dato a la instancia del segundo carro"""

carro2.marchas = 2000

print("El numero de marchas que puede dar mi segundo carro es: {}".format(carro2.marchas))
"""No es posible llamar un atributo de datos que se le fue asignada a otra instancia de la clase"""
#print("El numero de marchas que puede dar mi primer carro es: {}".format(carro1.marchas))

