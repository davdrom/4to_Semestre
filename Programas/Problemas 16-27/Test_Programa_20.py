#Romero Ramos David Grupo 942
from Programa_20 import *
try:
    animal1 = Animal("", "Mamífero", 100, 1)
except Exception as e:
    print(e)

try:
    animal2 = Animal("León", "Felino", -10, 2)
except Exception as e:
    print(e)

try:
    animal3 = Animal("Águila", "Ave", 5.5, "3")
except Exception as e:
    print(e)

try:
    animal4 = Animal("Mariposa", "Insecto", 0, 4)
except Exception as e:
    print(e)

try:
    animal5 = Animal("Tigre", "Mamífero", 150, 0)
except Exception as e:
    print(e)

animal6 = Animal("Elefante", "Mamífero", 2000, 5)
print(animal6)