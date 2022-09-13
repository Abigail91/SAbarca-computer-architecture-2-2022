from tkinter import *

def mensaje():
	print("Hello")

ventana = Tk()
ventana.geometry("1300x900")
ventana.title("Simulador protocolo MESI")



lblU = Label(ventana, text="000")
lblU.grid(row=21, column=1)
lblU = Label(ventana, text="000")
lblU.grid(row=21, column=2)
lblU = Label(ventana, text="000")
lblU.grid(row=21, column=3)
lblU = Label(ventana, text="000")
lblU.grid(row=21, column=4)
lblU = Label(ventana, text="000")
lblU.grid(row=21, column=5)
lblU = Label(ventana, text="000")
lblU.grid(row=21, column=6)
lblU = Label(ventana, text="000")
lblU.grid(row=21, column=7)
lblU = Label(ventana, text="000")
lblU.grid(row=21, column=8)


lblP0 = Label(ventana, text="P0", width=15, height=7)
lblP0.grid(row=0, column=2)

lblP1 = Label(ventana, text="P1", width=15, height=7)
lblP1.grid(row=0, column=4)

lblP2 = Label(ventana, text="P2", width=15, height=7)
lblP2.grid(row=0, column=6)

lblP3 = Label(ventana, text="P3", width=15, height=7)
lblP3.grid(row=0, column=8)

btn = Button(ventana, text = "Empezar Simulación", command=mensaje, height=2)
btn.grid(row=2, column=9)

btn = Button(ventana, text = "Pausar Simulación", command=mensaje, height=2)
btn.grid(row=4, column=9)

btn = Button(ventana, text = "Simulación paso a paso", command=mensaje, height=2)
btn.grid(row=6, column=9)


lblP3 = Label(ventana, text="Instrucción especifica", width=30, height=2)
lblP3.grid(row=8, column=9)
entry = Entry()
entry.grid(row=9, column=9)
btn = Button(ventana, text = "Agregar Instrucción", command=mensaje, height=2)
btn.grid(row=10, column=9)

lblP3 = Label(ventana, text="Alertas", width=30, height=2)
lblP3.grid(row=13, column=9)

lbl = Label(ventana, text="", width=10, height=4)
lbl.grid(row=0, column=0)
lblE = Label(ventana, text="Ejecutando", width=30, height=2)
lblE.grid(row=1, column=0)
lblU = Label(ventana, text="Última ejecución", width=30, height=2)
lblU.grid(row=2, column=0)
lblU = Label(ventana, text="Bloque 0", width=30, height=2)
lblU.grid(row=3, column=0)
lblU = Label(ventana, text="Estado", width=30)
lblU.grid(row=4, column=0)
lblU = Label(ventana, text="Dirección", width=30)
lblU.grid(row=5, column=0)
lblU = Label(ventana, text="Dato", width=30)
lblU.grid(row=6, column=0)
lblU = Label(ventana, text="Bloque 1", width=30, height=2)
lblU.grid(row=7, column=0)
lblU = Label(ventana, text="Estado", width=30)
lblU.grid(row=8, column=0)
lblU = Label(ventana, text="Dirección", width=30)
lblU.grid(row=9, column=0)
lblU = Label(ventana, text="Dato", width=30)
lblU.grid(row=10, column=0)
lblU = Label(ventana, text="Bloque 2", width=30, height=2)
lblU.grid(row=11, column=0)
lblU = Label(ventana, text="Estado", width=30)
lblU.grid(row=12, column=0)
lblU = Label(ventana, text="Dirección", width=30)
lblU.grid(row=13, column=0)
lblU = Label(ventana, text="Dato", width=30)
lblU.grid(row=14, column=0)
lblU = Label(ventana, text="Bloque 3", width=30,height=2)
lblU.grid(row=15, column=0)
lblU = Label(ventana, text="Estado", width=30)
lblU.grid(row=16, column=0)
lblU = Label(ventana, text="Dirección", width=30)
lblU.grid(row=17, column=0)
lblU = Label(ventana, text="Dato", width=30)
lblU.grid(row=18, column=0)

lblU = Label(ventana, text="Memoria",height=4)
lblU.grid(row=19, column=4)

lblU = Label(ventana, text="Bloque 0")
lblU.grid(row=20, column=1)
lblU = Label(ventana, text="Bloque 1")
lblU.grid(row=20, column=2)

lblU = Label(ventana, text="Bloque 2")
lblU.grid(row=20, column=3)
lblU = Label(ventana, text="Bloque 3")
lblU.grid(row=20, column=4)

lblU = Label(ventana, text="Bloque 4")
lblU.grid(row=20, column=5)
lblU = Label(ventana, text="Bloque 5")
lblU.grid(row=20, column=6)

lblU = Label(ventana, text="Bloque 6")
lblU.grid(row=20, column=7)
lblU = Label(ventana, text="Bloque 7")
lblU.grid(row=20, column=8)

ventana.mainloop()
