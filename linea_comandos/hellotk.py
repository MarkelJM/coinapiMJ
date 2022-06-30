from tkinter import *
from tkinter import ttk

root = Tk()
marco = ttk.Frame(root, padding=50)
marco.grid()

etiqueta = Label(marco, text= "Hello Tkinter", padx = 100, pady=50, bg= 'white')
etiqueta.grid(row=0, column=0)


otra = Label(marco, text= "soy otra etiqueta de Tkinter", bg='yellow')
otra.grid(row=1, column=0)

root.mainloop()
