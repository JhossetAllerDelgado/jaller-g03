""""Problema 1"""

""" 
-Pedir al usuario su email y mostrarlo en la panrtalla indicando que es su direccion
-Validar si es una direccion de correo electronico
-El email se considerara si tiene el simbolo del '@'
"""
def validar(email):
   caracterPedido = "@"
    for letra in email:
    if letra == caracterPedido:
       return True
    return False

emailUsuario = input("Ingrese su email por  favor: ")

if validar(emailUsuario):
    print("Email valido")
else:
    print("Email incorrecto")




