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
texto.pack()

def pruebas(nombres,apellidos,pais):
    return f"Hola {nombres} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text=pruebas(pais="Peru",nombres="Andres",apellidos="Taboada"))
# texto.config(
#     justify=RIGHT
# )
texto.config(
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=10,
    cursor="spider"
    #cursor="circle"
    #cursor="arrow"
)

texto.pack(anchor=E)

ventana.mainloop()