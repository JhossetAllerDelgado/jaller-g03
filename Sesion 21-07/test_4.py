
"""manejo de archivos"""
tecnologiasBackend = ["\nPython ", "Java ", "Ruby ", "NodeJS "]
tecnologiasFrontend = ["\nAngular ", "JavaScript ", "ReactJS", "Boostrap"]

"""Apertura de nuestro archivo"""
"""a+: Permite escribir varias lineas al abrir nuestro archivo"""
"""a+: Escribe nuevas lineas de texto sin sobreescribir en contenido del archivo"""

file = open("my_files/files3.txt", "a+")
file.writelines(tecnologiasBackend)
file.writelines(tecnologiasFrontend)

file = open("my_files/files3.txt")
print("El contenido de mi archivoes: {}".format(file.read()))

"""Cierre del archivo"""
file.close()




