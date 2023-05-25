from tkinter import *

def seleccion():
    txt.config(text=f'Opcion seleccionada {opcion.get()}')

pantalla = Tk()

pantalla.title("Ejercicio 10.1")

contenido = Frame(pantalla, relief='flat', borderwidth=33)


opcion = IntVar()

rbtn = Radiobutton(pantalla, text = "Opcion 1", value=1, variable=opcion, command=seleccion)
rbtn.grid(column=0, row=0)
rbtn2 = Radiobutton(pantalla, text = "Opcion 2", value=2, variable=opcion, command=seleccion)
rbtn2.grid(column=0, row=1)
rbtn3 = Radiobutton(pantalla, text = "Opcion 3", value=3, variable=opcion, command=seleccion)
rbtn3.grid(column=0, row=2)
rbtn4 = Radiobutton(pantalla, text = "Opcion 4", value=4, variable=opcion, command=seleccion)
rbtn4.grid(column=0, row=3)

txt = Label(pantalla, text="Seleccione una opcion")
txt.grid(column=1, row=4)

btn = Button(pantalla, text="Reiniciar", command=lambda: {
    opcion.set(None),
    txt.config(text="Seleccione una opcion")})

btn.grid(column=3, row=0)

contenido.grid()

mainloop()