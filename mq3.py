import spidev
import time
import os
from matplotlib import pyplot as plt
import datetime as dt 
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = []
ys = []
def read(ch) :
	adc = spi.xfer2([1,(8+ch)<<4,0])
	data = ((adc[1] & 3) << 8) + adc[2]
	return data
	time.sleep(50)
	
value = 0
threshold = 4.1
list =[]

while True :
	cc = read(value)
	v = cc / 100
	list.append(v)
#	if (v > threshold) :
#		print('! ! ! alcohol detected ! ! !' + str(v))
#	else :
#		print('no alcohol detected' + str(v))
#	print (list)
    
    
xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
ys.append(list)
xs = xs[-20:]
ys = ys[-20:]
ax.clear()
ax.plot(xs,ys)
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.title('Sensor values over time (without alcohol )')
plt.ylabel('values ')
plt.show()
print('yy')
time.sleep(5)
