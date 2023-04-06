import adc
import time
import digipot
def input(user,mode):
	#set digipot to minimum resistance
	digipot.write_digipot(0xB00000)

	#resistance count
	res = 0

	while(True):
		out0 = adc.read_adc(0)
		#out1 = adc.read_adc(1)
		out = out0 - 2.5
		#print("outputvalue : ", out)

		if(out > 0.004):
			#increase the digipot value by 10 ohm
			digipot.write_digipot(0xE00000)
			res += 1	#increment by 1
			#time.sleep(0.001)	#delay of 50ms
			
		else:
			digipot.write_digipot(0x200000)		#store the digipot value
			#print("null point : ", out)

			#resistance calculations
			null_res = (res*(9950/1024))
			k = ((9990 + null_res)/(9890 + 8770 - null_res))
			#print("Null point ratio : ", k)
			#print("Null point resistance : ", null_res)
			#print("null index : ", res)

			#write contents to file
			#file_name = input("Enter the file name: ")
			if mode==0:
				file_path = f"/home/pi/Desktop/EDL-Project/CYFRA/{user}.txt"
				
				# Open the file in write mode
				with open(file_path, "w") as file:
					# Write some data to the file
					file.write(str(out) + "\n")
					file.write(str(k) + "\n")
					file.write(str(null_res) + "\n")
					file.write(str(res) + "\n")
			if mode==1:
				file_path = f"/home/pi/Desktop/EDL-Project/CEA/{user}.txt"
				
				# Open the file in write mode
				with open(file_path, "w") as file:
				# Write some data to the file
					file.write(str(out) + "\n")
					file.write(str(k) + "\n")
					file.write(str(null_res) + "\n")
					file.write(str(res) + "\n")
			#file = open(user, "w")
			#file.write(str(out) + "\n")
			#file.write(str(k) + "\n")
			#file.write(str(null_res) + "\n")
			#file.write(str(res) + "\n")
			break
	
