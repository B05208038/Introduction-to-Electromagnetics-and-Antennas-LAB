import RPi.GPIO as GPIO
import time
#import motor, setting it up
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
p = GPIO.PWM(40, 50)
p.start(0)
time.sleep(5)
#adjust degree here
zero = 7.5
NT = 16.5
MNT = 3.0
######
#import infared
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.IN)


try: 
    while True:
        if (GPIO.input(8) == True):
            p.ChangeDutyCycle(NT)
            print "+90 now"
            #time.sleep(3)
        if (GPIO.input(8) == False):
            p.ChangeDutyCycle(MNT)
            print "-90 now"
            #time.sleep(3)

except KeyboardInterrupt:
    print "interrupted, stop code"
    GPIO.cleanup()
