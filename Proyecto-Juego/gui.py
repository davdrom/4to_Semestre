from constantes import *
import random
from tkinter import Button, Label, Frame, messagebox, filedialog, Menu, Tk, PhotoImage, Entry, Toplevel, Canvas
import pickle


class GUI:
    def __init__(self):
        self.VENTANA = Tk()  # Crear Ventana
        self.VENTANA.title(TITULO)  # Nombre de la ventana
        self.VENTANA.iconbitmap("imagenes/icono.ico")
        self.VENTANA.wm_iconbitmap("imagenes/icono.ico")
        self.VENTANA.config(bg="black")
        self.menu_principal()  # Llama al menu principal

        # Necesario para evitar error en cargar partida
        self.combate_frame = Frame(self.VENTANA)
        self.resultado_frame = Frame(self.VENTANA)
        self.combate_frame.grid(column=0, row=0)
        self.resultado_frame.grid(column=0, row=0)

        self.jugador = JUGADOR_1
        self.oponentes = ENEMIGOS

        self.combate_actual = 0
        self.ventana = Frame(pady=0)
        self.historia2_frame = Frame(self.ventana)
        self.cont = 0
        self.contHIPER = 0

    def menu_principal(self):
        self.menu_principal_frame = Frame(self.VENTANA)
        self.menu_principal_frame.grid(column=0, row=0)
        self.menu_principal_frame.config(bg="black")

        self.label_titulo = Label(self.menu_principal_frame,text="TORNEO DE LEYENDAS", font=(FUENTETEXTO,30), fg="RED", bg="black")
        self.label_titulo.grid(column=0, row=0,pady=10,padx=10)
        self.label_nombre = Label(self.menu_principal_frame,text="Ingresa tu nombre:", font=(FUENTETEXTO,12), fg="white", bg="black")
        self.label_nombre.grid(column=0, row=1,pady=10,padx=10)
        self.entry_nombre = Entry(self.menu_principal_frame, font=(FUENTETEXTO,12), fg="white", bg="black")
        self.entry_nombre.grid(column=0, row=2,pady=10,padx=10)


        self.iniciar_button = Button(self.menu_principal_frame,
                                     text="Iniciar Juego",
                                     command=self.iniciar_juego, font=(FUENTETEXTO,12), fg="white", bg="red")

        self.iniciar_button.grid(column=0, row=3,pady=10,padx=10)

        self.cargar_button = Button(self.menu_principal_frame,
                                    text="Cargar Partida",
                                    command=self.cargar_partida, font=(FUENTETEXTO,12), fg="white", bg="blue")

        self.cargar_button.grid(column=0, row=4,pady=10,padx=10)

    def actualizar_nombre(self):
        nuevonombre = self.entry_nombre.get()
        if nuevonombre == "":
            nuevonombre = "Jugador 1"
        self.jugador.nombre = nuevonombre

    def iniciar_juego(self):
        self.mostrar_historia()
        self.actualizar_nombre()
        self.menu_principal_frame.destroy()

    def mostrar_historia(self):
        self.historia_frame = Frame(self.VENTANA)
        self.historia_frame.grid(column=0, row=0)
        self.historia_frame.config(bg="black")
        self.crear_menu_barra()

        historia_label = Label(self.historia_frame,
                                  text=Historia1, font=(FUENTETEXTO,12), fg="white", bg="black")
        historia_label.grid(column=0, row=0, pady=10, padx=10)

        continuar_button = Button(self.historia_frame, text="Continuar",
                                  command=self.mostrar_historia2, font=(FUENTETEXTO,12), fg="black", bg="white", relief="groove", borderwidth=6)
        continuar_button.grid(column=0, row=1, pady=10, padx=10)

    def mostrar_historia2(self):
        self.resultado_frame.destroy()
        self.combate_frame.destroy()
        self.historia_frame.destroy()
        self.historia2_frame = Frame(self.VENTANA)
        self.historia2_frame.grid(column=0, row=0)
        self.historia2_frame.config(bg="black")
        self.crear_menu_barra()

        historia_label = Label(self.historia2_frame,
                                  text=Historia2, font=(FUENTETEXTO,16), fg="white", bg="black")
        historia_label.grid(column=0, row=0,pady=10,padx=10)

        pelea_label = Label(self.historia2_frame,
                                  text="PREPARATE PARA TU PRIMER ENFRENTAMIENTO", font=(FUENTETEXTO,20), fg="RED", bg="black")
        pelea_label.grid(column=0, row=1,pady=10,padx=10)

        continuar_button = Button(self.historia2_frame, text="Continuar",
                                  command=self.primercomb, font=(FUENTETEXTO,12), fg="black", bg="white", relief="groove", borderwidth=6)
        continuar_button.grid(column=0, row=3)

    def primercomb(self):
        messagebox.showinfo(title=f"Combate {self.combate_actual + 1}: {self.oponentes[self.combate_actual].nombre}",
                            message=self.oponentes[self.combate_actual].historia)
        self.mostrar_combate()

    def cargar_imagenes(self):
        self.imagenJugador = PhotoImage(file=self.jugador.imagen)
        self.imagenJugador = self.imagenJugador.subsample(1,1)
        self.imagenOponente = PhotoImage(file=self.oponentes[self.combate_actual].imagen)
        self.imagenOponente = self.imagenOponente.subsample(1,1)
        self.versusimagen = PhotoImage(file="imagenes/versus.png")
        self.versusimagen = self.versusimagen.subsample(10,10)


    def mostrar_combate(self):
        self.resultado_frame.destroy()
        self.combate_frame.destroy()
        self.historia2_frame.destroy()
        self.crear_menu_barra()

        self.combate_frame = Frame(self.VENTANA)
        self.combate_frame.grid(column=0, row=0)
        self.VENTANA.config(bg="white")
        self.combate_frame.config(bg="white")

        self.cargar_imagenes()

        combate_label = Label(self.combate_frame, text=f"Combate {self.combate_actual + 1}", font=(FUENTETEXTO, 20),
                              fg="black", bg="white")
        combate_label.grid(column=1, row=0, pady=10, padx=10)

        combate_label = Label(self.combate_frame,
                              text=f"Combate {self.combate_actual + 1}", font=(FUENTETEXTO, 20), fg="black", bg="white")
        combate_label.grid(column=1, row=0, pady=10, padx=10)

        salud_jugador_label = Label(self.combate_frame,
                                    text=f"Salud de {self.jugador.nombre}: {self.jugador.salud}", font=(FUENTETEXTO,12), fg="green", bg="white")
        salud_jugador_label.grid(column=0, row=1, pady=10, padx=10)

        stats_jugador_label = Label(self.combate_frame,
                                    text=f"Ataque: {self.jugador.ataque}      Defensa: {self.jugador.defensa}", font=(FUENTETEXTO,12), fg="black", bg="white")
        stats_jugador_label.grid(column=0, row=3, pady=10, padx=10)


        salud_enemigo_label = Label(self.combate_frame,
                                    text=f"Salud de {self.oponentes[self.combate_actual].nombre}: {self.oponentes[self.combate_actual].salud}",
                                    font=(FUENTETEXTO,12), fg="red", bg="white")

        salud_enemigo_label.grid(column=2, row=5, pady=10, padx=10)

        self.imagenJugadorlbl = Label(self.combate_frame,
                                      image=self.imagenJugador,bg="white")

        self.imagenJugadorlbl.grid(column=0, row=4, pady=1, padx=10)

        self.versuslbl = Label(self.combate_frame,
                               image=self.versusimagen,bg="white")

        self.versuslbl.grid(column=1, row=4, pady=10, padx=10)

        self.imagenOponentelbl = Label(self.combate_frame,
                                      image=self.imagenOponente,bg="white")

        self.imagenOponentelbl.grid(column=2, row=4, pady=10, padx=10)

        ataque_button = Button(self.combate_frame,
                               text="JAB",
                               command=self.atacar,
                               activeforeground="red",
                               activebackground="white", relief="groove", borderwidth=6, font=(FUENTETEXTO,12), fg="white", bg="red")
        ataque_button.grid(column=0, row=6, pady=10, padx=10)

        defensa_button = Button(self.combate_frame,
                                text="DEFENDER",
                                command=self.defender,activeforeground="green",
                                activebackground="white", relief="groove", borderwidth=6, font=(FUENTETEXTO,12), fg="white", bg="green")

        defensa_button.grid(column=1, row=6, pady=10, padx=10)

        self.ataque_S_button = Button(self.combate_frame,
                               text="GANCHO",
                               command=self.ataque_S,
                               activeforeground="gold",
                               activebackground="white", relief="groove", borderwidth=6, state="disabled", font=(FUENTETEXTO,12), fg="white", bg="gold")
        self.ataque_S_button.grid(column=2, row=6, pady=10, padx=10)

        if self.cont >= 3:
            self.ataque_S_button.config(state="normal")


        if len(self.jugador.inventario) > 0 and objetoMIKE.nombre == self.jugador.inventario[0].nombre:
            self.habilidadeslbl = Label(self.combate_frame,
                                        text=f"Habilidades Especiales:",
                                        font=(FUENTETEXTO, 12), fg="Black", bg="white")

            self.habilidadeslbl.grid(column=0, row=7, pady=10, padx=10)

            self.boton_Guantes = Button(self.combate_frame,
                               text="HIPERGANCHO",
                               command=self.hipergancho,
                               activeforeground="orange",
                               activebackground="white", relief="groove", borderwidth=6, state="disabled", font=(FUENTETEXTO,12), fg="white", bg="orange")

            self.boton_Guantes.grid(column=0, row=8,pady=10,padx=10)
            if self.contHIPER >= 2:
                self.boton_Guantes.config(state="normal")

        if len(self.jugador.inventario) > 1 and objetoMUHAMMAD.nombre == self.jugador.inventario[1].nombre:
            self.boton_PANTALONES = Button(self.combate_frame,
                               text="HIPERCURACION",
                               command=self.curacion,
                               activeforeground="light green",
                               activebackground="white", relief="groove", borderwidth=6, state="disabled", font=(FUENTETEXTO,12), fg="white", bg="light green")

            self.boton_PANTALONES.grid(column=1, row=8,pady=10,padx=10)
            if self.contHIPER >= 3:
                self.boton_PANTALONES.config(state="normal")

        if len(self.jugador.inventario) > 2 and objetoBRUCE.nombre == self.jugador.inventario[2].nombre:
            self.boton_NUNCHAKUS = Button(self.combate_frame,
                               text="HIPERPUÑETAZ0",
                               command=self.punetazo,
                               activeforeground="PINK",
                               activebackground="white", relief="groove", borderwidth=6, state="disabled", font=(FUENTETEXTO,12), fg="white", bg="PINK")

            self.boton_NUNCHAKUS.grid(column=2, row=8,pady=10,padx=10)
            if self.contHIPER >= 4:
                self.boton_NUNCHAKUS.config(state="normal")

        if len(self.jugador.inventario) > 3 and objetoCONOR.nombre == self.jugador.inventario[3].nombre:
            self.boton_hiperguardia = Button(self.combate_frame,
                               text="HIPERGUARDIA",
                               command=self.guardia,
                               activeforeground="cyan",
                               activebackground="white", relief="groove", borderwidth=6, state="disabled", font=(FUENTETEXTO,12), fg="white", bg="cyan")

            self.boton_hiperguardia.grid(column=0, row=9, padx=10)
            if self.contHIPER >= 5:
                self.boton_hiperguardia.config(state="normal")

        if len(self.jugador.inventario) > 4 and objetoFLOYD.nombre == self.jugador.inventario[4].nombre:
            self.boton_hiperguardia = Button(self.combate_frame,
                               text="HIPERUPPER",
                               command=self.upper,
                               activeforeground="dark violet",
                               activebackground="white", relief="groove", borderwidth=6, state="disabled", font=(FUENTETEXTO,12), fg="white", bg="dark violet")

            self.boton_hiperguardia.grid(column=1, row=9, padx=10)
            if self.contHIPER >= 6:
                self.boton_hiperguardia.config(state="normal")

        if len(self.jugador.inventario) > 5 and objetoMANNY.nombre == self.jugador.inventario[5].nombre:
            self.boton_hiperguardia = Button(self.combate_frame,
                               text="HIPERREGENERACION",
                               command=self.regeneracion,
                               activeforeground="khaki",
                               activebackground="white", relief="groove", borderwidth=6, state="disabled", font=(FUENTETEXTO,12), fg="white", bg="khaki")

            self.boton_hiperguardia.grid(column=2, row=9, padx=10)
            if self.contHIPER >= 7:
                self.boton_hiperguardia.config(state="normal")


    def jugadorvive(self):
        if not self.jugador.esta_vivo():
            messagebox.showerror(title="DERROTA",
                                   message=f"Has perdido!\n{self.oponente_actual.nombre} te ha derrotado.\n Vuelve a iniciar el juego para volver a jugar")
            self.VENTANA.destroy()

    def oponentevive(self):
        if not self.oponentes[self.combate_actual].esta_vivo():

            self.jugador.agregar_objeto(self.oponentes[self.combate_actual].objeto)
            self.mostrar_victoria()
            messagebox.showinfo(title="FIN DEL COMBATE",
                                message=f"Derrotaste a {self.oponentes[self.combate_actual].nombre} y obtuviste {self.oponentes[self.combate_actual].objeto.nombre}!")
            messagebox.showinfo(title=f"{self.oponentes[self.combate_actual].nombre}",
                                   message=random.choices(textosderrotas))
        else:
            self.turno_enemigo()
    def upper(self):
        if self.contHIPER >= 6:
            self.contHIPER = 0
            self.cont += 1
            danio_jugador = self.jugador.ataque * 4
            self.oponentes[self.combate_actual].recibir_danio(danio_jugador)
            self.mostrar_combate()
            messagebox.showinfo(title="COMBATE",
                                message=f"Has usado el HIPERUPPER de FLOYD MAYWEATHER JR. y has hecho {danio_jugador-self.oponentes[self.combate_actual].defensa} de daño!")

            self.oponentevive()
    def regeneracion(self):
        if self.contHIPER >= 7:
            self.contHIPER = 0
            self.cont += 1
            salud_ganada = 50
            self.jugador.salud += salud_ganada
            messagebox.showinfo(title="COMBATE",
                                message=f"Has usado la HIPERREGENERACION de MANNY PACQUIAO, tu salud ha subido {salud_ganada} puntos!")
            self.turno_enemigo()

    def guardia(self):
        if self.contHIPER >= 5:
            self.contHIPER = 0
            self.cont += 1
            defensa_ganada = 2
            self.jugador.defensa += defensa_ganada
            messagebox.showinfo(title="COMBATE",
                                message=f"Has usado la HIPERGUARDIA de CONOR MCGREGOR, tu defensa ha subido PERMANENTEMENTE {defensa_ganada} puntos!")
            self.turno_enemigo()


    def punetazo(self):
        if self.contHIPER >= 4:
            self.contHIPER = 0
            self.cont += 1
            danio_jugador = self.jugador.ataque * 2.5
            self.oponentes[self.combate_actual].recibir_danio(danio_jugador)
            self.mostrar_combate()
            messagebox.showinfo(title="COMBATE",
                                message=f"Has usado el HIPERPUÑETAZ0 de BRUCE LEE y has hecho {danio_jugador-self.oponentes[self.combate_actual].defensa} de daño!")

            self.oponentevive()

    def curacion(self):
        if self.contHIPER >= 3:
            self.contHIPER = 0
            self.cont += 1
            salud_recuperada = 25
            self.jugador.salud = self.jugador.salud + salud_recuperada
            self.mostrar_combate()
            messagebox.showinfo(title="COMBATE",
                                message=f"Has usado la CURACION de MUHAMMAD ALI y te recuperaste {salud_recuperada} de salud!")

            self.oponentevive()

    def hipergancho(self):
        if self.contHIPER >= 2:
            self.contHIPER= 0
            self.cont += 1
            danio_jugador = self.jugador.ataque * 1.5
            self.oponentes[self.combate_actual].recibir_danio(danio_jugador)
            self.mostrar_combate()
            messagebox.showinfo(title="COMBATE",
                                message=f"Has usado el HIPERGANCHO de MIKE TYSON y has hecho {danio_jugador-self.oponentes[self.combate_actual].defensa} de daño!")

            self.oponentevive()
    def atacar(self):
        self.cont += 1
        self.contHIPER += 1
        danio_jugador = random.randint((self.jugador.ataque-2), self.jugador.ataque)
        self.oponentes[self.combate_actual].recibir_danio(danio_jugador)
        self.mostrar_combate()
        messagebox.showinfo(title="COMBATE",message=f"Has hecho {danio_jugador-self.oponentes[self.combate_actual].defensa} de daño!")

        self.oponentevive()

    def ataque_S(self):
        if self.cont >= 3:
            self.cont = 0
            self.contHIPER += 1
            danio_jugador = self.jugador.ataque_s
            self.oponentes[self.combate_actual].recibir_danio(danio_jugador)
            self.mostrar_combate()
            messagebox.showinfo(title="COMBATE",
                                message=f"Has hecho {danio_jugador-self.oponentes[self.combate_actual].defensa} de daño!")

            self.oponentevive()
    def defender(self):
        self.cont += 1
        self.contHIPER += 1
        self.defensa_bonus = 20
        self.jugador.defensa += self.defensa_bonus
        messagebox.showinfo("Habilidad Especial",
                            "Has usado Defensa Inexpugnable. Tu defensa se ha mejorado en 20 puntos para este turno.")
        self.turno_enemigo_defensa()

    def turno_enemigo(self):
        self.oponente_actual = self.oponentes[self.combate_actual]
        self.danio_enemigo = random.randint(self.oponente_actual.ataque-7, self.oponente_actual.ataque)
        self.jugador.recibir_danio(self.danio_enemigo)
        self.danio_total = self.danio_enemigo-self.jugador.defensa
        if self.danio_total <= 0:
            self.danio_total = 0
        messagebox.showwarning(title="COMBATE",
                                     message=f"{self.oponente_actual.nombre} te ha hecho {self.danio_total} de daño!")
        self.mostrar_combate()

        self.jugadorvive()

    def turno_enemigo_defensa(self):
        self.oponente_actual = self.oponentes[self.combate_actual]
        self.danio_enemigo = random.randint(self.oponente_actual.ataque-7, self.oponente_actual.ataque)
        self.jugador.recibir_danio(self.danio_enemigo)
        self.danio_total = self.danio_enemigo-self.jugador.defensa
        if self.danio_total <= 0:
            self.danio_total = 0
        messagebox.showwarning(title="COMBATE",
                               message=f"{self.oponente_actual.nombre} te ha hecho {self.danio_total} de daño!")
        self.jugador.defensa -= self.defensa_bonus
        self.mostrar_combate()

    def mostrar_victoria(self):
        self.combate_frame.destroy()
        self.resultado_frame.destroy()
        self.resultado_frame = Frame(self.VENTANA)
        self.resultado_frame.grid(column=0, row=0)
        self.VENTANA.config(bg="black")
        self.resultado_frame.config(bg="black")

        resultado_label = Label(self.resultado_frame, text=f"Has derrotado a {self.oponentes[self.combate_actual].nombre}!", font=(FUENTETEXTO,12), fg="white", bg="black")
        resultado_label.grid(column=0, row=0,pady=10,padx=10)

        inventario_label = Label(self.resultado_frame, text=f"Inventario de {self.jugador.nombre}: ", font=(FUENTETEXTO,10), fg="ORANGE", bg="black")
        inventario_label.grid(column=1, row=0,pady=10,padx=10)

        for objeto in self.jugador.inventario:
            objeto_label = Label(self.resultado_frame, text=f"- {objeto.nombre} (Ataque +{objeto.valor_ataque} -- Defensa +{objeto.valor_defensa})", font=(FUENTETEXTO,8), fg="yellow", bg="black")
            objeto_label.grid(column=1,pady=10,padx=10)

        victoria_label = Label(self.resultado_frame,
                               text="¡Elige la opcion que quieras hacer antes de tu proximo combate!", font=(FUENTETEXTO,12), fg="white", bg="black")
        victoria_label.grid(column=0, row=1,pady=10,padx=10)


        entrenar_defensa_button = Button(self.resultado_frame, text="Entrenar Defensa", font=(FUENTETEXTO,12), fg="WHITE", bg="CYAN",
                                         command=self.entrenar_defensa, relief="groove", borderwidth=6)
        entrenar_defensa_button.grid(column=0, row=2,pady=10,padx=10)

        entrenar_ataque_button = Button(self.resultado_frame, text="Entrenar Ataque", command=self.entrenar_ataque, font=(FUENTETEXTO,12), fg="WHITE", bg="ORANGE", relief="groove", borderwidth=6)
        entrenar_ataque_button.grid(column=0, row=3,pady=10,padx=10)

        descansarbtn = Button(self.resultado_frame, text="Descansar por hoy", command=self.descansar, font=(FUENTETEXTO,12), fg="WHITE", bg="PINK", relief="groove", borderwidth=6,)
        descansarbtn.grid(column=0, row=4,pady=10,padx=10)

        self.crear_menu_barra()

    def entrenar_defensa(self):
        self.jugador.defensa += 1
        texto_defensa = f"Has entrenado tu defensa, ahora tienes una defensa de {self.jugador.defensa}.\n¡Prepárate para el próximo combate!"
        messagebox.showinfo(title="Entrenamiento",
                            message=texto_defensa)
        self.siguiente_combate()
        self.resultado_frame.destroy()

    def entrenar_ataque(self):
        self.jugador.ataque += 1
        texto_ataque = f"Has entrenado tu ataque, ahora tienes un ataque de {self.jugador.ataque}.\n¡Prepárate para el próximo combate!"
        messagebox.showinfo(title="Entrenamiento",
                            message=texto_ataque)
        self.siguiente_combate()
        self.resultado_frame.destroy()

    def descansar(self):
        salud_recuperada = random.randint(10,30)
        texto = f"Recuperaste salud al descansar tras ese largo combate, has recuperado {salud_recuperada} puntos de salud!\n¡Prepárate para el próximo combate!"
        self.jugador.salud += salud_recuperada
        if self.jugador.salud > 100:
            self.jugador.salud = 100
        messagebox.showinfo(title="Descanso",
                            message=texto)
        self.siguiente_combate()
        self.resultado_frame.destroy()

    def siguiente_combate(self):
        self.combate_actual += 1
        if self.combate_actual < len(self.oponentes):
            self.mostrar_combate()
            messagebox.showinfo(
                title=f"Combate {self.combate_actual + 1}: {self.oponentes[self.combate_actual].nombre}",
                message=self.oponentes[self.combate_actual].historia)
        else:
            self.mostrar_game_over()

    def mostrar_game_over(self):
        self.combate_frame.destroy()
        self.resultado_frame.destroy()

        self.resultado_frame = Frame(self.VENTANA)
        self.resultado_frame.grid(column=0, row=0)
        self.resultado_frame.config(bg="black")

        resultado_label1 = Label(self.resultado_frame, text=f"GANASTE EL TORNEO!", font=(FUENTETEXTO,12), fg="gold", bg="black")
        resultado_label1.grid(column=0, row=0,pady=10,padx=10)

        resultado_label2 = Label(self.resultado_frame, text=f"Tu esfuerzo ha rendido frutos!", font=(FUENTETEXTO,12), fg="gold", bg="black")
        resultado_label2.grid(column=0, row=1,pady=10,padx=10)

        messagebox.showinfo(title="GAME OVER", message="¡Has ganado el torneo!")

    def crear_menu_barra(self):
        menubar = Menu(self.VENTANA)
        self.VENTANA.config(menu=menubar)
        archivo_menu = Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Guardar Partida", command=self.guardar_partida)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.VENTANA.quit)
        menubar.add_cascade(label="Juego", menu=archivo_menu)
        informacion_menu = Menu(menubar)
        informacion_menu.add_command(label="Torneo de Leyendas", command=self.infoTorneo)
        informacion_menu.add_command(label="Combate", command=self.FORMACOMBATIR)
        informacion_menu.add_command(label="Integrantes", command=self.INTEGRANTES)
        menubar.add_cascade(label="Informacion",menu=informacion_menu)

    def INTEGRANTES(self):
        messagebox.showinfo(title="Integrantes", message="Abel Castillo Vergudo\nAngel Gabriel Garcia Barrera\nDavid Romero Ramos")

    def FORMACOMBATIR(self):
        messagebox.showinfo(title="Forma de combate", message=formadecombate)

    def infoTorneo(self):
        self.infotorneo = Toplevel()
        self.infotorneo.title("TORNEO DE LEYENDAS")
        self.infotorneo.config(bg="black")
        titulo = Label(self.infotorneo, text="TORNEO DE LEYENDAS",font=(FUENTETEXTO,18), fg="GOLD", bg="BLACK")
        titulo.grid(column=0, row=0,pady=10,padx=10)
        texto = Label(self.infotorneo,
                      text=textoinformacion,
                      font=(FUENTETEXTO,12), fg="WHITE", bg="BLACK")
        texto.grid(column=0, row=1,pady=10,padx=10)

    def guardar_partida(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de partida", "*.txt")])

        if archivo:
            datos_partida = {
                'jugador': self.jugador,
                'oponentes': self.oponentes,
                'combate_actual': self.combate_actual,
                'contador_normal': self.cont,
                'contador_hiper': self.contHIPER

            }

            with open(archivo, 'wb') as file:
                pickle.dump(datos_partida, file)

            messagebox.showinfo("Guardar Partida", "Partida guardada exitosamente.")

    def cargar_partida(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de partida", "*.txt")])

        if archivo:
            with open(archivo, 'rb') as file:
                datos_partida = pickle.load(file)

            self.jugador = datos_partida['jugador']
            self.oponentes = datos_partida['oponentes']
            self.combate_actual = datos_partida['combate_actual']
            self.cont = datos_partida['contador_normal']
            self.contHIPER = datos_partida['contador_hiper']



            messagebox.showinfo("Cargar Partida", "Partida cargada exitosamente.")
            self.menu_principal_frame.destroy()
            self.mostrar_combate()

    def iniciar(self):
        self.VENTANA.mainloop()

