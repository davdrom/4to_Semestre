#Romero Ramos David Grupo 942
"""

3. Crear un menú que realice lo siguiente:
Crear un libro.
Leer libro.
Imprimir información del libro.
Salir.


"""


from Programa_2 import *

libros = []

while True:
    print("--------")
    print("1. Crear libro")
    print("2. Leer libro")
    print("3. Imprimir información del libro actual")
    print("4. Salir")
    o = input("Ingrese una opción: ")

    if o == "1":
        nombre = input("Ingrese el nombre del libro: ")
        propietario = input("Ingrese el nombre del propietario: ")
        libro = Libro(nombre, propietario)
        libros.append(libro)
        print("Libro creado.")
        print(f"Indice: {libros.index(libro)}")

    elif o == "2":
        i = int(input("Ingrese el índice del libro a leer: "))
        libros[i].leer()
        print("Libro leído.")

    elif o == "3":
        i = int(input("Ingrese el índice del libro a imprimir: "))
        print(libros[i])

    elif o == "4":
        print("Saliendo")
        break

    else:
        print("Opción inválida.")