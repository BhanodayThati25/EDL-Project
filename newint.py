import RPi.GPIO as GPIO
import time
import ADS1263


# set the pin numbers for the Digipot click - consecutive GPIO pins on raspberry pi

GPIO.setmode(GPIO.BCM)
ADC = ADS1263.ADS1263()

if (ADC.ADS1263_init_ADC1('ADS1263_400SPS') == -1):
		exit()

ADC.ADS1263_SetMode(0) # 0 is singleChannel, 1 is diffChannel

channelList = 0
cs_pin = 17
sclk_pin = 27
mosi_pin = 22
REF = 5.08       			
alpha = 2.5
sigma = 0.01

def write_digipot(data):
	# sending 24 bit data
	# set the GPIO pins as outputs
	GPIO.setup(cs_pin, GPIO.OUT)
	GPIO.setup(sclk_pin, GPIO.OUT)
	GPIO.setup(mosi_pin, GPIO.OUT)

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
	
# setting initial value of the digipot

digipot_value = 0xB003FF
write_digipot(digipot_value)
#digipot_value = 0xE00000

res = digipot_value & 0x000FFF
#res_aw = 8730-((res)*8730/1024)
res_aw = 1024 - res
while(True):
	try:
		# The channel must be less than 10
		ADC_Value = ADC.ADS1263_GetChannalValue(0)    # get ADC1 value
		#time.sleep(1)
		if(ADC_Value>>31 ==1):
			out_1 = (REF*2 - ADC_Value * REF / 0x80000000)
		else:
			out_1 = (ADC_Value * REF / 0x7fffffff)
		print ("out1 = %lf"%out_1)
		
		
		if (abs(out_1-alpha) <= sigma):
			digipot_value = 0x200000
			write_digipot(digipot_value)
			print("success");
			R_dec = 50 + ((res)*8730/1024)
			print("Resistance :", 50 + ((res)*8730/1024))#R_BW
			exit()
			
		elif (out_1 > (alpha+sigma)):
			digipot_value = 0x700000
			write_digipot(digipot_value)
			res_aw = res_aw+ 1
			res =1024 - res_aw 
			print("dec")
			
		elif (out_1 < (alpha-sigma)):
			digipot_value = 0xE00000
			write_digipot(digipot_value)
			print("inc")
			res = res + 1
			#time.sleep(1)
			
		#ADC.ADS1263_Exit()
	#k= 9.86+R_dec / (9.89+(8730-R_dec))

	except IOError as e:
		print(e)
	   
	except KeyboardInterrupt:
		print("ctrl + c:")
		print("Program end")
		ADC.ADS1263_Exit()
		exit()
