import RPi.GPIO as GPIO
import time
import ADS1263


# set the pin numbers for the Digipot click - consecutive GPIO pins on raspberry pi

GPIO.setmode(GPIO.BCM)

cs_pin = 17
sclk_pin = 27
mosi_pin = 22
	
REF = 5.08          # Modify according to actual voltage
					# external AVDD and AVSS(Default), or internal 2.5V
					
alpha = 2.5

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

digipot_value = 0xB00001
write_digipot(digipot_value)
                    
while(True):
	ADC = ADS1263.ADS1263()
	
	if (ADC.ADS1263_init_ADC1('ADS1263_400SPS') == -1):
		exit()

	ADC.ADS1263_SetMode(0) # 0 is singleChannel, 1 is diffChannel

	# ADC1 Test
	channelList = [0]
	
	# set the bits for Digi pot resistance
	
	try:
		# The channel must be less than 10
		ADC_Value = ADC.ADS1263_GetAll(channelList)    # get ADC1 value
		time.sleep(1)
		if(ADC_Value[0]>>31 ==1):
			out_1 = (REF*2 - ADC_Value[0] * REF / 0x80000000)
		else:
			out_1 = (ADC_Value[0] * REF / 0x7fffffff)
		print ("out1 = %lf"%out_1)
		
		
		if (abs(out_1)<=alpha):
				digipot_value = 0x200000
				write_digipot(digipot_value)
				time.sleep(1)
				print("success");
				exit()
				
		elif (out_1>alpha):
			digipot_value = 0xE00000
			write_digipot(digipot_value)
			
			time.sleep(1)
			print("yes")
			
		elif (out_1<-alpha):
			digipot_value = 0x600000
			write_digipot(digipot_value)
			time.sleep(1)
			
	
	except IOError as e:
		print(e)
	   
	except KeyboardInterrupt:
		print("ctrl + c:")
		print("Program end")
		ADC.ADS1263_Exit()
		exit()
