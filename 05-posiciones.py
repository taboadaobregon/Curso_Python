from tkinter import *

ventana = Tk()
ventana.geometry("500x500")


texto = Label(ventana, text="Hola mundo")
texto.config(
    fg="white",
    bg="black",
    padx=520,
    pady=20,
    font=("Consolas", 20)
    )
texto.pack(side=TOP)

def pruebas(nombres,apellidos,pais):
    return f"Hola {nombres} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text="aaa")
# texto.config(
#     justify=RIGHT
# )
texto.config(
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
    #cursor="circle"
    #cursor="arrow"
)

#texto.pack(side=TOP,fill=X,expand=YES)
texto.pack(side=LEFT)


texto = Label(ventana, text="aaa")
# texto.config(
#     justify=RIGHT
# )
texto.config(
    height=3,
    bg="pink",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
    #cursor="circle"
    #cursor="arrow"
)

texto.pack(side=LEFT)


texto = Label(ventana, text="hola")
# texto.config(
#     justify=RIGHT
# )
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
    #cursor="circle"
    #cursor="arrow"
)

texto.pack(side=TOP,fill=X,expand=YES)

ventana.mainloop()