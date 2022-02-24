import spidev
import time
import os
from matplotlib import pyplot as plt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

def read(ch) :
	adc = spi.xfer2([1,(8+ch)<<4,0])
	data = ((adc[1] & 3) << 8) + adc[2]
	return data
	time.sleep(50)
list =[]
timing =[]
value = 0
threshold = 4.1
current_time=time.time()
print( current_time)
elapse_time = 0

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
#adding first data
doc_ref = db.collection('sensor').document('alcohol')

while ( elapse_time < 60) :
	cc = read(value)
	v = cc /100
	list.append(v)
	timing.append(time.time())
	elapse_time=(time.time()) - current_time
	print (v)
	doc_ref.set({

    'value': v

    })
	time.sleep(3)
	
#	if (v > threshold) :
#		print('! ! ! alcohol detected ! ! !' + str(v))
#	else :
#		print('no alcohol detected' + str(v))
	#print (list)
plt.style.use("dark_background")
plt.figure(figsize=(30,15))
plt.title('Sensor values over time (without alcohol )')
plt.subplot(222)
plt.plot( timing, list)


plt.grid(True)
plt.show()






