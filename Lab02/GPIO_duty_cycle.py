import time 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(22, GPIO.OUT)
p1 = GPIO.PWM(16, 1)
#p2 = GPIO.PWM(18, 1)
#p3 = GPIO.PWM(22, 1)
p1.start(0)

p1.ChangeDutyCycle(50)
p1.ChangeFrequency(1)
time.sleep(3); 
p1.ChangeFrequency(1*2)
time.sleep(1.5); 
p1.ChangeFrequency(1)
time.sleep(3); 

p1.stop()
GPIO.cleanup()