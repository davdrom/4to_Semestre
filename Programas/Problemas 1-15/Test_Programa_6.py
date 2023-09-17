#Romero Ramos David Grupo 942

from Programa_6 import Persona

p = Persona("David", 20)
print("Nombre:", p.nombre)
print("Edad:", p.edad)

try:
    p.edad = -10
except ValueError as e:
    print("Error:", str(e))

p.cumplir_anios()
print("Edad actualizada:", p.edad)
