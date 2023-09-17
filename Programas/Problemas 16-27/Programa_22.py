#Romero Ramos David Grupo 942
"""
22. Crear una clase llamada ItemLibro que contenga dos atributos: libro: Libro y cantidad de copias de dicho libro.
Agregue los métodos set, get y validaciones que considere pertinentes. No olvide sobreescribir el método __str__
"""
from Programa_21 import *
class ItemLibro:
    def __init__(self, libro, cantidad):
        self.libro = libro
        self.cantidad = cantidad
        self.validar_atributos()

    def __str__(self):
        return f"Libro: {self.libro}\nCantidad: {self.cantidad}"

    def validar_atributos(self):
        if not isinstance(self.libro, Libro):
            raise ValueError("El atributo 'libro' debe ser un objeto de la clase Libro.")

        if not isinstance(self.cantidad, int) or self.cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero no negativo.")



