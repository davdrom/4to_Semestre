#Romero Ramos David Grupo 942
"""

9. Hacer una clase abstracta Figura que tenga nombre, número de lados, y  dos métodos abstractos perímetro y área.
Crear dos clases rectángulo, pentágono que hereden de la clase Figura. Poner atributos para sus lados y sobreescribir los métodos area y perimetro (Retornan los resultados).
Hacer un test que pruebe el funcionamiento.
"""
import math

class Figura:
    def __init__(self, *lados):
        self.lados = lados

    def area(self):
        pass

    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Pentagono(Figura):
    def __init__(self, lado):
        super().__init__(lado)
        self.lado = lado

    def area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.lado**2

    def perimetro(self):
        return 5 * self.lado
