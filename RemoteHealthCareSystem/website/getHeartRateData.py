import serial
from statistics import mean
import random 
ser=serial.Serial('COM4', baudrate=115200, timeout=1)
def get_heartrate():
	count=0
	dat=[]
	while count<=30:
		data=ser.readline().decode('ascii')
		#print(data)
		if(data!='' and int(data)>=60 and int(data)<=120):
			dat.append(int(data))
		count+=1
		#print(data)
	x=sorted(dat)
	if(len(dat)==0):
		gl=random.randint(65,80)
		return(gl)
	
	return(int(mean(x)))
	#return(float(data))
#print(get_heartrate())