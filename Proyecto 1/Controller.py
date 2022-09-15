import time

from MemoryBus import MemoryBus
from L1Cache import L1Cache

class Controller:
	def  __init__(self, processorId, cache, bus):
		self.cache  = cache
		self.memoryBus  = bus
		self.processor  = processorId
		
	def getData(self, address):
		#Buscar con associative 1 way desde controlador
		return L1Block("B0")
		
	def read(self, address):
		hitBlock  = self.getData(address)
		if hitBlock.bitState != "I":
			print(str(self.processor) + "Read Hit \n")
		else:
			print(str(self.processor) + "Read miss\n")
			#Manejo de miss
			
	def write(self, address, data):
		hitBlock  = self.getData(address)
		if hitBlock.bitState != "I":
			print(str(self.processor) + "Write Hit \n")
			#Logica de estados MESI
		else:
			#Logica de estados MESI y politicas de escritura
	
