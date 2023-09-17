#Romero Ramos David Grupo 942


from Programa_5 import *

t1 = Triangulo(1, 1, 1)
t2 = Triangulo(2, 2, 2)
t3 = Triangulo(3, 3, 3)

print("Perímetro 1:", t1.perimetro())
print("Perímetro 2:", t2.perimetro())
print("Perímetro 3:", t3.perimetro())

print("Área 1:", t1.area())
print("Área 2:", t2.area())
print("Área 3:", t3.area())

try:
    t1.nlados = 4
except:
    print("No se puede modificar el numero de lados")

print("Número de lados 1:", t1.nlados)
print("Número de lados 2:", t2.nlados)
print("Número de lados 3:", t3.nlados)
