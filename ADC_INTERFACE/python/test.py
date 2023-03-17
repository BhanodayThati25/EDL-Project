import time
import adc
import digipot
import numpy as np

#output_values = np.array([])

try:
	file_name = input("Enter the file name: ")
	with open(str(file_name), "r") as f:
		
		V_initial = float(f.readline())
		print("null point voltage = ", V_initial)
		k = float(f.readline())
		print("Wheatstone ratio = ", k)
		null_res = float(f.readline())
		print("Null point resistance R_BW = ", null_res)
		res = int(f.readline())
		print("resistance index = ", res)

	#setting digipot to null point
	digipot.write_digipot(0xB00000+res)

	for i in range(50):
		digipot.write_digipot(0xB00000+res)
		out0 = adc.read_adc(0)
		out1 = adc.read_adc(1)
		out = out0 - out1
		print("Voltage = ", out)

	#mean calculation
	"""
	#100 readings of ADC after change in resistance
	for i in range(100):
		out0 = adc.read_adc(0)
		out1 = adc.read_adc(1)
		out = out0 - out1

		#print(out)
		output_values = np.append(output_values, out)

	#finding the mean of the array
	"""
	out0 = adc.read_adc(0)
	out1 = adc.read_adc(1)
	out = out0 - out1

	#output
	V_final = out
	print("Output value : ", V_final)
	
	delta_V = abs(V_final - V_initial)
	print("Delta_V = ", delta_V)
	delta_R = delta_V*(k+1)*(k+1)
	delta_R = delta_R/(5*k - delta_V*(k+1))
	print("Delta_R/R = ", delta_R)
	
	response_output = 100*(delta_R/(1 + delta_R))
	print("Response = ", response_output)
	
	#results - writing data to file
	"""
	file = open(file_name, "a")
	file.write("Results : ")
	file.write(str(delta_V) + "\n")
	file.write(str(delta_R) + "\n")
	file.write(str(response_output) + "\n")
	"""
	exit()
		
	 
except IOError as e:
	print(e)
   
except KeyboardInterrupt:
	print("ctrl + c:")
	print("Program end")
	exit()
