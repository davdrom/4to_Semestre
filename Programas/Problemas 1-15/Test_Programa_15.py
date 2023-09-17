#Romero Ramos David Grupo 942

from Programa_15 import *
zoo = Zoologico()

a1 = Mamifero("Leon", "D", 1, 11)
a2 = Ave("Cuervo", "D", 1, 22, "Negro", 222)
a3 = Insecto("Mosca", "D", 3, 33, True)

zoo.agregar_animal(a1)
zoo.agregar_animal(a2)
zoo.agregar_animal(a3)

zoo.editar_animal("D", "D1", 111, 1111)
zoo.eliminar_animal("D1")
zoo.imprimir_informacion_animal("D")

print("Número total de animales:", zoo.numero_total_animales())

print("Número de mamíferos:", zoo.numero_animales_clase(Mamifero))
print("Número de aves:", zoo.numero_animales_clase(Ave))
print("Número de insectos:", zoo.numero_animales_clase(Insecto))

print("Promedio de peso de mamíferos:", zoo.promedio_peso_clase(Mamifero))
print("Promedio de peso de aves:", zoo.promedio_peso_clase(Ave))
print("Promedio de peso de insectos:", zoo.promedio_peso_clase(Insecto))
