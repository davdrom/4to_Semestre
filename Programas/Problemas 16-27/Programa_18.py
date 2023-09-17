#Romero Ramos David Grupo 942
"""
18. Modificar el problema 16, para incluir el control de excepciones listados en el problema anterior para que la
aplicación siempre se encuentre en funcionamiento. Recuerde imprimir mensajes expresivos  al usuario que le permitan
saber qué acciones está realizando de manera incorrecta.
"""

from Programa_14 import *
from Programa_15 import Zoologico

def mostrar_menu():
    print("----- MENU -----")
    print("1. Dar de alta un nuevo animal")
    print("2. Editar un animal")
    print("3. Eliminar un animal")
    print("4. Imprimir información de un animal")
    print("5. Imprimir información de todos los animales")
    print("6. Imprimir estadísticas de los animales")
    print("7. Salir")

# Crear el zoológico
zoo = Zoologico()

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")

    try:
        if opcion == "1":
            # Dar de alta un nuevo animal
            tipo_animal = input("Ingrese el tipo de animal (Mamifero, Ave, Insecto): ").lower()
            nombre = input("Ingrese el nombre del animal: ")
            peso = float(input("Ingrese el peso del animal: "))
            num_jaula = int(input("Ingrese el número de jaula asignado al animal: "))

            if tipo_animal == "mamifero":
                animal = Mamifero(nombre, tipo_animal, peso, num_jaula)
            elif tipo_animal == "ave":
                color_plumaje = input("Ingrese el color del plumaje del ave: ")
                altura_max_vuelo = float(input("Ingrese la altura máxima de vuelo del ave: "))
                animal = Ave(nombre, tipo_animal, peso, num_jaula, color_plumaje, altura_max_vuelo)
            elif tipo_animal == "insecto":
                vuela = input("¿El insecto vuela? (Sí/No): ").lower() == "si"
                animal = Insecto(nombre, tipo_animal, peso, num_jaula, vuela)
            else:
                raise ValueError("Tipo de animal inválido")

            zoo.agregar_animal(animal)
            print("Se ha agregado el animal correctamente")

        elif opcion == "2":
            # Editar un animal
            nombre = input("Ingrese el nombre del animal a editar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del animal: ")
            nuevo_peso = float(input("Ingrese el nuevo peso del animal: "))
            nuevo_num_jaula = int(input("Ingrese el nuevo número de jaula del animal: "))

            zoo.editar_animal(nombre, nuevo_nombre, nuevo_peso, nuevo_num_jaula)
            print("Se ha editado el animal correctamente")

        elif opcion == "3":
            # Eliminar un animal
            nombre = input("Ingrese el nombre del animal a eliminar: ")

            zoo.eliminar_animal(nombre)
            print("Se ha eliminado el animal correctamente")

        elif opcion == "4":
            # Imprimir info
            nombre = input("Ingrese el nombre del animal a imprimir: ")

            zoo.imprimir_informacion_animal(nombre)

        elif opcion == "5":
            # Imprimir infor
            animales = zoo.animales

            if not animales:
                print("No hay animales registrados")
            else:
                for animal in animales:
                    print(animal)

        elif opcion == "6":
            # Imprimir estadísticas
            num_total_animales = zoo.numero_total_animales()
            num_mamiferos = zoo.numero_animales_clase(Mamifero)
            num_aves = zoo.numero_animales_clase(Ave)
            num_insectos = zoo.numero_animales_clase(Insecto)
            promedio_peso_mamiferos = zoo.promedio_peso_clase(Mamifero)
            promedio_peso_aves = zoo.promedio_peso_clase(Ave)
            promedio_peso_insectos = zoo.promedio_peso_clase(Insecto)

            print("Estadísticas de los animales:")
            print(f"Numero total de animales: {num_total_animales}")
            print(f"Numero de mamíferos: {num_mamiferos}")
            print(f"Numero de aves: {num_aves}")
            print(f"Numero de insectos: {num_insectos}")
            print(f"Promedio de peso de mamíferos: {promedio_peso_mamiferos:.2f}")
            print(f"Promedio de peso de aves: {promedio_peso_aves:.2f}")
            print(f"Promedio de peso de insectos: {promedio_peso_insectos:.2f}")

        elif opcion == "7":
            print("Adiós")
            break

        else:
            raise ValueError("Opción inválida")

    except ValueError as e:
        print("Error:", str(e))
        print("Por favor, ingrese valores válidos.")
        print()

    except KeyError as e:
        print("Error: No se encontró el animal con ese nombre.")
        print()

    except Exception as e:
        print("Ocurrió un error inesperado:", str(e))
        print("Por favor, inténtelo nuevamente.")
        print()

    print()
