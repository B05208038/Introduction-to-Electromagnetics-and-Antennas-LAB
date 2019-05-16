import RPi.GPIO as GPIO
import time 
GPIO.setmode (GPIO.BOARD)
LED_PIN1 = 16
LED_PIN2 = 18
LED_PIN3 = 22
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)

print "LED is on "
GPIO.output(LED_PIN1, GPIO.HIGH)
GPIO.output(LED_PIN2, GPIO.HIGH)
GPIO.output(LED_PIN3, GPIO.HIGH)
time.sleep(3)

GPIO.cleanup()