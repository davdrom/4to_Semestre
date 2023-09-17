#Romero Ramos David Grupo 942
"""
17. Pruebe su programa del problema 16 experimentando con diferentes escenarios hipotéticos que le permitan observar qué
excepciones pueden presentarse. Listar todas las excepciones que se generaron. NOTA: Debe contemplar que cada acción del menú
puede generar excepciones; Ejemplos:  El usuario tiene problemas al capturar datos, Seleccionar elementos que no existen.
"""

"""
    Acción: Dar de alta un nuevo animal.
    Excepción posible: ValueError si se ingresan datos inválidos para el animal, como un peso no numérico.
    Acción: Editar un animal.
    Excepción posible: KeyError si se intenta editar un animal que no existe en la lista de animales.
    Acción: Eliminar un animal.
    Excepción posible: KeyError si se intenta eliminar un animal que no existe en la lista de animales.
    Acción: Imprimir información de un animal.
    Excepción posible: KeyError si se intenta imprimir la información de un animal que no existe en la lista de animales.
    Acción: Imprimir información de todos los animales.
    Excepción posible: No se generan excepciones en esta acción, a menos que la lista de animales esté vacía.
    Acción: Imprimir estadística de los animales.
    Excepción posible: ZeroDivisionError si no hay animales de una clase específica para calcular el promedio de peso.

"""