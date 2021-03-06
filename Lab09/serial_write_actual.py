import time
import serial 

ser = serial.Serial(
	
	port = '/dev/ttyUSB0',
	baudrate = 9600, 
	parity = serial.PARITY_NONE, 
	stopbits = serial.STOPBITS_ONE, 
	bytesize = serial.EIGHTBITS, 
	timeout = 1
)
counter = 0

while 1: 
	stream = input()
	ser.write(str.encode(stream+'\n'))
	time.sleep(1)
	counter += 1

