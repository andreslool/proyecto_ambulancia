from tkinter import *
from tkinter import messagebox
import sqlite3
import sys

#          funciones       #


def buscarllamada():
    try:
        miConexion = sqlite3.connect("Emergencia")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM REGISTRO WHERE CI=" + CI.get())

    except:
        messagebox.showwarning("BBDD", "¡Debes añadir datos primero!")

    elusuario = miCursor.fetchall()

    for usuario in elusuario:
        CI.set(usuario[0])
        Nombre.set(usuario[1])
        Apellido.set(usuario[2])
        Telefono.set(usuario[3])
        Parentesco.set(usuario[4])

    miConexion.commit()


def agregarllamada():

    try:
        miConexion = sqlite3.connect("Emergencia")
        miCursor = miConexion.cursor()
        miCursor.execute("INSERT INTO REGISTRO VALUES ('" + CI.get() +
                         "','" + Nombre.get() +
                         "','" + Apellido.get() +
                         "','" + Telefono.get() +
                         "','" + Parentesco.get() + "')")

        miConexion.commit()

        CI.set("")
        Nombre.set("")
        Apellido.set("")
        Telefono.set("")
        Parentesco.set("")

        messagebox.showinfo("REGISTRO", "Registro agregado con exito")

    except:
        messagebox.showwarning("BBDD", "¡Debes agregar datos primero!")


def limpiarllamada():
    CI.set("")
    Nombre.set("")
    Apellido.set("")
    Telefono.set("")
    Parentesco.set("")


