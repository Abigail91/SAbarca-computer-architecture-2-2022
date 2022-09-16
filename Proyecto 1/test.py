#c  = Controller("P0", L1Cache(),MemoryBus())
from MemoryBus import MemoryBus
from Memory import Memory
from Processor import Processor
from L1Block import L1Block
memory =  Memory()
b = MemoryBus(memory)
p0 = Processor(0, b)
p1 = Processor(1, b)
p2 = Processor(2, b)
p3 = Processor(3, b)
b.processors = [p0, p1, p2,p3]

	
p0.control.cache.getBlock(2).setAddress(2)
p0.control.cache.getBlock(2).setBitState("I")
p0.control.cache.getBlock(2).setData(5)
p3.control.cache.getBlock(2).setAddress(2)
p3.control.cache.getBlock(2).setBitState("M")
p3.control.cache.getBlock(2).setData(5)
b.sharedAddressP(2, 1)
print(b.readMemory(2))
p2.control.read(2)
p2.control.cache.getBlock(2).printBlock()
p0.control.cache.getBlock(2).printBlock()
p3.control.cache.getBlock(2).printBlock()
print(b.readMemory(2))
