import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
p = GPIO.PWM(40, 50)
p.start(0)
time.sleep(5)

try: 
	while True:
		p.ChangeDutyCycle(7.5)
		print "zero degree now"
		time.sleep(3)
		p.ChangeDutyCycle(14.5)
		print "+90 now"
		time.sleep(3)
		p.ChangeDutyCycle(4.5)
		print "-90 now"
		time.sleep(3)

except KeyboardInterrupt:
	GPIO.cleanup()
