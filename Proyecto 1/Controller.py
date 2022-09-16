import time

from MemoryBus import MemoryBus
from L1Cache import L1Cache

class Controller:
	def  __init__(self, processorId, bus):
		self.cache  = L1Cache()
		self.memoryBus  = bus
		self.processor  = processorId
		
	def getCorresBlock(self, address):
        	if address == 0 or address == 4:
            		block = self.cache.getBlock(0)
        	elif address == 1 or address == 5:
            		block = self.cache.l1Blocks[1]
        	elif address == 2 or address == 6:
            		block = self.cache.l1Blocks[2]
        	elif address == 3 or address == 7:
            		block = self.cache.l1Blocks[3]
        	else:
        		print("Direccion incorrecta")

        	if block.memoryAddress == address and block.getBitState() != "I":
		        return block
        	else:
        		return False

		
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
			print("Write Miss")
			#Logica de estados MESI y politicas de escritura
			

	
