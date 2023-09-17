#Romero Ramos David Grupo 942
"""

2. Crear una clase Libro debe tener dos atributos propietario y leído (False si no se ha leído, True en caso contrario).
Realizar una acción leer que modifique el atributo leído a True.
Realizar un archivo  test donde cree 3 libros y pruebe la acción llamada leer.

"""

class Libro:
    def __init__(self, nombre, propietario):
        self.nombre = nombre
        self.propietario = propietario
        self.leido = False

    def leer(self):
        self.leido = True

    def __str__(self):
        estado = "leído" if self.leido else "no leído"
        return f"Libro: {self.nombre}, Propietario: {self.propietario}, Estado: {estado}"
