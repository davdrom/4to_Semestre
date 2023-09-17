#Romero Ramos David Grupo 942

from Programa_11 import *

a = Administrador(1, "admin1", "admin1@ggg.com", "contraseniaa", "Grupo1", 10)
print("ID:", a.id)
print("Nickname:", a.nickname)
print("Email:", a.email)
print("Contraseña:", a.password)
print("Estatus:", a.estatus)
print("Nombre de grupo:", a.nombre_grupo)

i = Integrante(2, "user1", "user1@ggg.com", "contraseniaaa", "Grupo2")
print("ID:", i.id)
print("Nickname:", i.nickname)
print("Email:", i.email)
print("Contraseña:", i.password)
print("Estatus:", i.estatus)
print("Nombre de grupo:", i.nombre_grupo)

a.dar_baja(i)
print("Estatus actualizado:", i.estatus)

a.dar_alta(i)
print("Estatus actualizado:", i.estatus)

i.dar_alta_grupo("Grupo3")
print("Nombre de grupo actualizado:", i.nombre_grupo)

i.dar_baja_grupo()
print("Nombre de grupo actualizado:", i.nombre_grupo)
