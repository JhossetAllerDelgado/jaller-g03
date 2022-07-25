"""Eejercicio 4"""
"""
4. Crear un programa el cual pueda realizar depositos y extracciones de dinero
reglas:
- El banco va a requerir que al finalizar el dia calcule el dinero que se ha depositado
- crear dos clases, una clase cliente y otra clase banco
- la clase cliente tendra los atributos de nombre y cantidad
- crear los metodos constructor, depositar, extraer, mostrar el total del dinero depositado
- el banco tendra 3 atributos de la clase cliente, el metodo constructor, operar y deposito total
- instanciar para el caso de 3 personas
"""

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Susana")
        self.cliente2 = Cliente("Jorge")
        self.cliente3 = Cliente("Elisabeth")

    def operar(self):
        self.cliente1.depositar(500)
        self.cliente2.depositar(100)
        self.cliente3.depositar(60)

    def depositos(self):
        total = self.cliente1.mostrarCantidad() + self.cliente2.mostrarCantidad() + self.cliente3.mostrarCantidad()
        print("El total de dinero que tiene el banco es: {}".format(total))
        self.cliente1.imprimiDatos()
        self.cliente2.imprimiDatos()
        self.cliente3.imprimiDatos()



class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        if monto > self.cantidad:
            print("No tienes suficiente lado para que retire")
        elif self.cantidad == 0:
            print("No tienes saldo para retirar")
        else:
            self.cantidad -= monto

    def mostrarCantidad(self):
        return self.cantidad

    def imprimiDatos(self):
        print("{} tiene un cantidad depositada de: {}".format(self.nombre, self.cantidad))


banco = Banco()
banco.operar()
banco.depositos()

banco.cliente1.imprimiDatos()








