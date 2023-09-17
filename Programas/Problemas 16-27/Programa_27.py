#Romero Ramos David Grupo 942
"""
27. Modificar la aplicación Agenda realizada en clase, se debe de agregar el código necesario para que las funcionalidades de
editar y eliminar funcionen adecuadamente. No olvide experimentar y agregar excepciones de ser necesario.

"""

from tkinter import *
from tkinter import messagebox


class Persona:
    def __init__(self, nombre, apellidos,
                 telefono, sexo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.sexo = sexo

    def __str__(self):
        return f"{self.nombre}, {self.apellidos}," \
               f" {self.telefono}, {self.sexo}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, item: Persona):
        self.contactos.append(item)

    def eliminar(self, index):
        if index < 0 or index >= len(self.contactos):
            raise Exception("Contacto. No existe")
        self.contactos.pop(index)

    def editar(self, index, item: Persona):
        if index < 0 or index >= len(self.contactos):
            raise Exception("Contacto. No existe")
        self.contactos[index] = item

    def get_persona(self, index):
        if index < 0 or index >= len(self.contactos):
            raise Exception("Contacto. No existe")
        return self.contactos[index]


class F1(Frame):

    def __init__(self, contenedor: Tk):
        super().__init__(contenedor, pady=30)

        lblNombre = Label(self, text="Nombre: ")
        lblNombre.grid(row=0, column=0)
        self.txtNombre = Entry(self)
        self.txtNombre.grid(row=0, column=1, padx=5, pady=5)

        lblApellidos = Label(self, text="Apellidos: ")
        lblApellidos.grid(row=1, column=0)
        self.txtApellidos = Entry(self)
        self.txtApellidos.grid(row=1, column=1, padx=5, pady=5)

        lblTelefono = Label(self, text="Telefono: ")
        lblTelefono.grid(row=2, column=0)
        self.txtTelefono = Entry(self)
        self.txtTelefono.grid(row=2, column=1, padx=5, pady=5)

        self.sexo = StringVar()
        self.rdbM = Radiobutton(self, text="Masculino",
                                value="M", variable=self.sexo)
        self.rdbM.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        self.rdbF = Radiobutton(self, text="Femenino", value="F", variable=self.sexo)
        self.rdbF.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

        self.rdbS = Radiobutton(self, text="Sin Especificar", value="SN", variable=self.sexo)
        self.rdbS.grid(row=6, column=0, padx=5, pady=5, columnspan=2)

        self.rdbS.select()


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda App")
        self.geometry("600x350")
        self.minsize(width=600, height=340)
        # self.resizable(False, False)
        self.agenda = Agenda()
        self.lista_personas = StringVar()
        self.list_box = Listbox(self, listvariable=self.lista_personas)
        self.list_box.pack(side=LEFT, fill=BOTH, expand=True)

        frameDerecho = Frame(self)
        frameDerecho.pack(side=TOP, fill=BOTH, expand=True)

        self.f = F1(frameDerecho)
        self.f.pack(side=TOP)

        frameBotones = Frame(frameDerecho)
        self.btn_agregar = Button(frameBotones, text="Agregar", width=3, command=self.agregar)
        self.btn_agregar.pack(side=LEFT, padx=10, ipadx=30, pady=10)

        self.btn_editar = Button(frameBotones, text="Editar", width=3, command=self.editar)
        self.btn_editar.pack(side=LEFT, padx=10, ipadx=30, pady=10)

        self.btn_eliminar = Button(frameBotones, text="Eliminar", width=3, command=self.eliminar)
        self.btn_eliminar.pack(side=LEFT, padx=10, ipadx=30, pady=10)
        frameBotones.pack(side=BOTTOM, fill=BOTH)

        self.list_box.bind("<<ListboxSelect>>",
                           self.selected)

    def selected(self, event):
        indices= self.list_box.curselection()
        index = indices[0]
        p= self.agenda.get_persona(index)
        self.clean()
        self.f.txtNombre.insert(0, p.nombre)
        self.f.txtApellidos.insert(0, p.apellidos)
        self.f.txtTelefono.insert(0, p.telefono)
        self.f.sexo.set(p.sexo)


    def agregar(self):
        nombre = self.f.txtNombre.get()
        apellidos = self.f.txtApellidos.get()
        telefono = self.f.txtTelefono.get()
        sexo = self.f.sexo.get()
        p = Persona(nombre, apellidos, telefono, sexo)
        self.agenda.agregar(p)
        self.lista_personas.set(self.agenda.contactos)
        messagebox.showinfo("AGREGAR", "CONTACTO AGREGADO CORRECTAMENTE!")
        self.clean()

    def editar(self):
        indices = self.list_box.curselection()
        if indices:
            index = indices[0]
            nombre = self.f.txtNombre.get()
            apellidos = self.f.txtApellidos.get()
            telefono = self.f.txtTelefono.get()
            sexo = self.f.sexo.get()
            p = Persona(nombre, apellidos, telefono, sexo)
            try:
                self.agenda.editar(index, p)
                self.lista_personas.set(self.agenda.contactos)
                messagebox.showinfo("EDITAR", "CONTACTO EDITADO CORRECTAMENTE!")
                self.clean()
            except Exception as e:
                messagebox.showerror("ERROR", str(e))

    def eliminar(self):
        indices = self.list_box.curselection()
        if indices:
            index = indices[0]
            try:
                self.agenda.eliminar(index)
                self.lista_personas.set(self.agenda.contactos)
                messagebox.showinfo("ELIMINAR", "CONTACTO ELIMINADO CORRECTAMENTE!")
                self.clean()
            except Exception as e:
                messagebox.showerror("ERROR", str(e))

    def clean(self):
        self.f.txtNombre.delete(0, END)
        self.f.txtApellidos.delete(0, END)
        self.f.txtTelefono.delete(0, END)
        self.f.sexo.set("SN")
        self.f.txtNombre.focus()

if __name__ == "__main__":
    w = Window()
    w.mainloop()
