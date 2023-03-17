import ADS1263

#ADC initialization
ADC = ADS1263.ADS1263()

if (ADC.ADS1263_init_ADC1('ADS1263_14400SPS') == -1):
		exit()

ADC.ADS1263_SetMode(0) # 0 is singleChannel, 1 is diffChannel

#setting the reference of the ADC
REF = 5.08

	
def read_adc(channel_number):
	# get ADC1 value - assign channel
	ADC_Value = ADC.ADS1263_GetChannalValue(channel_number)
	
	# reading values from ADC
	if(ADC_Value>>31 ==1):
		out = (REF*2 - ADC_Value * REF / 0x80000000)
	else:
		out = (ADC_Value * REF / 0x7fffffff)
	
	return out

#exit the ADC
