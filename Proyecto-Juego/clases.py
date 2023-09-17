class Personaje:
    def __init__(self, nombre, salud, ataque, defensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.ataque_s = ataque*2

    def recibir_danio(self, danio):
        danio_recibido = max(danio - self.defensa, 0)
        self.salud -= danio_recibido
        if not self.salud > 0:
            self.salud = 0

    def esta_vivo(self):
        return self.salud > 0

class Jugador(Personaje):
    def __init__(self, nombre, salud, ataque, defensa, imagen):
        super().__init__(nombre, salud, ataque, defensa)
        self.imagen = imagen
        self.inventario = []

    def agregar_objeto(self, objeto):
        self.inventario.append(objeto)
        self.ataque += objeto.valor_ataque
        self.defensa += objeto.valor_defensa


class Enemigo(Personaje):
    def __init__(self, nombre, salud, ataque, defensa, objeto, imagen, historia):
        super().__init__(nombre, salud, ataque, defensa)
        self.objeto = objeto
        self.imagen = imagen
        self.historia = historia

class Objeto:
    def __init__(self, nombre, valor_ataque, valor_defensa):
        self.nombre = nombre
        self.valor_ataque = valor_ataque
        self.valor_defensa = valor_defensa