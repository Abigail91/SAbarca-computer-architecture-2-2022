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
		hitBlock  = self.getCorresBlock(address)
		if hitBlock:
			print(str(self.processor) + " Read Hit \n")
		else:
			print(str(self.processor) + " Read miss\n")
			self.memoryBus.lockMe()
			processorsShared = self.memoryBus.sharedAddressP(address, self.processor)
			if len(processorsShared) != 0:
				p = processorsShared[0]
				block = p.control.getCorresBlock(address)
				if block.bitState == "M":
					self.memoryBus.writeMemory(block.memoryAddress, block.data)
				blockWrite = self.cache.write(address, block.getData(), "S")
				self.memoryBus.changeStates(address, processorsShared, 0)
				
				
			else:
				data = self.memoryBus.readMemory(address)
				blockWrite  = self.cache.write(address, data, "E")
				
			if blockWrite.bitState == "M" and blockWrite.address :
				self.memoryBus.writeMemory(block.address, block.data)
			self.memoryBus.unlockMe()
				
			
	def write(self, address, data):
		hitBlock  = self.getCorresBlock(address)
		if hitBlock.bitState != "I":
			print(str(self.processor) + "Write Hit \n")
			#Logica de estados MESI
		else:
			print("Write Miss")
			#Logica de estados MESI y politicas de escritura
			

	
