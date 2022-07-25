"""Manejo de archivos"""
"""Apertura y lectura de archivos"""

"""r: Abre el archivo en modo lectura"""

file = open("../my_files/files.txt", "r")
#file2 = open("files.docx", "r")
"""read(): nos permite leer el contenido del archivo"""
print("Ccontenido de nuestro archivo 'files': {}".format(file.read()))


