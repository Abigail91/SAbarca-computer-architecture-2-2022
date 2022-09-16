class L1Block:
	def  __init__(self, id):
		self.id = id
		self.bitState = "I"
		self.memoryAddress = 0
		self.data = 0

	def getId(self):
        	return self.id

	def setId(self, number):
        	self.id = id
		
	def getBitState(self):
        	return self.bitState

	def setBitState(self, state):
        	self.bitState = state

	def getAddress(self):
        	return self.memoryAddress

	def setAddress(self, address):
        	self.memoryAddress = address

	def getData(self):
        	return self.data

	def setData(self, data):
        	self.data = data

#l = L1Block("B0")
#print(l.id)
#print(l.bitState)
#l.bitState = "M"
#print(l.bitState)
		