def conexionbbdd():
    miConexion = sqlite3.connect("Emergencia")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
			CREATE TABLE EMERGENCIA (
			CI INTEGER (10),
			NOMBRE VARCHAR (50),
			APELLIDO VARCHAR (50),
			EDAD INTEGER (3),
			TIPOEMERGENCIA TEXT (100),
			LUGAREMERGENCIA TEXT (100),
			FECHAENTRADA VARCHAR (10),
			FECHASALIDA VARCHAR (10),
			CIREGISTRO INTEGER (10))
			''')

        miCursor.execute('''
			CREATE TABLE REGISTRO (
			CI INTEGER (10),
			NOMBRE VARCHAR (50),
			APELLIDO VARCHAR (50),
			TELEFONO INTEGER (12),
			PARENTESCO VARCHAR (50))
			''')

        messagebox.showinfo("BBDD", "BBDD creada con exito")

    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")


def licencia():

    messagebox.showinfo("Licencia", "Version 1.0 | actualizado el: 01/12/20")


def acercade():

    messagebox.showinfo("Acerca de", "Creado por: Andres Marquez")


def salirapp():
    valor = messagebox.askquestion("Salir", "¿Estas seguro?")

    if valor == "yes":
        sys.exit()


def limpiarcampos():

    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miEdad.set("")
    tipoemergencia.delete(1.0, END)
    lugaremergencia.delete(1.0, END)
    miFechaEntrada.set("")
    miFechaSalida.set("")
    miciregistro.set("")


def agregar():

    try:
        if miID.get() == "":
            messagebox.showwarning("ATENCION", "Debes agregar una cedula!")
        else:
            miConexion = sqlite3.connect("Emergencia")
            miCursor = miConexion.cursor()
            miCursor.execute("INSERT INTO Emergencia VALUES ('" + miID.get() +
                             "','" + miNombre.get() +
                             "','" + miApellido.get() +
                             "','" + miEdad.get() +
                             "','" + tipoemergencia.get("1.0", END) +
                             "','" + lugaremergencia.get("1.0", END) +
                             "','" + miFechaEntrada.get() +
                             "','" + miFechaSalida.get() +
                             "','" + miciregistro.get() + "')")

            miConexion.commit()

            miID.set("")
            miNombre.set("")
            miApellido.set("")
            miEdad.set("")
            tipoemergencia.delete(1.0, END)
            lugaremergencia.delete(1.0, END)
            miFechaEntrada.set("")
            miFechaSalida.set("")
            miciregistro.set("")

            messagebox.showinfo("BBDD", "Registro agregado con exito")

    except:
        messagebox.showwarning(
            "BBDD", "¡Debes crear la base de datos primero!")


def buscar():

    try:
        miConexion = sqlite3.connect("Emergencia")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM EMERGENCIA WHERE CI=" + miID.get())

    except:
        messagebox.showwarning("BBDD", "¡Debes añadir datos primero!")

    elusuario = miCursor.fetchall()

    for usuario in elusuario:
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miEdad.set(usuario[3])
        lugaremergencia.delete(1.0, END)
        lugaremergencia.insert(1.0, usuario[4])
        tipoemergencia.delete(1.0, END)
        tipoemergencia.insert(1.0, usuario[5])
        miFechaEntrada.set(usuario[6])
        miFechaSalida.set(usuario[7])
        miciregistro.set(usuario[8])

    miConexion.commit()


def borrarusuario():

    try:
        valor = messagebox.askquestion(
            "Borrar Usuario", "¿Estas seguro De Borrar este Usuario?")
        if valor == "yes":
            miConexion = sqlite3.connect("Emergencia")
            miCursor = miConexion.cursor()
            miCursor.execute("DELETE FROM EMERGENCIA WHERE CI=" + miID.get())
            miConexion.commit()
            messagebox.showinfo("BBDD", "persona eliminada con exito")

    except:
        messagebox.showwarning("BBDD", "¡persona no encontrada!")


def borrarllamada():

    try:
        valor = messagebox.askquestion(
            "Borrar Usuario", "¿Estas seguro De Borrar este Registro?")
        if valor == "yes":
            miConexion = sqlite3.connect("Emergencia")
            miCursor = miConexion.cursor()
            miCursor.execute("DELETE FROM REGISTRO WHERE CI=" + CI.get())
            miConexion.commit()
            messagebox.showinfo("BBDD", "persona eliminada con exito")

    except:
        messagebox.showwarning("BBDD", "¡persona no encontrada!")

#     INTERFAZ GRAFICA      #


raiz = Tk()
raiz.title("Registro del servicio de Ambulancias")
raiz.resizable(0, 0)
# raiz.iconbitmap(".ico")
raiz.geometry("800x550")
raiz.config(bg="aqua")

#         menu      #

barramenu = Menu()
raiz.config(menu=barramenu, width=300, height=300)

bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label="Conectar", command=conexionbbdd)

archivomenu = Menu(barramenu, tearoff=0)
archivomenu.add_command(label="Agregar", command=agregar)
archivomenu.add_command(label="Buscar...", command=buscar)
archivomenu.add_command(label="Borrar usuario", command=borrarusuario)
archivomenu.add_command(label="Borrar registro", command=borrarllamada)

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label="Licencia", command=licencia)
ayudamenu.add_command(label="Acerca de...", command=acercade)

salirmenu = Menu(barramenu, tearoff=0)

barramenu.add_cascade(label="BBDD", menu=bbddmenu)
barramenu.add_cascade(label="Archivo", menu=archivomenu)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)
barramenu.add_cascade(label="Salir", command=salirapp)

#        variables del programa        #

miID = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miEdad = StringVar()
miFechaEntrada = StringVar()
miFechaSalida = StringVar()
miciregistro = StringVar()

CI = StringVar()
Nombre = StringVar()
Apellido = StringVar()
Telefono = StringVar()
Parentesco = StringVar()

#     comienzo campos     #

miframe = Frame(raiz)
miframe.grid(row=0, column=0, padx=10, pady=0)

cuadroID = Entry(miframe, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadronombre = Entry(miframe, textvariable=miNombre)
cuadronombre.grid(row=1, column=1, padx=10, pady=10)

cuadroapellido = Entry(miframe, textvariable=miApellido)
cuadroapellido.grid(row=2, column=1, padx=10, pady=10)

cuadroedad = Entry(miframe, textvariable=miEdad)
cuadroedad.grid(row=3, column=1, padx=10, pady=10)

tipoemergencia = Text(miframe, width=15, height=4)
tipoemergencia.grid(row=6, column=1, padx=10, pady=10)
scrollvert = Scrollbar(miframe, command=tipoemergencia.yview)
scrollvert.grid(row=6, column=2, sticky="nsew")
tipoemergencia.config(yscrollcommand=scrollvert.set)

lugaremergencia = Text(miframe, width=15, height=4)
lugaremergencia.grid(row=7, column=1, padx=10, pady=10)
scrollvert2 = Scrollbar(miframe, command=lugaremergencia.yview)
scrollvert2.grid(row=7, column=2, sticky="nsew")
lugaremergencia.config(yscrollcommand=scrollvert2.set)

cuadrofechaentrada = Entry(miframe, textvariable=miFechaEntrada)
cuadrofechaentrada.grid(row=8, column=1, padx=10, pady=10)

cuadrofechasalida = Entry(miframe, textvariable=miFechaSalida)
cuadrofechasalida.grid(row=9, column=1, padx=10, pady=10)

cuadrociregistro = Entry(miframe, textvariable=miciregistro)
cuadrociregistro.grid(row=10, column=1, padx=10, pady=10)

#        label      #

labelID = Label(miframe, text="C.I: ")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)

labelnombre = Label(miframe, text="Nombres: ")
labelnombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)

labelapellido = Label(miframe, text="Apellidos: ")
labelapellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)

labeledad = Label(miframe, text="Edad: ")
labeledad.grid(row=3, column=0, sticky="e", padx=10, pady=10)

labeltipoemergencia = Label(miframe, text="Tipo de Emergencia: ")
labeltipoemergencia.grid(row=6, column=0, sticky="e", padx=10, pady=10)

labellugaremergencia = Label(miframe, text="Lugar de la Emergencia: ")
labellugaremergencia.grid(row=7, column=0, sticky="e", padx=10, pady=10)

labelfechaingreso = Label(miframe, text="Fecha de ingreso: ")
labelfechaingreso.grid(row=8, column=0, sticky="e", padx=10, pady=10)

labelfechasalida = Label(miframe, text="Fecha de Salida: ")
labelfechasalida.grid(row=9, column=0, sticky="e", padx=10, pady=10)

labelciregistro = Label(miframe, text="Cedula de la persona que registra: ")
labelciregistro.grid(row=10, column=0, sticky="e", padx=10, pady=10)

#        botones       #

miframe2 = Frame(raiz)
miframe2.grid(row=1, column=0, padx=10, pady=0)

botonagregar = Button(miframe2, text="Guardar", command=agregar)
botonagregar.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

botonbuscar = Button(miframe2, text="Buscar", command=buscar)
botonbuscar.grid(row=1, column=3, sticky="nsew", padx=10, pady=10)

botonborrar = Button(miframe2, text="Borrar", command=limpiarcampos)
botonborrar.grid(row=1, column=4, sticky="nsew", padx=10, pady=10)

#     comienzo campos registro     #

miframe3 = Frame(raiz)
miframe3.grid(row=0, column=1, sticky="s", padx=10, pady=0)

cuadroregistroID = Entry(miframe3, textvariable=CI)
cuadroregistroID.grid(row=2, column=1, padx=10, pady=10)

cuadroregistronombre = Entry(miframe3, textvariable=Nombre)
cuadroregistronombre.grid(row=3, column=1, padx=10, pady=10)

cuadroregistroapellido = Entry(miframe3, textvariable=Apellido)
cuadroregistroapellido.grid(row=4, column=1, padx=10, pady=10)

cuadroregistrotelefono = Entry(miframe3, textvariable=Telefono)
cuadroregistrotelefono.grid(row=5, column=1, padx=10, pady=10)

cuadroregistroparentesco = Entry(miframe3, textvariable=Parentesco)
cuadroregistroparentesco.grid(row=6, column=1, padx=10, pady=10)

#        label registro      #

#imagen= PhotoImage(file="ambulancia.png")
#tituloimagen= Label(miframe3, image=imagen)
#tituloimagen.grid(row=0, column=0, columnspan=2, sticky="s", padx=10, pady=0)

labelregistrotitulo = Label(miframe3, text=" REGISTRO DE LLAMADAS ")
labelregistrotitulo.grid(row=1, column=0, columnspan=2,
                         sticky="s", padx=10, pady=0)

labelregistroCI = Label(miframe3, text="C.I: ")
labelregistroCI.grid(row=2, column=0, sticky="e", padx=10, pady=10)

labelregistronombre = Label(miframe3, text="Nombres: ")
labelregistronombre.grid(row=3, column=0, sticky="e", padx=10, pady=10)

labelregistroapellido = Label(miframe3, text="Apellidos: ")
labelregistroapellido.grid(row=4, column=0, sticky="e", padx=10, pady=10)

labelregistrotelefono = Label(miframe3, text="Telefono: ")
labelregistrotelefono.grid(row=5, column=0, sticky="e", padx=10, pady=10)

labelregistroparentesco = Label(
    miframe3, text="Parentesco con la emergencia: ")
labelregistroparentesco.grid(row=6, column=0, sticky="e", padx=10, pady=10)

#        botones registro       #

miframe4 = Frame(raiz)
miframe4.grid(row=1, column=1, padx=10, pady=0)

botonagregar = Button(miframe4, text="Guardar", command=agregarllamada)
botonagregar.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

botonbuscar = Button(miframe4, text="Buscar", command=buscarllamada)
botonbuscar.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)

botonborrar = Button(miframe4, text="Borrar", command=limpiarllamada)
botonborrar.grid(row=0, column=4, sticky="nsew", padx=10, pady=10)

raiz.mainloop()
