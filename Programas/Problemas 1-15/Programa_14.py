#Romero Ramos David Grupo 942
"""

14. Gestión de un Zoológico.  Desarrollar la siguiente jerarquía de clases que representa los animales de un posible zoológico:

La clase Animal es una clase abstracta con cuatro atributos protected (_NombreAtributo no usar doble guión bajo):
a) Una cadena indicando la especie (león, águila, abeja),
b) Una cadena indicando el nombre del animal concreto
c) Un dato numérico real indicando el peso en kg.
d) Un dato numérico entero indicando el número de jaula que se asigna al animal.

Además, la clase Animal declara un método abstracto DefinirClaseDeAnimalEres(); el cuál retorna una cadena.  Recuerde que habrá que sobrescribir este método en las clases derivadas.

La clase Mamífero no añade nuevos atributos, aunque deberá implementar el método DefinirClaseDeAnimalEres().

La clase Ave tiene dos nuevos atributos protected (_NombreAtributo no usar doble guión bajo):
a) Una cadena colorPlumaje indicando el color predominante
b) Un dato numérico real indicando la alturaMaximaVuelo.

La clase Insecto tiene un nuevo atributo protected de tipo booleano llamado vuela que indica si el insecto vuela o no.


"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, nombre, peso, numJaula):
        self.especie = especie
        self.nombre = nombre
        self.peso = peso
        self.numJaula = numJaula

    @abstractmethod
    def DefinirClaseDeAnimalEres(self):
        pass

    def __str__(self):
        return f"Mamífero: {self.nombre}, Especie: {self.especie}, Peso: {self.peso} kg, Número de jaula: {self.numJaula}"

class Mamifero(Animal):
    def DefinirClaseDeAnimalEres(self):
        return "Soy un mamífero."



class Ave(Animal):
    def __init__(self, especie, nombre, peso, numJaula, colPlumaje, vueloMax):
        super().__init__(especie, nombre, peso, numJaula)
        self.colPlumaje = colPlumaje
        self.vueloMax = vueloMax

    def DefinirClaseDeAnimalEres(self):
        return "Soy un ave."

    def __str__(self):
        return f"Ave: {self.nombre}, Especie: {self.especie}, Peso: {self.peso} kg, Número de jaula: {self.numJaula}, Color de plumaje: {self.colPlumaje}, Altura máxima de vuelo: {self.vueloMax} m"


class Insecto(Animal):
    def __init__(self, especie, nombre, peso, numJaula, vuela):
        super().__init__(especie, nombre, peso, numJaula)
        self.vuela = vuela

    def DefinirClaseDeAnimalEres(self):
        return "Soy un insecto."

    def __str__(self):
        return f"Insecto: {self.nombre}, Especie: {self.especie}, Peso: {self.peso} kg, Número de jaula: {self.numJaula}, Vuela: {self.vuela}"
