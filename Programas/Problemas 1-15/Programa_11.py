#Romero Ramos David Grupo 942
"""

11. Crear dos clases Administrador e Integrante, las cuales heredan de User (Problema 10).
Administrador (nombre grupo, cantidad usuarios) debe tener las acciones dar baja (cambia estatus a False a un integrante,
y pone nombre grupo del integrante a vacío), dar alta (cambia Estatus a True a un integrante y pone nombre de grupo del integrante igual al del administrador).
El Integrante (nombre grupo) debe tener las acciones dar alta en un grupo y dar de baja en un grupo.
Los cuales reciben como parámetro un objeto de tipo Administrador, para simular una petición de que están interesados o no a unirse.
Crear un archivo Test que verifique el proceso.


"""
from Programa_10 import *

class Administrador(User):
    def __init__(self, id, nickname, email, password, nombre_grupo, cantidad_usuarios, estatus=False):
        super().__init__(id, nickname, email, password, estatus)
        self.nombre_grupo = nombre_grupo
        self.cantidad_usuarios = cantidad_usuarios

    def dar_baja(self, usuario):
        usuario.desactivar()

    def dar_alta(self, usuario):
        usuario.activar()


class Integrante(User):
    def __init__(self, id, nickname, email, password, nombre_grupo, estatus=False):
        super().__init__(id, nickname, email, password, estatus)
        self.nombre_grupo = nombre_grupo

    def dar_alta_grupo(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo

    def dar_baja_grupo(self):
        self.nombre_grupo = ""