"""Uso de librerias JSON para tratar tipos de dato JSON"""

"""Importamos la libreria JSON"""
import json

pythonDict = {"name": "Mary", "edad": 28, "dni": "70178110"}

"""Conversion de tipo dato a JSON: dumps()"""

dictToJson = json.dumps(pythonDict)
print("El dato convertido a JSON es el siguiente: {}".format(dictToJson))
print("El tipo de dato convertido es de tipo: {}".format(type(dictToJson)))




