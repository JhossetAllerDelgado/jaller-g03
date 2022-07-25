"""Eejercicio 2"""
"""
2. Crear un programa que tenga la clase Persona
reglas:
- La clase tendra como atributos el nombre y la edad de una persona 
- Implementar los metodos para inicializar los atributos
- Implementar un metodo para mostrar e indicar si la persona es mayor  de edad 
"""
class Persona():
    """Inicializar los atributos en el constructor"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarDatos(self):
        print("Su nombre es: {}".format(self.nombre))
        print("Y su edad es: {}".format(self.edad))

    def mayoEdad (self):
        if self.edad >=18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

persona1 = Persona("Ivana", 25)
persona2 = Persona("Carlos", 16)

"""Imprimiendo el resultado si es mayor de edad o no"""
persona1.mostrarDatos()
persona1.mayoEdad()

persona2.mostrarDatos()
persona2.mayoEdad()







