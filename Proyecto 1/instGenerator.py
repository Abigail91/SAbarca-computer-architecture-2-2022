import time
			
def randomNum(n):
	t0 = str(time.time())
	t0 = t0.replace('.','0')
	p = int(t0[-2:])/100
	i = 0
	ex = 0
	while(i < n):
		t = str(time.time())
		t = t.replace('.','0')
		r = int(t[-2:])/100
		if(r<p):
			ex = ex + 1
		i = i+1
	return ex
def genInstruction():
	inst = randomNum(2)
	address = bin(randomNum(7))[2:]
	while len(address) < 3:  
		address = "0" + address
	if inst == 0:
		data = hex(randomNum(65535))[2:]
		instResult = "WRITE " + str(address)+ ";" + data
	elif inst == 1:
		instResult = "READ " + str(address)
	elif inst == 1:
		instResult = "CALC "
	else:
		instResult = "CALC "
	return instResult
	
for i in range(10):
	print(genInstruction())

# 16 bits	
