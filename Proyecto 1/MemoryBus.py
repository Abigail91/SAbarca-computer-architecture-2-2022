import threading
import time
from Memory import Memory
from Processor import Processor

## Falta definir el cpu
class MemoryBus:
	def  __init__(self, p0, p1, p2, p3, memory):
		self.lock = threading.Lock()
		memory = memory
		processors = [p0, p1, p2, p3]
		
	def sharedAddressP(self, address, cpu):
		cpus = []
		
		for processor in self.processors:
			if processor.id != cpu 
				#Verificar los bloques de cache con asociatividad one way controlador
				
	def lockMe(self):
		self.lock.acquire()
		
	def unlockMe(self):
		self.lock.release()

		self.lock.release()

