from tkinter import *
import time
from Memory import Memory
from MemoryBus import MemoryBus
from Processor import Processor
import threading
class interfaz:
	def  __init__(self, root):
		self.root = Tk = root
		self.root.geometry("1300x900")
		self.root.title("Simulador protocolo MESI")
		self.root.resizable(False, False)
		self.processors = []
		self.memory = Memory()
		self.bus = MemoryBus(self.memory)
		self.P0AInst= StringVar()
		self.P0AInst.set("P0 : ----------")
		self.P0LInst= StringVar()
		self.P0LInst.set("P0 : ----------")
		self.P0B0D= StringVar()
		self.P0B0D.set("P0 : ----------")
		self.P0B1D= StringVar()
		self.P0B1D.set("P0 : ----------")
		self.P0B2D= StringVar()
		self.P0B2D.set("P0 : ----------")
		self.P0B3D= StringVar()
		self.P0B3D.set("P0 : ----------")
		
		self.UI()
		self.back()




	def UI(self):
		ventana = self.root

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
		p0AInstLabel = Label(self.root, textvariable=self.P0AInst)
		p0AInstLabel.grid(row=1, column=2)
		p0LInstLabel = Label(self.root, textvariable=self.P0LInst)
		p0LInstLabel.grid(row=2, column=2)
		p0B0DL = Label(self.root, textvariable=self.P0B0D)
		p0B0DL.grid(row=6, column=2)
		p0B1DL = Label(self.root, textvariable=self.P0B1D)
		p0B1DL.grid(row=10, column=2)
		p0B2DL = Label(self.root, textvariable=self.P0B2D)
		p0B2DL.grid(row=14, column=2)
		p0B3DL = Label(self.root, textvariable=self.P0B3D)
		p0B3DL.grid(row=18, column=2)

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
	
	def back(self):
		b = self.bus
		p0 = Processor(0, b)
		p1 = Processor(1, b)
		p2 = Processor(2, b)
		p3 = Processor(3, b)
		self.processors = [p0,p1,p2,p3]
		p0.runThread(False)
		UIThread = threading.Thread(target=self.updateUI, daemon=True)
		UIThread.start()
		
	def updateUI(self):
		while 1:
			print(self.processors[0].instRunning)
			self.P0AInst.set(self.processors[0].instRunning)
			self.P0LInst.set(self.processors[0].lastInst)
			self.P0B0D.set(self.processors[0].control.cache.getBlock(0).getData())
			self.P0B1D.set(self.processors[0].control.cache.getBlock(1).getData())
			self.P0B2D.set(self.processors[0].control.cache.getBlock(2).getData())
			self.P0B3D.set(self.processors[0].control.cache.getBlock(3).getData())
			time.sleep(0.1)


def mensaje():
	print("Hello")


