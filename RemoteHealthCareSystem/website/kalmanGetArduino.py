import serial
ser=serial.Serial('COM3', baudrate=9600, timeout=1)
def get_glucose():
	count=0
	minm=[]
	while count<=100:
		data=ser.readline().decode('ascii').strip()
		if(data!='' and count>15):
			minm.append(data)
		count+=1
		#print(data)
	k=[float(i) for i in minm]
	return(k)