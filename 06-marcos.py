from tkinter import *

ventana = Tk()
ventana.title("Marcos | Mater en Python")
ventana.geometry("700x700")


marco_padre = Frame(ventana,width=250,height=250)

# marco_padre.config(
#     bg="pink",
#     bd=5,
#     #relief=SOLID,
#     relief=SOLID
# )

marco_padre.pack(side=BOTTOM,anchor=S, fill=X,expand=YES)


marco = Frame(marco_padre,width=250,height=250)

marco.config(
    bg="red",
    bd=5,
    #relief=SOLID,
    relief=RAISED
)

marco.pack(side=LEFT,anchor=SW)

marco = Frame(marco_padre,width=250,height=250)

marco.config(
    bg="green",
    bd=5,
    #relief=SOLID,
    relief=RAISED
)

marco.pack(side=RIGHT,anchor=SE)

marco_padre = Frame(ventana,width=250,height=250)

# marco_padre.config(
#     bg="pink",
#     bd=5,
#     #relief=SOLID,
#     relief=SOLID
# )

marco_padre.pack(side=TOP,anchor=N,fill=X,expand=YES)


marco = Frame(marco_padre,width=250,height=250)

marco.config(
    bg="green",
    bd=5,
    #relief=SOLID,
    relief=RAISED
)

marco.pack(side=RIGHT,anchor=SE)


marco = Frame(marco_padre,width=250,height=250)

marco.config(
    bg="blue",
    bd=5,
    #relief=SOLID,
    relief=RAISED
)

marco.pack(side=LEFT,anchor=SE)


ventana.mainloop()