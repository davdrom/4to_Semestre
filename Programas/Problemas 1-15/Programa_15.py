#Romero Ramos David Grupo 942
"""

15. Crear una clase zoológico que contenga como atributo una lista de animales usando la jerarquía de clases del problema anterior. Esta clase debe tener los siguiente métodos:
Agregar un nuevo animal.
Editar información de un animal en específico.
Eliminar un animal.
Imprimir información de un animal
Número total de animales.
Número de animales de cada clase (Mamífero, Ave, Insecto).
Promedio de peso de cada clase (Mamífero, Ave, Insecto.


"""
from Programa_14 import *
class Zoologico:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def editar_animal(self, nombre, nuevo_nombre, nuevo_peso, nuevo_num_jaula):
        for animal in self.animales:
            if animal.nombre == nombre:
                animal.nombre = nuevo_nombre
                animal.peso = nuevo_peso
                animal.numJaula = nuevo_num_jaula
                break

    def eliminar_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                self.animales.remove(animal)
                break

    def imprimir_informacion_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                print("Información del animal:")
                print("Especie:", animal.especie)
                print("Nombre:", animal.nombre)
                print("Peso:", animal.peso)
                print("Número de jaula:", animal.numJaula)
                break
        else:
            print("No se encontró el animal con ese nombre.")

    def numero_total_animales(self):
        return len(self.animales)

    def numero_animales_clase(self, clase):
        count = 0
        for animal in self.animales:
            if isinstance(animal, clase):
                count += 1
        return count

    def promedio_peso_clase(self, clase):
        total_peso = 0
        count = 0
        for animal in self.animales:
            if isinstance(animal, clase):
                total_peso += animal.peso
                count += 1
        if count > 0:
            return total_peso / count
        else:
            return 0