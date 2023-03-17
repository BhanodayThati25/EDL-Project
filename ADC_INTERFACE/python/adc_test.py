import adc
import time
import digipot

#set digipot to minimum resistance
digipot.write_digipot(0xB00000)

#resistance count
res = 0

while(True):
    out0 = adc.read_adc(0)
    print("output = ", out0)
    digipot.write_digipot(0xE00000)

exit()
