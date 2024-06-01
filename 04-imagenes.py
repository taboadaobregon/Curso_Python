from tkinter import *
from PIL import Image,ImageTk

ventana = Tk()

ventana.geometry("700x500")

Label(ventana,text="Hola, soy andres").pack(anchor=W)

imagen = Image.open('./04-Tkinter/imagenes/images (1).jpeg')
render = ImageTk.PhotoImage(imagen)

Label(ventana,image=render).pack(anchor=W)

ventana.mainloop()