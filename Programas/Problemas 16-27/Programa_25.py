#Romero Ramos David Grupo 942
"""
25. Diseñar e implementar una GUI para el juego del Gato. Debe tener una clase jugador, con los atributos nombre, total de juegos, número de ganados, número de perdidos,
número de empatados. Al iniciar la GUI debe crear dos instancias de Jugador preguntar por sus nombres usando simpledialog.askstring .
Para crear el tablero puede usar botones o labels. Lo más sencillo son labels que cambien el texto X o O.
A ambos widgets le pueden agregar imágenes en lugar de texto.
La diferencia entre ambos es que al hacer click, un label no tiene command tienes que usar bind, mientras que un botón si tiene command.

Debe de tener dos botones uno de Iniciar Juego y otro donde muestre los resultados de los dos jugadores usando messagebox.
Puede guiarse con las imágenes siguientes, el diseño es totalmente libre.

Debe realizar todas las validaciones necesarias y excepciones para el correcto funcionamiento de la aplicación.
Todos estos puntos: diseño, creación de clases, validaciones y excepciones impactarán en la calificación de este problema.

"""
import tkinter as tk
from tkinter import simpledialog, messagebox


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.total_juegos = 0
        self.num_ganados = 0
        self.num_perdidos = 0
        self.num_empatados = 0


class GUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("GATOO")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="black")

        self.jugador1 = None
        self.jugador2 = None
        self.jugador_actual = None

        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.botones = []

        self.crear_interfaz()
        self.juego_iniciado = None

    def crear_interfaz(self):
        self.crear_botones()
        self.crear_inicio_juego()
        self.crear_resultados()
        self.crear_turno_etiqueta()

    def crear_botones(self):
        for i in range(3):
            fila_botones = []
            for j in range(3):
                boton = tk.Button(self.ventana, text=" ", width=10, height=5, font=("Fixedsys", 16, "bold"),
                                  state="disabled")

                boton.grid(row=i, column=j, padx=5, pady=5)
                boton.bind("<Button-1>", lambda event, x=i, y=j: self.marcar_casilla(x, y))
                fila_botones.append(boton)
            self.botones.append(fila_botones)

    def crear_inicio_juego(self):
        self.btn_inicio_juego = tk.Button(self.ventana, text="Iniciar Juego", command=self.iniciar_juego, font=("Fixedsys", 14, "bold"), bg="black",fg="white")
        self.btn_inicio_juego.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    def crear_resultados(self):
        self.btn_resultados = tk.Button(self.ventana, text="Mostrar Resultados", command=self.mostrar_resultados,font=("Fixedsys", 14, "bold"), bg="black",fg="white")
        self.btn_resultados.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def crear_turno_etiqueta(self):
        self.etiqueta_turno = tk.Label(self.ventana, text="", font=("Fixedsys", 20, "bold"), bg="black",fg="white")
        self.etiqueta_turno.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    def iniciar_juego(self):
        self.juego_iniciado = True
        self.jugador1 = Jugador(simpledialog.askstring("Jugador 1", "Nombre del Jugador 1"))
        self.jugador2 = Jugador(simpledialog.askstring("Jugador 2", "Nombre del Jugador 2"))
        self.jugador_actual = self.jugador1

        self.actualizar_texto_botones("")
        self.limpiar_tablero()
        self.habilitar_botones()
        self.actualizar_turno_etiqueta()

    def habilitar_botones(self):
        for fila in self.botones:
            for boton in fila:
                boton.config(state="normal")

    def deshabilitar_botones(self):
        for fila in self.botones:
            for boton in fila:
                boton.config(state="disabled")

    def marcar_casilla(self, fila, columna):
        if self.juego_iniciado:
            if self.tablero[fila][columna] == " ":
                self.tablero[fila][columna] = "X" if self.jugador_actual == self.jugador1 else "O"
                self.botones[fila][columna].config(text=self.tablero[fila][columna])

                if self.tablero[fila][columna] == "X":
                    self.botones[fila][columna].config(fg="red")
                elif self.tablero[fila][columna] == "O":
                    self.botones[fila][columna].config(fg="black")

                self.botones[fila][columna].unbind("<Button-1>")

                if self.comprobar_ganador():
                    self.mostrar_mensaje_ganador()
                    self.actualizar_resultados()
                    self.limpiar_tablero()
                    self.habilitar_botones()
                elif self.comprobar_empate():
                    self.mostrar_mensaje_empate()
                    self.actualizar_resultados()
                    self.limpiar_tablero()
                    self.habilitar_botones()
                else:
                    self.jugador_actual = self.jugador2 if self.jugador_actual == self.jugador1 else self.jugador1
                    self.actualizar_turno_etiqueta()
    def actualizar_turno_etiqueta(self):
        turno_jugador = f"Turno de: {self.jugador_actual.nombre}"
        self.etiqueta_turno.config(text=turno_jugador)

    def limpiar_colores(self):
        for fila in self.botones:
            for boton in fila:
                boton.config(bg="white")

    def limpiar_tablero(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.actualizar_texto_botones("")
        for i in range(3):
            for j in range(3):
                self.botones[i][j].bind("<Button-1>", lambda event, x=i, y=j: self.marcar_casilla(x, y))
                self.limpiar_colores()

    def actualizar_texto_botones(self, texto):
        for fila in self.botones:
            for boton in fila:
                boton.config(text=texto)

    def comprobar_ganador(self):
        for i in range(3):
            # Comprobar filas
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != " ":
                self.resaltar_casillas_ganadoras([(i, 0), (i, 1), (i, 2)])
                return True
            # Comprobar columnas
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != " ":
                self.resaltar_casillas_ganadoras([(0, i), (1, i), (2, i)])
                return True
        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != " ":
            self.resaltar_casillas_ganadoras([(0, 0), (1, 1), (2, 2)])
            return True
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != " ":
            self.resaltar_casillas_ganadoras([(0, 2), (1, 1), (2, 0)])
            return True
        return False

    def resaltar_casillas_ganadoras(self, casillas):
        for fila, columna in casillas:
            self.botones[fila][columna].config(bg="gold", fg="white")

    def comprobar_empate(self):
        for fila in self.tablero:
            if " " in fila:
                return False
        return True

    def mostrar_mensaje_ganador(self):
        messagebox.showinfo("¡Felicidades!", f"¡{self.jugador_actual.nombre} ha ganado!")

    def mostrar_mensaje_empate(self):
        messagebox.showinfo("Empate", "¡El juego ha terminado en empate!")

    def mostrar_resultados(self):
        if self.juego_iniciado:
            messagebox.showinfo("Resultados", f"{self.jugador1.nombre}: {self.jugador1.num_ganados} ganados, "
                                              f"{self.jugador1.num_perdidos} perdidos, {self.jugador1.num_empatados} empatados\n"
                                              f"{self.jugador2.nombre}: {self.jugador2.num_ganados} ganados, "
                                              f"{self.jugador2.num_perdidos} perdidos, {self.jugador2.num_empatados} empatados")
        else:
            messagebox.showerror(title="NO", message="TIENES QUE INICIAR EL JUEGO PRIMERO!")

    def actualizar_resultados(self):
        if self.jugador_actual == self.jugador1:
            self.jugador1.num_ganados += 1
            self.jugador2.num_perdidos += 1
        else:
            self.jugador1.num_perdidos += 1
            self.jugador2.num_ganados += 1
        self.jugador1.total_juegos += 1
        self.jugador2.total_juegos += 1

    def iniciar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    juego = GUI()
    juego.iniciar()
