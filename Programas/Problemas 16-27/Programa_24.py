#Romero Ramos David Grupo 942
"""
24.  Crear un archivo python donde pruebe la clase Biblioteca. Debe crear un menú, donde cada opción llame a un método de la clase Biblioteca.
"""
from Programa_23 import *

def mostrar_menu():
    print("********** MENÚ **********")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Editar libro")
    print("4. Obtener información de un libro")
    print("5. Mostrar biblioteca")
    print("6. Guardar biblioteca en archivo binario")
    print("7. Guardar biblioteca en archivo JSON")
    print("8. Salir")
    print("***************************")

def ejecutar_opcion(opcion, biblioteca):
    if opcion == "1":
        agregar_libro(biblioteca)
    elif opcion == "2":
        eliminar_libro(biblioteca)
    elif opcion == "3":
        editar_libro(biblioteca)
    elif opcion == "4":
        obtener_libro(biblioteca)
    elif opcion == "5":
        mostrar_biblioteca(biblioteca)
    elif opcion == "6":
        guardar_binario(biblioteca)
    elif opcion == "7":
        guardar_json(biblioteca)
    elif opcion == "8":
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Intente nuevamente.")

def agregar_libro(biblioteca):
    nombre = input("Ingrese el nombre del libro: ")
    anio = int(input("Ingrese el año de edición del libro: "))
    autor = input("Ingrese el autor del libro: ")

    biblioteca.agregar_libro(nombre, anio, autor)
    print("Libro agregado correctamente.")

def eliminar_libro(biblioteca):
    indice = int(input("Ingrese el índice del libro que desea eliminar: "))
    try:
        biblioteca.eliminar_libro(indice - 1)
        print("Libro eliminado correctamente.")
    except IndexError as e:
        print(f"Error: {str(e)}")

def editar_libro(biblioteca):
    indice = int(input("Ingrese el índice del libro que desea editar: "))
    try:
        nombre = input("Ingrese el nuevo nombre del libro: ")
        anio = int(input("Ingrese el nuevo año de edición del libro: "))
        autor = input("Ingrese el nuevo autor del libro: ")

        biblioteca.editar_libro(indice - 1, nombre, anio, autor)
        print("Libro editado correctamente.")
    except IndexError as e:
        print(f"Error: {str(e)}")

def obtener_libro(biblioteca):
    indice = int(input("Ingrese el índice del libro del cual desea obtener información: "))
    try:
        libro = biblioteca.obtener_libro(indice - 1)
        print(f"Información del libro:\n{str(libro)}")
    except IndexError as e:
        print(f"Error: {str(e)}")

def mostrar_biblioteca(biblioteca):
    print(str(biblioteca))

def guardar_binario(biblioteca):
    ruta_archivo = input("Ingrese la ruta del archivo binario donde desea guardar la biblioteca: ")
    try:
        biblioteca.guardar_bin(ruta_archivo)
        print("Biblioteca guardada correctamente en formato binario.")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")

def guardar_json(biblioteca):
    ruta_archivo = input("Ingrese la ruta del archivo JSON donde desea guardar la biblioteca: ")
    try:
        biblioteca.guardar_json(ruta_archivo)
        print("Biblioteca guardada correctamente en formato JSON.")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")

def main():
    biblioteca = Biblioteca()
    opcion = ""

    while opcion != "8":
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        ejecutar_opcion(opcion, biblioteca)

if __name__ == "__main__":
    main()
