
"""MAnejo de archivos"""

tecnologiasBackend = ["Python", "\nJava"]

file = open("my_files/files4.txt", "a+")

file.writelines(tecnologiasBackend)

file = open("my_files/files4.txt", "r")

for newLine in file:
    if newLine.find("Python"):
        print(newLine)
        print("Tienes en tu lista Pyton")


"""Cierre del archivo"""

file.close()


