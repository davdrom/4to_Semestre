#Romero Ramos David Grupo 942
"""

8. Hacer una clase llamada Materia (id, nombre, créditos).
Id no puede ser modificada; créditos debe ser positiva.
Hacer un archivo test que pruebe su funcionamiento.

"""
class Materia:
    def __init__(self, id, nombre, creditos):
        self._id = id
        self.nombre = nombre
        self._creditos = creditos

    @property
    def id(self):
        return self._id

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, valor):
        if valor > 0:
            self._creditos = valor
        else:
            raise ValueError("Los créditos deben ser un valor positivo")
