#Romero Ramos David Grupo 942
"""

6. Crear una clase Persona (nombre, edad), puede ser la clase del Problema 1.
Modificar para que la edad pueda ser modificada pero no puede tener valores negativos o ceros.
Hacer un archivo test que pruebe su funcionamiento.

"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor > 0:
            self._edad = valor
        else:
            raise ValueError("La edad debe ser un valor positivo")

    def cumplir_anios(self):
        self.edad += 1
