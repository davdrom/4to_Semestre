#Romero Ramos David Grupo 942
"""

5. Modificar la clase Triangulo del problema 4. Agregar un atributo número de lados para que siempre su valor sea 3.
No se puede modificar este atributo solo leer. Hacer un archivo test que pruebe su funcionamiento.
"""
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self._nlados = 3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        s = self.perimetro() / 2
        return (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5

    @property
    def nlados(self):
        return self._nlados
