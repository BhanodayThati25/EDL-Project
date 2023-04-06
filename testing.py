file_path = f"C:\\Academics\\sem6\\EDL\\EDL-Project\\CYFRA\\r.txt"

		# Open the file in write mode
with open(file_path, "r") as f:
		# Write some data to the file
		V_initial = float(f.readline())
		print(V_initial)