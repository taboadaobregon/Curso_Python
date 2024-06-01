
#Tkinter
# Modulo para crear interface graficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.titulo = "Master en python"
        self.icono = './imagenes/twitter-logo (1).ico'
        self.icono_alt = './04-Tkinter/imagenes/twitter-logo (1).ico'
        self.size = "770x470"
        self.rezisable = False
    
    def cargar(self):

        #crear la ventana raiz
        ventana = Tk()
        #asi podemos jalar 
        self.ventana = ventana

        #titulo de la ventana
        ventana.title(self.titulo)

        #comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icono)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icono_alt)

        #Icono de la ventana
        ventana.iconbitmap(ruta_icono)


        #mostrar texto en el programa
        texto = Label(ventana, text = ruta_icono )
        texto.pack()



        # cambio el tamaño de la ventana
        ventana.geometry(self.size)

        #bloquear el tamaño de la ventana
        if self.rezisable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
            #ventana.resizable(1,0) nivel horizontal
            #ventana.resizable(0,1) nivel vertical

        #Arrancar y mostrar la ventana hasta que se cierre
        #ventana.mainloop()
    
    #aqui todavia no se ejecuta el programa
    def addTexto(self,dato):
        texto = Label(self.ventana , text = dato)
        texto.pack()

    def mostrar(self):
        #Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()
    
#instanciar mi programa 
programa  = Programa()
programa.cargar()
programa.addTexto("hola soy andres taboada")
programa.mostrar()