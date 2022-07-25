"""manejo de archivos"""
"""w: Abre el archivo para poder escribir sobre el"""
file = open("my_files/files2.txt", "w")
file.write("lenguaje multiplataforma\n")
file.write("esta basado en POOO\n")
file.write(("Python es completame nte intuitivo"))

file = open("my_files/files2.txt", "r")

print("nuestro file tiene el siguiente contenido: {}".format(file.read()))

"""cierre el archivo"""

file.close()



