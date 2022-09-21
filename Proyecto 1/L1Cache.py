from L1Block import L1Block
class L1Cache:
	def  __init__(self):
		self.l1Blocks = [L1Block("0"), L1Block("1"), L1Block("2"),L1Block("3")]
		
	def getBlock(self, id):
		return self.l1Blocks[id]

	def getL1BlockByAddress(self, address):
		resultB = L1Block(0)
		for l1Block in self.l1Blocks:
			if l1Block.memoryAddress == address:	
				resultB = l1Block
		return resultB 
				
	def write(self, address, data, bitState):
		if address == 0 or address == 4:
			block = L1Block(0)
			block.setAddress(self.l1Blocks[0].getAddress())
			block.setBitState(self.l1Blocks[0].getBitState())
			block.setData(self.l1Blocks[0].getData())
			self.l1Blocks[0].setAddress(address)
			self.l1Blocks[0].setBitState(bitState)
			self.l1Blocks[0].setData(data)
		elif address == 1 or address == 5:
			block = L1Block(1)
			block.setAddress(self.l1Blocks[1].getAddress())
			block.setBitState(self.l1Blocks[1].getBitState())
			block.setData(self.l1Blocks[1].getData())
			self.l1Blocks[1].setAddress(address)
			self.l1Blocks[1].setBitState(bitState)
			self.l1Blocks[1].setData(data)
		elif address == 2 or address == 6:
			block = L1Block(2)
			block.setAddress(self.l1Blocks[2].getAddress())
			block.setBitState(self.l1Blocks[2].getBitState())
			block.setData(self.l1Blocks[2].getData())
			self.l1Blocks[2].setAddress(address)
			self.l1Blocks[2].setBitState(bitState)
			self.l1Blocks[2].setData(data)
		elif address == 3 or address == 7:
			block = L1Block(3)
			block.setAddress(self.l1Blocks[3].getAddress())
			block.setBitState(self.l1Blocks[3].getBitState())
			block.setData(self.l1Blocks[3].getData())
			self.l1Blocks[3].setAddress(address)
			self.l1Blocks[3].setBitState(bitState)
			self.l1Blocks[3].setData(data)
		else:
			block = L1Block(0)
			print("Direccion incorrecta")
		return block
	
#l1 = L1Cache() 
#l1.l1Blocks[2].memoryAddress = 5	
#for i in range(4):
#	print(l1.l1Blocks[i].id)
#print(l1.getL1BlockByAddress(5).id)
#l1.write(0, 10, "M")
#print(l1.getBlock(0).data)
