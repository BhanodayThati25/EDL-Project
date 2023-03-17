import adc
import time
import digipot

#set digipot to minimum resistance
digipot.write_digipot(0xB001FF)

#resistance count
res = 0

while(True):
	out0 = adc.read_adc(0)
	#out1 = adc.read_adc(1)
	out = out0 #- out1
	print("output value : ", out)

