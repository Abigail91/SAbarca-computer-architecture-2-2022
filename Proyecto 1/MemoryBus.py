import threading
import time
from Memory import Memory



class MemoryBus:
	def  __init__(self, memory):
		self.lock = threading.Lock()
		memory = memory
		processors = []
		
	def sharedAddressP(self, address, cpu):
		cpus = []
		
		for processor in self.processors:
			if processor.id != cpu and processor.control.getCorresBlock(address):
				cpus.append(processor.id)
		print(str(cpus))
		return cpus
				
	def lockMe(self):
		self.lock.acquire()
		
	def unlockMe(self):
		self.lock.release()

		self.lock.release()



