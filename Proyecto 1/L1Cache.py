from L1Block import L1Block
class L1Cache:
	def  __init__(self):
		self.l1Blocks = [L1Block("0"), L1Block("1"), L1Block("2"),L1Block("3")]
		
	def getBlock(self, id):
		return self.l1Blocks[id]

	def getL1BlockByAddress(self, address):
		for l1Block in self.l1Blocks:
			if l1Block.memoryAddress == address:	
				return l1Block 
				
	def write(self, address, data, bitState):
		if address == 0 or address == 4:
            		self.l1Blocks[0].setAddress(address)
            		self.l1Blocks[0].setBitState(bitState)
            		self.l1Blocks[0].setData(data)
		elif address == 1 or address == 5:
            		self.l1Blocks[1].setAddress(address)
            		self.l1Blocks[1].setBitState(bitState)
            		self.l1Blocks[1].setData(data)
		elif address == 2 or address == 6:
            		self.l1Blocks[2].setAddress(address)
            		self.l1Blocks[2].setBitState(bitState)
            		self.l1Blocks[2].setData(data)
		elif address == 3 or address == 7:
            		self.l1Blocks[3].setAddress(address)
            		self.l1Blocks[3].setBitState(bitState)
            		self.l1Blocks[3].setData(data)
		else:
        		print("Direccion incorrecta")
#l1 = L1Cache() 
#l1.l1Blocks[2].memoryAddress = 5	
#for i in range(4):
#	print(l1.l1Blocks[i].id)
#print(l1.getL1BlockByAddress(5).id)
#l1.write(0, 10, "M")
#print(l1.getBlock(0).data)
