import threading
import time
import instGenerator
from Controller import Controller

class Processor:
	def  __init__(self, id, bus):
		self.id = id
		self.running  = False
		self.instRunning  = "---"
		self.lastInst  = ""
		self.control  = Controller(self.id, bus)
		self.customInst = ""
		
	
	def exc(self):
		while self.running:
			self.thread_clock()
	
	def exc_step(self):
		self.thread_clock()
		
	def thread_clock(self):
		self.lastInst = self.instRunning
		if self.customInst == "":
			inst = instGenerator.genInstruction()
		else:	
			inst = self.customInst[4:]
			print(inst)
		self.instRunning = inst
		initial = inst[0]
		if initial == "R":
			self.control.read(int(inst[5:8], 2))
		elif initial == "W":
			self.control.write(int(inst[6:9], 2), int(inst[10:],16))
		elif initial == "C":
			print("CALC")
		else:
			print("Instruction error")
			self.instRunning = ""


		
	def runThread(self, isStep):
		if self.running:
			print(str(self.id) + " Ejecutando \n")
		else: 
			if isStep:
				hilo = threading.Thread(target=self.exc_step, daemon=True)
			else:
				self.running = True
				hilo = threading.Thread(target=self.exc, daemon=True)
			hilo.start()
			
	def pauseThread(self):
		if self.running:
			self.running = False
		else: 
			print(str(self.id) + " Detenido \n")	
