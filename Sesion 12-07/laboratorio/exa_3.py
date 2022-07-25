"""Eejercicio 3 """
"""
3. Crear un programa que cargue los datos de un triangulo
reglas:
- Crear una classe Triangulo y metodo para iniciar sus atributos
- Crear un metodo para imprimir el valor de un lado con un tamaño mayor
- Crear un metodo para saber que tipo de triangulo es (equilatero isoseles escaleno)
"""

class Triangulo:

    def __init__(self):
        self.lado1 = input("Ingrese el valor del primer lado")
        self.lado2 = input("Ingrese el valor del segundo lado")
        self.lado3 = input("Ingrese el valor del tercer lado")

    def mostrarDatos(self):
        print("Los lados del triangulo tienen los siguientes valores: ")
        print("lado1: {}".format(self.lado1))
        print("lado2: {}".format(self.lado2))
        print("lado3: {}".format(self.lado3))

    def comparar(self):
        print("El lado mayores:")
        if self.lado1 > self.lado2 and self.lado1>self.lado3:
            print("lado 1 con valor es: ".format(self.lado1))
        elif self.lado2 > self.lado3 and self.lado2>self.lado1:
            print("lado 2 con valor es: ".format(self.lado2))
        elif self.lado3 > self.lado2 and self.lado3>self.lado1:
            print("lado 3 con valor es: ".format(self.lado3))
        #elif self.lado3 == self.lado2 or self.lado3 == self.lado1 or self.lado1 == self.lado2 and self.la :
        elif self.lado3 == self.lado2 and self.lado2 != self.lado1:
            print("Hay 2 lados iguales")
        else:
            print("Los tres lados son iguales")

    def tipo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("es un triangulo equilatero")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print("es un triangulo escaleno")
        else:
            print("Es un triangulo isoceles")

figura = Triangulo()
figura.mostrarDatos()
figura.comparar()
figura.tipo()







