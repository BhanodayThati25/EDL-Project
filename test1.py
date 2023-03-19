def input(user,mode):
	if mode==0:
		file_path = f"/home/pi/Desktop/EDL-Project/CYFRA/{user}.txt"
		
		# Open the file in write mode
		with open(file_path, "w") as file:
			# Write some data to the file
			file.write(str(2*int(user)))
	if mode==1:
		file_path = f"/home/pi/Desktop/EDL-Project/CEA/{user}.txt"
		
		# Open the file in write mode
		with open(file_path, "w") as file:
			# Write some data to the file
			file.write(str(2*int(user)))
	

