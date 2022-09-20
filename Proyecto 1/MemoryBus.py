import threading
import time
from Memory import Memory



class MemoryBus:
	def  __init__(self, memory):
		self.lock = threading.Lock()
		self.memory = memory
		self.processors = []
		self.instructions = []
		
	def sharedAddressP(self, address, cpu):
		cpus = []
		
		for processor in self.processors:
			if processor.id != cpu and processor.control.getCorresBlock(address):
				cpus.append(processor)
		return cpus
				
	def lockMe(self):
		self.lock.acquire()
		
	def unlockMe(self):
		self.lock.release()
		
	def readMemory(self, address):
		data = self.memory.read(address)
		time.sleep(1)
		return data
		
	def writeMemory(self, address, data):
		self.memory.write(address, data)
		time.sleep(1)	
	def changeStates(self, address, processorsShared, change):
		for processor in processorsShared:
			block = processor.control.cache.getL1BlockByAddress(address)
			match change:
				case 0:
					block.setBitState("S") 
				case 1:
					block.setBitState("I") 
				case 2:
					block.setBitState("E")





