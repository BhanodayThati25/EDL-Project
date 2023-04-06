import RPi.GPIO as GPIO
import time

#addressing mode - pins
GPIO.setmode(GPIO.BCM)

#set warnings to false
GPIO.setwarnings(False)

#pin numbers for DIGITAL POTENTIOMETER
cs_pin = 24
sclk_pin = 23
mosi_pin = 25

#set the GPIO pins as outputs
GPIO.setup(cs_pin, GPIO.OUT)
GPIO.setup(sclk_pin, GPIO.OUT)
GPIO.setup(mosi_pin, GPIO.OUT)

def write_digipot(data):
	
	# set the GPIO pins as outputs
	#GPIO.setup(cs_pin, GPIO.OUT)
	#GPIO.setup(sclk_pin, GPIO.OUT)
	#GPIO.setup(mosi_pin, GPIO.OUT)
	
	# sending 24 bit data
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
		
	# deselect the digipot
	GPIO.output(cs_pin, 1)
