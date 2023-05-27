from tkinter import *
import sqlite3
from tkinter import messagebox


def guardarU(identificador, nombre, apellido):
    try:
        conex = sqlite3.connect("ejercicio11.db")
        cursor = conex.cursor()

        if identificador == "" or nombre == "" or apellido == "":
            raise Exception("datatype mismatch")

        cursor.execute("INSERT INTO Alumnos(id, nombre, apellido) VALUES (?, ?, ?)", (identificador, nombre, apellido))

        conex.commit()
    except Exception as e:

        if "UNIQUE constraint failed: Alumnos.id" == str(e):

            messagebox.showwarning(message="El identificador existe en la base de datos", title="Error")
        elif "datatype mismatch" == str(e):

            messagebox.showwarning(message="Llenar todos los campos", title="Error")
    finally:
        cursor.close()
        conex.close()

def buscarU(listaU, nombreB):
    try:
        conex = sqlite3.connect("ejercicio11.db")
        cursor = conex.cursor()
        encontrado = False

        alumnos = cursor.execute("SELECT * FROM Alumnos")

        listaU.delete(0, END)

        for alumno in alumnos.fetchall():

            if nombreB.capitalize() in alumno:
                listaU.insert(END, alumno)
                encontrado = False
                break
            elif nombreB in "default":
                listaU.insert(END, alumno)
            else:
                encontrado = True

        if encontrado:
            messagebox.showwarning(message="Nombre no encontrado", title="Error")

    except Exception as ex:

        print("Error "+ str(ex))
    finally:

        cursor.close()
        conex.close()


def main():
    pantalla = Tk()

    pantalla.geometry("265x300")
    pantalla.title("Registro alumnos")

    contenido = Frame(pantalla, bg='lightgray')

    Label(contenido, text="Identificador", bg='lightgray',).grid(column=0, row=0, pady=5)
    identificador = Entry(contenido)
    identificador.grid(column=1, row=0)

    Label(contenido, text="Nombre", bg='lightgray').grid(column=0, row=1, padx=10, pady=5)
    nombre = Entry(contenido)
    nombre.grid(column=1, row=1)

    Label(contenido, text="Apellido", bg='lightgray').grid(column=0, row=2, padx=10, pady=5)
    apellido = Entry(contenido)
    apellido.grid(column=1, row=2)

    Label(contenido, text="Nombre", bg='lightgray').grid(column=0, row=3, padx=10, pady=5)
    nombreB = Entry(contenido)
    nombreB.grid(column=1, row=3)

    listaU = Listbox(contenido)
    listaU.grid(column=1, row=4, pady=10)

    btnG = Button(contenido, text="Guardar", command=lambda : {
        guardarU(identificador.get(), nombre.get(), apellido.get()),
        identificador.delete(0,END),
        nombre.delete(0,END),
        apellido.delete(0,END)})
    btnG.grid(column=3, row=0, padx=10)

    btnB = Button(contenido, text="Buscar", command=lambda: {
        buscarU(listaU, nombreB.get()),
        nombreB.delete(0,END)})
    btnB.grid(column=3, row=3, padx=10)

    contenido.grid(column=0, row=2, ipadx=100, ipady=100)

if __name__ =="__main__":
    main()
    mainloop()