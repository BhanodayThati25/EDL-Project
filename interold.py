import RPi.GPIO as GPIO
import time
import ADS1263

GPIO.setmode(GPIO.BCM)

# set the pin numbers for the Digipot click - consecutive GPIO pins on raspberry pi
cs_pin = 17
sclk_pin = 27
mosi_pin = 22
	
REF = 5.08
                    
alpha = 2.5

# sending 24 bit data

def write_digipot(data):
	# set the GPIO pins as outputs
	GPIO.setup(cs_pin, GPIO.OUT)
	GPIO.setup(sclk_pin, GPIO.OUT)
	GPIO.setup(mosi_pin, GPIO.OUT)
	# select digipot
	GPIO.output(cs_pin, 0)
	# set the GPIO pins as outputs


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
	
#digipot_value = 0xB00001
#write_digipot(digipot_value)               
while(True):
	ADC = ADS1263.ADS1263()

	# The faster the rate, the worse the stability
	# and the need to choose a suitable digital filter(REG_MODE1)
	if (ADC.ADS1263_init_ADC1('ADS1263_400SPS') == -1):
		exit()

	ADC.ADS1263_SetMode(0) # 0 is singleChannel, 1 is diffChannel

	# ADC.ADS1263_DAC_Test(1, 1)      # Open IN6
	# ADC.ADS1263_DAC_Test(0, 1)      # Open IN7

	# ADC1 Test
	channelList = [0]
	
	# set the bits for Digi pot resistance
	digipot_value = 0xB00001
	write_digipot(digipot_value)
	
	try:
		# The channel must be less than 10
		ADC_Value = ADC.ADS1263_GetAll(channelList)    # get ADC1 value
		out_1 = ADC_Value[0] * REF / 0x7fffffff
		print ("out1 = %lf"%out_1)
		
		if (abs(out_1)<=alpha):
				#pwm.ChangeDutyCycle(100)
				digipot_value = 0x200000
				print("success");
				exit()
		elif ((out_1)>alpha):
			digipot_value = 0xE00000
		elif ((out_1)<-alpha):
			digipot_value = 0x600000

	except IOError as e:
		print(e)
   
	except KeyboardInterrupt:
		print("ctrl + c:")
		print("Program end")
		ADC.ADS1263_Exit()
		exit()
	

