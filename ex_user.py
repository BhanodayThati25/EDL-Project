import time
import adc
import digipot
import numpy as np


def input(user,mode):
	if mode==0:
		file_path = f"/home/pi/Desktop/EDL-Project/CYFRA/{user}.txt"

		# Open the file in write mode
		with open(file_path, "r") as f:
			# Write some data to the file
			V_initial = float(f.readline())
			print("null point voltage = ", V_initial)
			k = float(f.readline())
			print("Wheatstone ratio = ", k)
			null_res = float(f.readline())
			print("Null point resistance R_BW = ", null_res)
			res = int(f.readline())
			print("resistance index = ", res)

	if mode==1:
		file_path = f"/home/pi/Desktop/EDL-Project/CEA/{user}.txt"

		# Open the file in write mode
		with open(file_path, "r") as f:
			V_initial = float(f.readline())
			print("null point voltage = ", V_initial)
			k = float(f.readline())
			print("Wheatstone ratio = ", k)
			null_res = float(f.readline())
			print("Null point resistance R_BW = ", null_res)
			res = int(f.readline())
			print("resistance index = ", res)

	#setting digipot to null point
	digipot.write_digipot(0xB00000 + res)

	for i in range(40):
		digipot.write_digipot(0xB00000 + res)
		out0 = adc.read_adc(0)
	
	out0 = adc.read_adc(0)
	#out1 = adc.read_adc(1)
	out = out0 #- out1
	V_final = out - 2.5
	
	#print("Output value : ", V_final)
	delta_V = abs(V_final - V_initial)
	#print("Delta_V = ", delta_V)
	delta_R = delta_V*(k+1)*(k+1)
	delta_R = delta_R/(5*k - delta_V*(k+1))
	#print("Delta_R/R = ", delta_R)
	
	response_output = 100*(delta_R/(1 + delta_R))
	#print("Response = ", response_output)
	
	#concentration calculations
	resp = response_output
	#CEA - 0, CYFRA - 1
	mode = 0
	
	if(mode == 0):
		conc = (-0.0088*(resp**3)) + (2.8864*(resp**2)) + (605.27*(resp)) - 4856.59
		#print("Concentration - CEA = ", conc/1000)
		return(resp)

	if(mode == 1):
		conc = 0.147*(resp**3) + 14.5234*(resp**2) - 111.263*(resp) - 1256.154
		#print("Concentration - CYFRA = ", conc/1000)
		return(resp)

	exit()
		
