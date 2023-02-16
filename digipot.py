
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# set the pin numbers for the Digipot click

# consecutive GPIO pins on raspberry pi
cs_pin = 17
sclk_pin = 27
mosi_pin = 22

# set the GPIO pins as outputs
GPIO.setup(cs_pin, GPIO.OUT)
GPIO.setup(sclk_pin, GPIO.OUT)
GPIO.setup(mosi_pin, GPIO.OUT)

# sending 24 bit data

def write_digipot(data):
	
	# select digipot
	GPIO.output(cs_pin, 0)
	
	#shift data word - MSB first
	for i in range(24):
		if data & 0x800000:
			GPIO.output(mosi_pin, 1)
		else:
			GPIO.output(mosi_pin, 0)
			
		#pulse clock
		GPIO.output(sclk_pin, 1)
		GPIO.output(sclk_pin, 0)
		
		# shift data to right
		data = data << 1
		
		#delay
		#time.sleep(0.1)
		
	# deselect the digipot
	GPIO.output(cs_pin, 1)
	
	# GPIO.cleanup()
	
# set the bits for Digi pot resistance
digipot_value = 0xE00000
res = 0
write_digipot(0xB00000)
write_digipot(digipot_value)
for i in range(5):
	write_digipot(digipot_value)


"""
for i in range(1024):
	write_digipot(digipot_value)
	res += 1
	Res_f = 50 + ((res)*8730/1024)
	print("Resistance :", 50 + ((res)*8730/1024))
	if Res_f > 8720 :
		print(res)
		print("Resistance :", 50 + ((res)*8730/1024))
		exit()
	
	time.sleep(0.01)


value = 0xB003FF
print(value & 0x000FFF)
"""
