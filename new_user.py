import digipot
import time
import numpy as np
import adc

#setting initial value - digipot
digipot.write_digipot(0xB00000)

alpha = 2.50	#reference of AD620 amplifier
res = 0		#count resistance
output_values = np.array([])	#initialize array for output values

try:
    while(True):
        
        #read value of ADC
        out = adc.read_adc(1)
        
        
        if (out > alpha + 0.05):
                
            #store the digipot value
            #digipot.write_digipot(0x20000)
            output_values = np.abs(output_values - alpha)
            V_initial = np.min(output_values)
            print(V_initial)
            null_index = np.argmin(output_values)

            input("enter:")

            v_after = out
            print(v_after)
            input("enter2:")
            digipot.write_digipot(0xB00000)
            while(True):
                out_after = adc.read_adc(1)
                if (round(out_after,3) == round(v_after,3)):
                    input("enter3:")
                    v_final = adc.read_adc(1)
                    print(v_final)
                    exit()
                else:
                    digipot.write_digipot(0xE00000)
                    #print("increasing ...")
                    time.sleep(0.01)

            
            #print(values_initial, "\n")
            #print(V_initial, "\n") 
            #print(null_index, "\n")
            
            #decrement the ADC to the minimum index
            '''''
            digipot.write_digipot(0xB00000)

            for i in range(null_index):
                digipot.write_digipot(0xE00000)
                time.sleep(0.01)
                #print("decreasing ...")
            
            #print("calibrated ...")
            
            #read the value of ADC at the minimum index
            V_final = adc.read_adc(1)
            print("Null point voltage from array= ", V_initial)
            print("Null point voltage calibrated = ", V_final - 2.5)
            
            #calculating the resistance R_bw
            
            null_res = 50 + ((null_index)*8730/1017)
            k = (9890 + (8730 - null_res) ) / (9910 + null_res)
            print("Resistance - B & Wiper = ", null_res)
            print("K = ", k)
            
            
            # writing data to file
            
            exit()
            '''
            
            
        else:
            digipot.write_digipot(0xE00000)
            #print("increasing ...")
            time.sleep(0.01)
            output_values = np.append(output_values, out)
            #res = res + 1
			
except IOError as e:
	print(e)
   
except KeyboardInterrupt:
	print("ctrl + c:")
	print("Program end")
	exit()