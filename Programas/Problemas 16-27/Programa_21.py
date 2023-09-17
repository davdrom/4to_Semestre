#Romero Ramos David Grupo 942
"""
21. Crear una clase llamada libro, la cual contenga los atributos nombre, año de edición, autor, realizar los métodos
set, get y validaciones que considere pertinentes.  Nota: Puede agregar más atributos si lo considera necesario.
No olvide sobreescribir el método __str__.
"""
class Libro:
    def __init__(self, nombre, año_edicion, autor):
        self.nombre = nombre
        self.año_edicion = año_edicion
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.nombre}\nAño de edición: {self.año_edicion}\nAutor: {self.autor}"

    def validar_nombre(self):
        if not isinstance(self.nombre, str) or len(self.nombre) == 0:
            raise ValueError("El nombre del libro debe ser una cadena no vacía.")

    def validar_año_edicion(self):
        if not isinstance(self.año_edicion, int) or self.año_edicion < 0:
            raise ValueError("El año de edición debe ser un número entero no negativo.")

    def validar_autor(self):
        if not isinstance(self.autor, str) or len(self.autor) == 0:
            raise ValueError("El nombre del autor debe ser una cadena no vacía.")

    def validar_atributos(self):
        self.validar_nombre()
        self.validar_año_edicion()
        self.validar_autor()
