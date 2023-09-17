#Romero Ramos David Grupo 942
"""

1. Modificar la clase Persona realizada en clase la cual contiene los atributos nombre, edad.
Agregar un método a la clase llamada cumplir años que agregue uno más a la edad.
Cada vez que se mande a llamar al método se debe incrementar la edad en uno.
Probar esta modificación llamando a la acción e imprimir la edad en varias ocasiones.

"""

class Persona:

    def __init__(self, nombre, edad, ):
        self.nombre = nombre
        self.edad = edad

    def Caminar(self):
        print("Yo", self.nombre, "estoy caminando")

    def cumplir_años(self):
        self.edad += 1

    def __str__(self):
        return self.nombre + " " + str(self.edad)
