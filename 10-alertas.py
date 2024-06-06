from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("Alerta","Hola soy andres")

Button(ventana,text="Mostrar Alerta!! ",command=sacarAlerta).pack()


def salir(nombre):
    resultado = MessageBox.askquestion("Salir","¿Quieres continuar ejecutando la aplicacion?")
    if resultado != "yes":
        MessageBox.showinfo("Chaoo!!",f"Adios {nombre}")
        ventana.destroy()


Button(ventana,text="Salir",command=lambda:salir("Andres")).pack()


ventana.mainloop()