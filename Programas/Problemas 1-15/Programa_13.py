#Romero Ramos David Grupo 942
"""

13. Un banco requiere controlar las cuentas de sus clientes y para ello las clasifica en dos: cheques y ahorros.  Todas las cuentas del banco tienen los siguientes datos (atributos):
• Número de cuenta (entero).
• Nombre del cliente (cadena).
• Saldo (numérico real).
Además se realizan las siguientes operaciones con ellas:
• Consultar datos: A través de sus propiedades (atributos).
• Depositar: Incrementa el saldo con la cantidad de dinero que se deposita.
• Retirar: Antes de hacer el retiro, se debe verificar la suficiencia de saldo y en caso de aprobarlo, se disminuye el saldo.

 Las cuentas de ahorros presentan las siguientes características:
• Fecha de vencimiento (atributo).
• Porcentaje de interés mensual (atributo).
• Método para depositar los intereses el primer día de cada mes. (Sobre escribir método depositar)
• Solamente se puede retirar dinero el día de la fecha de vencimiento (Sobre escribir método retirar)

Las cuentas de cheques presentan las siguientes características:
• Comisión por uso de chequera (atributo).
• Comisión por emisión de cheques con saldo insuficiente (atributo).
• Método de retirar, se ejecuta cuando alguien cobra un cheque emitido por la cuenta. Se debe verificar la suficiencia de saldo, en caso de aprobarlo se disminuye saldo incluyendo la comisión por uso de chequera; en caso contrario solo se disminuye la comisión por emisión de cheques con saldo insuficiente pero no se retira el dinero por falta de fondos. (Sobre escribir método retirar)

Sobreescriba el método __str__ para mostrar los datos de cada tipo de objeto. NOTA: Realizar un archivo test que pruebe el funcionamiento, de todas las clases.


"""
from datetime import *
class Cuenta:
    def __init__(self, numero_cuenta, nombre_cliente, saldo):
        self.numero_cuenta = numero_cuenta
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo

    def consultar_datos(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Nombre del cliente:", self.nombre_cliente)
        print("Saldo:", self.saldo)

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro exitoso.")
        else:
            print("Saldo insuficiente para retirar.")

    def __str__(self):
        return f"Cuenta\nNúmero de cuenta: {self.numero_cuenta}\nNombre del cliente: {self.nombre_cliente}\nSaldo: {self.saldo}"


class CuentaAhorros(Cuenta):
    def __init__(self, numero_cuenta, nombre_cliente, saldo, fecha_vencimiento, interes_mensual):
        super().__init__(numero_cuenta, nombre_cliente, saldo)
        self.fecha_vencimiento = fecha_vencimiento
        self.interes_mensual = interes_mensual

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.fecha_vencimiento == datetime.now().date():
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print("Retiro exitoso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("No se puede retirar dinero antes de la fecha de vencimiento.")

    def __str__(self):
        return f"Cuenta de Ahorros\nNúmero de cuenta: {self.numero_cuenta}\nNombre del cliente: {self.nombre_cliente}\nSaldo: {self.saldo}\nFecha de vencimiento: {self.fecha_vencimiento}\nInterés mensual: {self.interes_mensual}"


class CuentaCheques(Cuenta):
    def __init__(self, numero_cuenta, nombre_cliente, saldo, comision_chequera, comision_saldo_insuficiente):
        super().__init__(numero_cuenta, nombre_cliente, saldo)
        self.comision_chequera = comision_chequera
        self.comision_saldo_insuficiente = comision_saldo_insuficiente

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            self.saldo -= self.comision_chequera
            print("Retiro exitoso.")
        else:
            self.saldo -= self.comision_saldo_insuficiente
            print("Saldo insuficiente.")

    def __str__(self):
        return f"Cuenta de Cheques\nNúmero de cuenta: {self.numero_cuenta}\nNombre del cliente: {self.nombre_cliente}\nSaldo: {self.saldo}\nComisión por uso de chequera: {self.comision_chequera}\nComisión por emisión de cheques con saldo insuficiente: {self.comision_saldo_insuficiente}"
