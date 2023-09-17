#Romero Ramos David Grupo 942
"""

12. Crear clase abstracta Operación (nombre, número de operadores). Debe tener un método abstracto llamado evaluar.
Crear 3 clases hijas de Operación llamadas Suma, Resta, Multiplicar.
Deben sobreescribir el método llamado evaluar para que retorne el resultado correspondiente. Crear archivo test.

"""

class Operacion:
    def __init__(self, nombre, num_operadores):
        self.nombre = nombre
        self.num_operadores = num_operadores

    def evaluar(self):
        raise NotImplementedError("El método evaluar debe ser implementado en las clases hijas")


class Suma(Operacion):
    def __init__(self, operador1, operador2):
        super().__init__("Suma", 2)
        self.operador1 = operador1
        self.operador2 = operador2

    def evaluar(self):
        return self.operador1 + self.operador2


class Resta(Operacion):
    def __init__(self, operador1, operador2):
        super().__init__("Resta", 2)
        self.operador1 = operador1
        self.operador2 = operador2

    def evaluar(self):
        return self.operador1 - self.operador2


class Multiplicar(Operacion):
    def __init__(self, operador1, operador2):
        super().__init__("Multiplicación", 2)
        self.operador1 = operador1
        self.operador2 = operador2

    def evaluar(self):
        return self.operador1 * self.operador2
