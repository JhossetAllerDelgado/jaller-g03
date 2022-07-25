"""
1. Escriba un programa donde tendrá los siguientes requisitos:
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato)
- Un método cumpleaños donde cada vez que invoque aumentará en un año la
edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla)
"""

class Persona():

    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def mostrarDatos(self):
        print("Su nombre es: {}".format(self.nombre))
        print("Y su edad es: {}".format(self.edad))
        print("Y su nacionalidad es: {}".format(self.nacionalidad))

    def cumpleaños (self):

        self.persona1.cumpleaños("27/05/1996")


persona1 = Persona("Jose", 30, "peruano")


persona1.mostrarDatos()
persona1.cumpleaños()



