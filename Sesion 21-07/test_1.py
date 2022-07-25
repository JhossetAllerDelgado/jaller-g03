"""Uso de librerias JSON para tratar tipos de dato JSON"""

"""Importamos la libreria JSON"""
import json
"""creando nuestra variable con un tipo de dato JSON"""
jsonData = '{"nombre": "Pyton", "Tipo": "Backend", "paradigma": "POO"}'
"""Convertimos a un dato que pueda manejar Python: loads()"""
jsonToPython = json.loads(jsonData)
print("Nuestros datos de tipo JSON a dato python: {}".format(jsonToPython))
print(jsonToPython['paradigma'])
print("El tipo de dato de nuestra variable es: {}".format(type(jsonToPython)))


