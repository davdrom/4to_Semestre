#Romero Ramos David Grupo 942
from Programa_19 import *

cuenta1 = Cuenta("1234567890", "D", 1000)
print(cuenta1)

cuenta1.depositar(200)
cuenta1.retirar(500)
print(cuenta1)

fecha_vencimiento = date(2023, 6, 1)
cuenta_ahorros = CuentaAhorros("0987654321", "A", 5000, fecha_vencimiento, 0.05)
print(cuenta_ahorros)

cuenta_ahorros.depositar(1000)
cuenta_ahorros.retirar(2000)
print(cuenta_ahorros)

cuenta_cheques = CuentaCheques("246813579", "V", 2000, 10, 50)
print(cuenta_cheques)

cuenta_cheques.depositar(500)
cuenta_cheques.retirar(1000)
print(cuenta_cheques)
