#Romero Ramos David Grupo 942

from Programa_10 import User

u = User(1, "David", "david@gmail.com", "contraseña123")
print("ID:", u.id)
print("Nickname:", u.nickname)
print("Email:", u.email)
print("Contraseña:", u.password)
print("Estatus:", u.estatus)

try:
    u.id = 2
except AttributeError as e:
    print("Error:", str(e))

try:
    u.password = "pass"
except ValueError as e:
    print("Error:", str(e))

u.activar()
print("Estatus actualizado:", u.estatus)

u.desactivar()
print("Estatus actualizado:", u.estatus)
