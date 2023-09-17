#Romero Ramos David Grupo 942
"""
23. Crear una clase Biblioteca, que contenga una lista vacía de Libros (usar la clase ItemLibro). Esta clase debe contener los siguientes métodos:
agregar_libro: El cual debe recibir como parámetro un objeto de tipo ItemLibro el cuál se agregara a la lista.
eliminar_libro: Reciba el índice del elemento que se desea eliminar. Validar que dicho índice se encuentre en el rango de la lista.
editar_libro: Recibe el índice del elemento a editar, y un objeto de tipo ItemLibro con los datos actualizados.
obtener_libro: Recibe el índice del elemento que se desea saber la información. Este método retorna un objeto de tipo ItemLibro.
__str__: Sobreescribir este método de tal manera que retorne la información de todos los libros, en caso de no existir ningún libro retornar Biblioteca vacía. Puede usar el formato que desee.
guardar_bin: Método para guardar la información de una instancia Biblioteca en un archivo binario. Debe recibir como parámetro la ruta donde se desea guardar el archivo. Recuerde si la ruta no existe esto puede ocasionar una excepción de tipo FileNotFoundException.
guardar_json: Método para guardar la información de una instancia Biblioteca en un archivo json. Debe recibir como parámetro la ruta donde se desea guardar el archivo. Recuerde si la ruta no existe esto puede ocasionar una excepción de tipo FileNotFoundException.

"""
from Programa_22 import *
import pickle
import json

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, item_libro):
        self.libros.append(item_libro)

    def eliminar_libro(self, indice):
        if 0 <= indice < len(self.libros):
            del self.libros[indice]
        else:
            raise IndexError("Índice fuera de rango.")

    def editar_libro(self, indice, item_libro):
        if 0 <= indice < len(self.libros):
            self.libros[indice] = item_libro
        else:
            raise IndexError("Índice fuera de rango.")

    def obtener_libro(self, indice):
        if 0 <= indice < len(self.libros):
            return self.libros[indice]
        else:
            raise IndexError("Índice fuera de rango.")

    def __str__(self):
        if len(self.libros) == 0:
            return "Biblioteca vacía."

        biblioteca_str = "Biblioteca:\n"
        for i, item_libro in enumerate(self.libros):
            biblioteca_str += f"\nLibro {i+1}:\n{str(item_libro)}\n"

        return biblioteca_str

    def guardar_bin(self, ruta_archivo):
        with open(ruta_archivo, "wb") as archivo:
            pickle.dump(self, archivo)

    def guardar_json(self, ruta_archivo):
        with open(ruta_archivo, "w") as archivo:
            json.dump(self, archivo, default=lambda x: x.__dict__, indent=4)
