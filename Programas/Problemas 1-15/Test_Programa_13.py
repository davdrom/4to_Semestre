#Romero Ramos David Grupo 942

from Programa_13 import *
cA = CuentaAhorros(1001, "DAVID", 5000, datetime(2023, 5, 31), 0.03)
cC = CuentaCheques(2001, "ROMERO", 8000, 10, 20)


print(cA)
print(cC)

cA.depositar(1000)
cC.depositar(1500)
cA.retirar(2000)
cC.retirar(5000)

print(cA)
print(cC)