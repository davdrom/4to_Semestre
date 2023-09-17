#Romero Ramos David Grupo 942

from Programa_8 import Materia

m = Materia(1, "Programacion", 4)
print("ID:", m.id)
print("Nombre:", m.nombre)
print("Créditos:", m.creditos)


try:
    m.id = 2
except AttributeError as e:
    print("Error:", str(e))


try:
    m.creditos = -2
except ValueError as e:
    print("Error:", str(e))

# Incrementar los créditos en 2
m.creditos += 2
print("Créditos actualizados:", m.creditos)
