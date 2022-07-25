"""
2. Usando el concepto de herencia y encapsulación (para saldo) para crear el
siguiente programa:
Reglas:
- Agregar un atributo saldo a la clase persona.
- Crear un método transferencia(self, persona2, monto)
- El saldo deberá representar el dinero que tiene la otra persona
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”
"""

class Persona():

    def __init__(self, persona2, monto):
        self.persona2 = persona2
        self.monto = monto
        self.saldo = 500


    def transferir(self, monto):
        self.cantidad += monto

    def transaccion(self, monto):
        if monto > self.cantidad:
            print("No tienes suficiente saldo para tranferir")
        elif self.cantidad == 0:
            print("No tienes saldo para transferir")
        else:
            self.cantidad -= monto

    def mostrarCantidad(self):
        return self.cantidad

    def imprimiDatos(self):
        print("{} tiene un cantidad depositada de: {}".format(self.persona2, self.cantidad))



