#Romero Ramos David Grupo 942
"""

7. Realizar una clase Profesor (id, nombre, edad, salario, carrera). La edad y el salario deben ser positivos.
El id no se puede modificar. Hacer un archivo test que pruebe su funcionamiento.
"""
class Profesor:
    def __init__(self, id, nombre, edad, salario, carrera):
        self._id = id
        self.nombre = nombre
        self._edad = edad
        self._salario = salario
        self.carrera = carrera


    @property
    def id(self):
        return self._id

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor > 0:
            self._edad = valor
        else:
            raise ValueError("La edad debe ser un valor positivo")

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor > 0:
            self._salario = valor
        else:
            raise ValueError("El salario debe ser un valor positivo")
