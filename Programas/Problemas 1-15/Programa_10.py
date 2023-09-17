#Romero Ramos David Grupo 942
"""

10. Hacer una clase User(id, nickname, email, password, status). Validar que el password tenga 8 caracteres o más. Id no se puede modificar.

"""
class User:
    def __init__(self, id, nickname, email, password, estatus=False):
        self._id = id
        self.nickname = nickname
        self.email = email
        self._password = password
        self.estatus = estatus


    @property
    def id(self):
        return self._id

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, valor):
        if len(valor) >= 8:
            self._password = valor
        else:
            raise ValueError("La contraseña debe tener 8 caracteres o más")

    def activar(self):
        self.estatus = True

    def desactivar(self):
        self.estatus = False
