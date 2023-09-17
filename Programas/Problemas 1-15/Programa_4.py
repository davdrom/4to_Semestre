#Romero Ramos David Grupo 942
"""

4. Crear una clase Triangulo. La cúal debe tener como atributos cada uno de sus lados.
Realizar dos métodos : perímetro y área. Probar este objeto y sus acciones.

"""

import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
