import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(40, GPIO.IN)
GPIO.setup(37, GPIO.OUT)

print "Please press ctrl+c to exit"
time.sleep(2)
print "ready"
time.sleep(2)


try:
	while True:
		if (GPIO.input(40)==1):
			print "motion detected"
			GPIO.output(35, GPIO.HIGH)
			GPIO.output(37, GPIO.LOW)
			time.sleep(6)
		if (GPIO.input(40)==0):
			print "nothing @@ "
		GPIO.output(37, GPIO.HIGH)
		GPIO.output(35, GPIO.LOW)
		time.sleep(1)

except KeyboardInterrupt:
	print("program camncelled")

finally: 
    GPIO.cleanup()


