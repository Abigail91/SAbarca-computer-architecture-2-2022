from L1Block import L1Block
class L1Cache:
	def  __init__(self):
		self.l1Blocks = [L1Block("B0"), L1Block("B1"), L1Block("B2"),L1Block("B3")]

	def getL1BlockByAddress(self, address):
		for l1Block in self.l1Blocks:
			if l1Block.memoryAddress == address:	
				return l1Block 
				
	def write(self, address, data, bitState):
#l1 = L1Cache() 
#l1.l1Blocks[2].memoryAddress = 5	
#for i in range(4):
#	print(l1.l1Blocks[i].id)
#print(l1.getL1BlockByAddress(5).id)
