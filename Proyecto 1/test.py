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

	
p0.control.write(3, 99)
p1.control.read(3)
p2.control.read(3)
p2.control.read(3)
p2.control.write(3,12)
p2.control.read(7)
p1.control.read(7)
p1.control.write(7, 50)

#b.writeMemory(3, 99)
#p0.control.read(2)
#p2.control.cache.getBlock(3).printBlock()

#p3.control.read(3)
#p2.control.cache.getBlock(3).printBlock()
#p3.control.cache.getBlock(3).printBlock()

p0.control.printCache()
p1.control.printCache()
p2.control.printCache()
p3.control.printCache()
memory.printMem()
