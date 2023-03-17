import digipot
import time
import adc

#intialize digipot to 0 resistance between B and Wiper
digipot.write_digipot(0xB00200)

for i in range(468):
	#increase the wiper position towards A from B
	digipot.write_digipot(0xE00000)
	print("increasing")	#for debugging
	#out0 = adc.read_adc(0)
	#out1 = adc.read_adc(1)
	#out = out0
	#print("Output voltage : ", out)
	time.sleep(0.1)		#delay of 100ms
