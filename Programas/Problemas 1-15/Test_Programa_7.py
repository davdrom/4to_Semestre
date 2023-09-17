#Romero Ramos David Grupo 942

from Programa_7 import Profesor

p = Profesor(1, "David", 20, 100, "IN")
print("ID:", p.id)
print("Nombre:", p.nombre)
print("Edad:", p.edad)
print("Salario:", p.salario)
print("Carrera:", p.carrera)

try:
    p.id = 2
except AttributeError as e:
    print("Error:", str(e))

try:
    p.edad = -10
except ValueError as e:
    print("Error:", str(e))


p.salario += 1000
print("Salario actualizado:", p.salario)
