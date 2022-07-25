"""
realizar un programa que contenga una clase llamada alumno
Reglas:
- debe de tener los atributos nombre y nota para alumno
- definir los metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota
- mostrar en el mensaje si el alumno aprobo o no
"""
class Alumno:
    """inicializar los atributos"""
    def __int__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    """Metodo para imprimir datos"""
    def imprimir(self):
        print("Nombre del alumno: {}".format(self.nombre))
        print("Nota: {}".format(self.nota))

    """Metodo para imprimir los datos"""
    def resultado(self):
        if self.nota < 11:
            print("El alumno ha desaprobado el curso")
        else:
            print("El alumno aprobo")

"""Creando las nuevas instancias"""
alumno1 = Alumno("Luis", 9)
alumno2 = Alumno("Sebas", 17)

alumno1.imprimir()
alumno1.resultado()







