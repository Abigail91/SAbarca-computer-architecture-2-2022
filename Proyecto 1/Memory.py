import time
class Memory: 
	def  __init__(self):
		self.positions = []
		for i in range(8):
			self.positions += [0]
			
	def write(self, address, data):
		self.positions[address] = data
		
	def read(self, address):
		return self.positions[address]
	def printMem(self):
		for i in range(8):
			print(str(i) + "=" +str(self.positions[i]))
		


#memoria = Memory()
#print(memoria.read(0) )
#print("\n")
#print(memoria.read(4))
#print("\n")
#memoria.write(4,5)
#print(memoria.read(4))
		
