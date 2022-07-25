"""Programacion orientada a objetos"""
"""Herencia multiple entre clases"""
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

class CarroSedan:

    def __init__(self):
        self.altura = 170

class CarroVolador(Carro, CarroSedan):

    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False

carVolador = CarroVolador("Negro", 50)

"""Herencia del primer padre"""
print("La velocidad inicial de mi carro volador es: {}".format(carVolador.velocidad))

"""Herencia de la segunda clase padre"""
#print("La altura de mi carro volador es: {}".format(carVolador.altura))
