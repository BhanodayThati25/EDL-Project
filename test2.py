def input(user,mode):
	if mode==0:
		file_path = f"/home/pi/Desktop/app/CYFRA/{user}.txt"

		# Open the file in write mode
		with open(file_path, "r") as file:
			# Write some data to the file
			contents = file.read()
	if mode==1:
		file_path = f"/home/pi/Desktop/app/CEA/{user}.txt"

		# Open the file in write mode
		with open(file_path, "r") as file:
			# Write some data to the file
			contents = file.read()
	return(contents)
