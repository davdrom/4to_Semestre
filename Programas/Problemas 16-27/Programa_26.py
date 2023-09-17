#Romero Ramos David Grupo 942
"""

"""
import tkinter as tk
import random
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("juego")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="gray")

        self.colores = ["red", "blue", "green", "pink", "black", "yellow", "orange", "white", "purple", "brown"]
        self.color_actual = ""
        self.color_texto_actual = ""
        self.puntaje = 0
        self.tiempo_restante = 30

        self.crear_widgets()
        self.generar_color_aleatorio()
        self.iniciar_temporizador()

    def crear_widgets(self):
        self.fuente_fixedsys = ("Fixedsys", 20)

        self.etiqueta_color = tk.Label(self.ventana, text="", font=self.fuente_fixedsys, pady=50,bg="gray")
        self.etiqueta_color.pack()

        self.etiqueta_ingreso = tk.Label(self.ventana, text="Ingresa el color de la palabra en ingles:", font=self.fuente_fixedsys, bg="gray")
        self.etiqueta_ingreso.pack()

        self.entrada_color = tk.Entry(self.ventana, font=self.fuente_fixedsys, bg="gray")
        self.entrada_color.pack()
        self.entrada_color.focus()

        self.entrada_color.bind('<Return>', self.validar_respuesta)

        self.etiqueta_puntaje = tk.Label(self.ventana, text="Puntaje: 0", font=self.fuente_fixedsys, bg="gray", fg="light green")
        self.etiqueta_puntaje.pack()

        self.etiqueta_tiempo = tk.Label(self.ventana, text="Tiempo: 30", font=self.fuente_fixedsys, bg="gray", fg="red")
        self.etiqueta_tiempo.pack()

    def generar_color_aleatorio(self):
        self.color_actual = random.choice(self.colores)
        self.color_texto_actual = random.choice(self.colores)

        self.etiqueta_color.config(text=self.color_actual, fg=self.color_texto_actual)

    def validar_respuesta(self, evento=None):
        respuesta_usuario = self.entrada_color.get().lower()

        if respuesta_usuario == self.color_texto_actual:
            self.puntaje += 1
            self.etiqueta_puntaje.config(text=f"Puntaje: {self.puntaje}")
        else:
            self.puntaje -= 1
            self.puntaje = max(0, self.puntaje)

        self.generar_color_aleatorio()
        self.entrada_color.delete(0, tk.END)

    def iniciar_temporizador(self):
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.etiqueta_tiempo.config(text=f"Tiempo: {self.tiempo_restante}")
            self.ventana.after(1000, self.iniciar_temporizador)
        else:
            self.finalizar_juego()

    def finalizar_juego(self):
        self.entrada_color.config(state="disabled")

        puntaje_mas_alto = self.obtener_puntaje_mas_alto()

        if self.puntaje > puntaje_mas_alto:
            self.guardar_puntaje_mas_alto()

        messagebox.showinfo("Fin del juego", f"Puntaje final: {self.puntaje}\n"
                                              f"Puntaje más alto: {puntaje_mas_alto}")

        self.ventana.quit()

    def obtener_puntaje_mas_alto(self):
        try:
            with open("puntaje_mas_alto.txt", "r") as archivo:
                puntaje_mas_alto = int(archivo.read())
        except FileNotFoundError:
            puntaje_mas_alto = 0

        return puntaje_mas_alto

    def guardar_puntaje_mas_alto(self):
        with open("puntaje_mas_alto.txt", "w") as archivo:
            archivo.write(str(self.puntaje))

    def iniciar(self):
        self.ventana.mainloop()

juego = GUI()
juego.iniciar()

