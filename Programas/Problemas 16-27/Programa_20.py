#Romero Ramos David Grupo 942
"""
20. Analizar la clase Animal realizada en el problema 14. Listar qué atributos pueden ser validados usando excepciones.
Después de esto realizar sus propias excepciones usando clases que heredan de Exception.
Modificar la clase Animal para lanzar las excepciones realizadas. Para finalizar haga un archivo test que pruebe el funcionamiento de todas las excepciones.
"""
class NombreInvalidoException(Exception):
    def __init__(self, mensaje="El nombre del animal es inválido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class TipoAnimalInvalidoException(Exception):
    def __init__(self, mensaje="El tipo de animal es inválido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class PesoInvalidoException(Exception):
    def __init__(self, mensaje="El peso del animal es inválido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class NumJaulaInvalidoException(Exception):
    def __init__(self, mensaje="El número de jaula es inválido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class Animal:
    def __init__(self, nombre, tipo_animal, peso, numJaula):
        if not nombre or not nombre.strip():
            raise NombreInvalidoException()
        self.nombre = nombre

        if tipo_animal not in ["Mamífero", "Ave", "Insecto"]:
            raise TipoAnimalInvalidoException()
        self.tipo_animal = tipo_animal

        if not isinstance(peso, (int, float)) or peso <= 0:
            raise PesoInvalidoException()
        self.peso = peso

        if not isinstance(numJaula, int) or numJaula <= 0:
            raise NumJaulaInvalidoException()
        self.numJaula = numJaula

    def __str__(self):
        return f"Animal: {self.nombre} - Tipo: {self.tipo_animal} - Peso: {self.peso} - Jaula: {self.numJaula}"
