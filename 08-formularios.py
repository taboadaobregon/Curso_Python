from tkinter import *


ventana = Tk()

ventana.geometry("500x400")

ventana.title("Formularios en Tkinter | andres")


# texto encabezado
encabezado = Label(ventana, text="Formulario en tkinter")

encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
#encabezado.pack(side=LEFT,anchor=NW,fill=X,expand=YES)
encabezado.grid(row=0 , column=0 ,columnspan=12,sticky=W)
# campo de texto

label = Label(ventana, text="NOMBRE")
label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

campo_texto = Entry(ventana)
#campo_texto.pack(side=LEFT,anchor=W)
campo_texto.grid(row=1,column=1,padx=5,pady=5,sticky=W)
campo_texto.config(justify="left",state="normal")


#apellidos
label = Label(ventana, text="APELLIDOS")
label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

campo_texto = Entry(ventana)
#campo_texto.pack(side=LEFT,anchor=W)
campo_texto.grid(row=2,column=1,padx=5,pady=5,sticky=W)
campo_texto.config(justify="left",state="disabled")


#label para descripcion

label = Label(ventana,text="Descripcion")
label.grid(row=3,column=0,padx=5,pady=5)

#campo texto grande 

campo_grande = Text(ventana)
campo_grande.grid(row=3,column=1)
campo_grande.config(
    width=30,
    height=5,
    font=("Arial",12),
    padx=15,
    pady=15
)


#boton
Label(ventana).grid(row=4,column=1)
boton = Button(ventana,text="Enviar")
boton.grid(row=5,column=1,sticky=W)
boton.config(
    padx=15,
    pady=15,
    bg="green",
    fg="white"
)



ventana.mainloop()

