#Romero Ramos David Grupo 942
"""
19. Modificar el problema 13, para incluir excepciones haciendo uso de la palabra reservada raise, al menos debe incluir las siguientes excepciones
(Nota: No es necesario realizar sus propias clases que heredan de Exception):

Saldo debe ser mayor o igual a cero, recuerde validar en el constructor , realizar un método set  y realizar la validación.
En la clase cuenta , los métodos retirar y depositar verificar que la cantidad sea mayor a 0. En caso contrarió lanzar una excepción.
En la clase de cuenta de ahorros el porcentaje de interés mensual (atributo) debe ser mayor o igual a 0.
 En la clase de cuenta de ahorros en el método retirar si el día es diferente a la fecha vencimiento lanzar una excepción.
En la clase de cuenta de cheques los atributos Comisión por uso de chequera y Comisión por emisión de cheques con saldo insuficiente deben ser mayor a cero.

Realizar un archivo test que pruebe el funcionamiento de todas estas excepciones.

"""

from datetime import *

class Cuenta:
    def __init__(self, numero_cuenta, nombre_cliente, saldo):
        self.numero_cuenta = numero_cuenta
        self.nombre_cliente = nombre_cliente
        self.saldo = self.validar_saldo(saldo)

    def validar_saldo(self, saldo):
        if saldo < 0:
            raise ValueError("El saldo debe ser mayor o igual a cero")
        return saldo

    def consultar_datos(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Nombre del cliente:", self.nombre_cliente)
        print("Saldo:", self.saldo)

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor a cero")
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor a cero")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
        print("Retiro exitoso.")

    def __str__(self):
        return f"Cuenta\nNúmero de cuenta: {self.numero_cuenta}\nNombre del cliente: {self.nombre_cliente}\nSaldo: {self.saldo}"


class CuentaAhorros(Cuenta):
    def __init__(self, numero_cuenta, nombre_cliente, saldo, fecha_vencimiento, interes_mensual):
        super().__init__(numero_cuenta, nombre_cliente, saldo)
        self.fecha_vencimiento = fecha_vencimiento
        self.interes_mensual = self.validar_interes(interes_mensual)

    def validar_interes(self, interes):
        if interes < 0:
            raise ValueError("El interés mensual debe ser mayor o igual a cero")
        return interes

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor a cero")
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.fecha_vencimiento != datetime.now().date():
            raise ValueError("No se puede retirar dinero antes de la fecha de vencimiento")
        super().retirar(cantidad)

    def __str__(self):
        return f"Cuenta de Ahorros\nNúmero de cuenta: {self.numero_cuenta}\nNombre del cliente: {self.nombre_cliente}\nSaldo: {self.saldo}\nFecha de vencimiento: {self.fecha_vencimiento}\nInterés mensual: {self.interes_mensual}"


class CuentaCheques(Cuenta):
    def __init__(self, numero_cuenta, nombre_cliente, saldo, comision_chequera, comision_saldo_insuficiente):
        super().__init__(numero_cuenta, nombre_cliente, saldo)
        self.comision_chequera = self.validar_comision(comision_chequera)
        self.comision_saldo_insuficiente = self.validar_comision(comision_saldo_insuficiente)

    def validar_comision(self, comision):
        if comision <= 0:
            raise ValueError("La comisión debe ser mayor a cero")
        return comision

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor a cero")
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor a cero")
        if cantidad > self.saldo:
            self.saldo -= self.comision_saldo_insuficiente
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
        self.saldo -= self.comision_chequera
        print("Retiro exitoso.")

    def __str__(self):
        return f"Cuenta de Cheques\nNúmero de cuenta: {self.numero_cuenta}\nNombre del cliente: {self.nombre_cliente}\nSaldo: {self.saldo}\nComisión por uso de chequera: {self.comision_chequera}\nComisión por emisión de cheques con saldo insuficiente: {self.comision_saldo_insuficiente}"
