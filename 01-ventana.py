#Tkinter
# Modulo para crear interface graficas de usuario

from tkinter import *
import os.path


#crear la ventana raiz
ventana = Tk()

#titulo de la ventana
ventana.title("Interfaz grafica de Python")

#comprobar si existe un archivo
ruta_icono = os.path.abspath('./imagenes/twitter-logo (1).ico')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./04-Tkinter/imagenes/twitter-logo (1).ico')

#Icono de la ventana
ventana.iconbitmap(ruta_icono)


#mostrar texto en el programa
texto = Label(ventana, text = ruta_icono )
texto.pack()



# cambio el tamaño de la ventana
ventana.geometry("750x450")

#bloquear el tamaño de la ventana
ventana.resizable(0,0)
#ventana.resizable(1,0) nivel horizontal
#ventana.resizable(0,1) nivel vertical





#Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()