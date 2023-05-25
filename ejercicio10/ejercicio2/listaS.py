from tkinter import *

def seleccion(event):
    valor = list(map(lambda x: x.strip(), lista.get()[1:-1].replace("'", '').split(',')))[listaS.curselection()[0]]
    txt.config(text=f'Valor seleccionado: {valor}')


pantalla = Tk()

pantalla.title("Ejercicio 10.2")
pantalla.geometry("250x200")

contenido = Frame(pantalla)

lista = StringVar()
lista.set(["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5", "Elemento 6", "Elemento 7", "Elemento 8"])

listaS = Listbox(contenido, listvariable=lista, bg='lightgray', bd=5, relief=RIDGE)

txt = Label(contenido, text="Seleccion")

listaS.bind("<<ListboxSelect>>", seleccion)

txt.pack()
listaS.pack()
contenido.pack()

mainloop()
