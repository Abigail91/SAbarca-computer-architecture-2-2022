import threading
import time
from Controller import Controller

class Processor:
	def  __init__(self, id):
		self.id = id
		self.running  = False
		self.instRunning  = ""
		self.lastInst  = ""
		self.control  = Controller(self.id)
		
	def decodeInst(self, instruction)
		print("Instrcuccion decodificada")
	
	def exc(self):
		while self.running:
			self.thread_clock()
	
	def exc_step(self):
		self.thread_clock()
		
	def thread_clock(self):
		print("Generando siguiente")
		
	def runThread(self, isStep):
		if self.running:
			print(str(self.id) + " Ejecutando \n")
		else: 
			if isStep:
				thread = threading.Thread(target=exc_step, daemon=True)
			else:
				thread = threading.Thread(target=exc, daemon=True)
			thread.start()
			
	def stopThread(self):
		if self.running:
			self.running = False
		else: 
			print(str(self.id) + " Detenido \n")	
