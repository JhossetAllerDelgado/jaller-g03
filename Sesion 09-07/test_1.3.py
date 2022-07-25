"""Programacion orientada a objetos"""
"""Herencia entre clases"""
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

"""Aplicando herencia"""
"""Creando nuestra clase hija"""
class CarroVolador(Carro):
    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False

carro1 = Carro("Rojo", 30)
carVolador = CarroVolador("Blanco", 40)

print("El color del carro volador es: {}".format(carVolador.color))
print("La aceleracion de mi carro volador es: {}".format(carVolador.aceleracion))
print("La velocidad inicial de mi carro volador es: {}".format(carVolador.aceleracion))
"""Aqui aplicamos el efecto de herencia al usar el metodo de clase padre Carro"""

carVolador.acelera()
carVolador.acelera()

print("La velocidad actual de mi carro volador es: {}".format(carVolador.velocidad))

#rint("El estado de vuelo de mi carro 1 es: {}".format(carro1.estadoVolando))


